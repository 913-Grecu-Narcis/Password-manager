import os

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
DEBUG = True
SECRET_KEY = "5030509070016"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'db.sqlite')
