"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase
from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        self.client = app.test_client()

        u1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD1"
        )
        
        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD2"
        )

        db.session.add_all([u1, u2])
        db.session.commit()

        # The PK id's autoincrement and change in setUp and tearDown, so I had to do this
        # I'll check with Zak to see if this is okay 

        f1 = Follows(
            user_being_followed_id = User.query.filter(User.email=="test1@test.com").first().id,
            user_following_id = User.query.filter(User.email=="test2@test.com").first().id  
        )

        db.session.add(f1)
        db.session.commit()

    def tearDown(self):
        """tear down"""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

    def test_user_model(self):
        """Does basic model work?"""

        user = User.query.filter(User.email == "test1@test.com").first()
        self.assertEqual(len(user.messages), 0)
        self.assertEqual(len(user.followers), 1)

    def test_repr_method(self):
        """Does the __repr__ method work?"""

        user = User.query.filter(User.email == "test1@test.com").first()
        self.assertEqual(str(user), "<User #1: testuser1, test1@test.com>")

    # def test_following(self):
    #     """Test the following functionality"""

    #     user1 = User.query.filter(User.email == "test1@test.com").first()
    #     user2 = User.query.filter(User.email == "test2@test.com").first()
    #     self.assertEqual(user1.is_followed_by(user2), True)
    #     self.assertEqual(user2.is_followed_by(user1), False)


