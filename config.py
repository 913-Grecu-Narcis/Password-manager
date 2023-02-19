import os

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
DEBUG = True
SECRET_KEY = b'YUdEYKFfEMiOm-orPotlKYD2-D2IQNCuWi6L4nC17AM='
FSC_EXPANSION_COUNT = 2048

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'db.sqlite')
