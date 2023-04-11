
# Installation

I just ended up installing all the usual packages plus the email_validator at the end: 

	pip install flask-sqlalchemy
	pip install flask-debugtoolbar
	pip install psycopg2-binary
	pip install flask-wtf
	pip install flask-bcrypt
	pip install email_validator

Rather then messing with Python version in WSL (which is difficult to do), I figured I would just install the latest versions and correct the code. 

# Part I: Questions

The two foreign keys in class Follows (tablename 'follows') make a compound primary key; it is assured to be unique because it comes from two PKs.

For variable followers in class User ...

	primaryjoin specifies the condition for joining the primary table with the association table. In a many-to-many relationship, the primary table is the table that has the relationship attribute, while the association table is the table that links the two primary tables together.

	secondaryjoin specifies the condition for joining the association table with the secondary table. In a many-to-many relationship, the secondary table is the table that is being linked to the primary table.

## Using pdb

### pdb commands at "/"

	User.query.filter(User.username == 'tuckerdiane').first().location
	User.query.filter(User.username == 'tuckerdiane').first().messages[0].text
	User.query.filter(User.username == 'tuckerdiane').first().followers
	db.session.query(User.id, User.email).filter(User.id < 10).all()
	db.session.query(User.email, User.username).all()
	Message.query.get(1).text

## Confusion

This confused me at first because the jinja templates used g.user ??

	@app.before_request
	def add_user_to_g():
	    """If we're logged in, add curr user to Flask global."""

	    if CURR_USER_KEY in session:
	        g.user = User.query.get(session[CURR_USER_KEY])

	    else:
	        g.user = None

I learned: the g object is a global object provided by Flask that is used to store data that is specific to the current request context. It's a simple way to share data between different parts of a Flask application during the processing of a single request.

## SQL for Postgres

I ran this to create a new user

	update users
	set bio = 'I like to eat lots of oranges.', location = 'Seattle, WA'
	where username = 'sadman22';

	update users
	set header_image_url = 'https://cdn.pixabay.com/photo/2018/01/05/22/48/couple-3064048_960_720.jpg'
	where username = 'sadman22';

	update users
	set image_url = 'https://randomuser.me/api/portraits/men/41.jpg'
	where username = 'sadman22';

I also ran this to insert values for my user: 

	INSERT INTO follows (user_being_followed_id, user_following_id)
	VALUES 
	(2, 301),
	(3, 301),
	(4, 301),
	(6, 301),
	(7, 301),
	(8, 301),
	(33, 301),
	(44, 301),
	(77, 301),
	(66, 301),
	(99, 301),
	(123, 301);

## Notes

I accidentally updated the wrong route. But it looks cool! Checkout the landing page after login! You can see the location and bio.

## Questions for Zak

I should confirm that my try / catch in `def profile()` works as indended. 

Feedback for SB: This assignment is annoying because it's really outdated for multiple reasons:

	People are way beyond Python 3.7, so the pip install -r requirements.txt doesn't work
	All the links to background images are broken and that's annoying; make it hard to debug

## Fix Homepage

The homepage for logged-in-users should show the last 100 warbles only from the users that the logged-in user is following, and that user, rather than warbles from all users.

## Look over the code in app.py related to authentication.

How is the logged in user being kept track of?

	def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id

What is Flask’s g object?

	The g object in Flask is a global variable that is intended to be used as a container for storing information that is specific to the current request, but that should not be persisted across requests.

	The g object is part of Flask's application context, which is a context that is created for a request and this persists for the lifetime of that request. The g object is initialized at the beginning of each request and is available to all code that is executed during that request. Once the request is complete, the g object is destroyed along with the application context.

	@app.before_request
	def before_request():

What is the purpose of add_user_to_g?

	This adds the user to the g object in Flask for the duration of a request (in this case, before we make an HTTP request to a route).

What does @app.before_request mean?

	Again, this is created for a request and persists for the lifetime of that request. The g object is initialized at the beginning of each request and is available to all code that is executed during that request.

# Part II: Add Likes

Add a new feature that allows a user to “like” a warble. They should only be able to like warbles written by other users. They should put a star (or some other similar symbol) next to liked warbles.

They should be able to unlike a warble, by clicking on that star.

On a profile page, it should show how many warblers that user has liked, and this should link to a page showing their liked warbles.

	Question: How do we deal with this repeating

	    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

Adding the likes to the profile page was much harder than I thought but I did it.

