import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'this_really_need_to_be_changed'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']