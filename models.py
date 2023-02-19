from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(2048))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(100))
    password = db.Column(db.String(2048))
    user_id = db.Column(db.Integer)

    def __init__(self, website, password, user_id):
        self.website = website
        self.password = password
        self.user_id = user_id

    def __repr__(self):
        return '<Password for %r>' % self.website
