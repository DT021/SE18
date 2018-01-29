from app import app
from .home import *
from .login import *
from .profile import *
from .signup import *
from .about import *
@app.route('/')
@app.route('/home')
def indexhome():
	return home()
@app.route('/login')
def indexlogin():
	return login()
@app.route('/signup')
def indexsignup():
	return signup()
@app.route('/profile')
def indexprofile():
	return profile1()
@app.route('/about')
def indexabout():
	return about()

