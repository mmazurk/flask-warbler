
# Installation

I just ended up installing all the usual packages plus the email_validator at the end: 

	pip install flask-sqlalchemy
	pip install flask-debugtoolbar
	pip install psycopg2-binary
	pip install flask-wtf
	pip install flask-bcrypt
	pip install email_validator

Rather then messing with Python version in WSL (which is difficult to do and find), I figured I would just install the latest versions and correct the code. 

# Answers to Questions

The two foreign keys in class Follows (tablename 'follows') make a compound primary key; it is assured to be unique because it comes from two PKs.

For variable followers in class User ...

	primaryjoin specifies the condition for joining the primary table with the association table. In a many-to-many relationship, the primary table is the table that has the relationship attribute, while the association table is the table that links the two primary tables together.

	secondaryjoin specifies the condition for joining the association table with the secondary table. In a many-to-many relationship, the secondary table is the table that is being linked to the primary table.

# Reviewing Model with pdb

### pdb commands

	User.query.filter(User.username == 'tuckerdiane').first().location
	User.query.filter(User.username == 'tuckerdiane').first().messages[0].text
	User.query.filter(User.username == 'tuckerdiane').first().followers
	db.session.query(User.id, User.email).filter(User.id < 10).all()
	db.session.query(User.email, User.username).all()
	Message.query.get(1).text

# Confusion

This confused me at first because the jinja templates used g.user ??

	@app.before_request
	def add_user_to_g():
	    """If we're logged in, add curr user to Flask global."""

	    if CURR_USER_KEY in session:
	        g.user = User.query.get(session[CURR_USER_KEY])

	    else:
	        g.user = None

I learned: the g object is a global object provided by Flask that is used to store data that is specific to the current request context. It's a simple way to share data between different parts of a Flask application during the processing of a single request.

# Database

I ran this so I could do the exercises.

	update users
	set bio = 'I like to eat lots of oranges.', location = 'Seattle, WA'
	where username = 'sadman22';

	update users
	set header_image_url = 'https://cdn.pixabay.com/photo/2018/01/05/22/48/couple-3064048_960_720.jpg'
	where username = 'sadman22';

	update users
	set image_url = 'https://randomuser.me/api/portraits/men/41.jpg'
	where username = 'sadman22';

# Notes

I accidentally updated the wrong route. But it looks cool! Checkout the landing page after login!

This assignment is annoying because it's really outdated for multiple reasons:

	People are way beyond Python 3.7, so the pip install -r requirements.txt doesn't work
	All the links to background images are broken and that's annoying; make it hard to debug



