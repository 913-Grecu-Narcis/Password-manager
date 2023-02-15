from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from .models.user import User
from .models.user import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup')
def signup():
    return render_template('register.html')


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    user_name = request.form['username']
    email = request.form['email']
    confirm_email = request.form['confirm_email']
    password = request.form['password']
    confirm_pass = request.form['confirm_password']

    user = User.query.filter_by(email=email).first()
    print(user)
    if user:
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, password=generate_password_hash(password), name=user_name)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth_bp.route('/login')
def login():
    return render_template('login.html')


@auth_bp.route('/login', methods=['POST'])
def login_post():
    user_email = request.form['email']
    user_password = request.form['password']

    user = User.query.filter_by(email=user_email).first()

    if not user or not check_password_hash(user.password, user_password):
        return redirect(url_for('auth.login'))

    login_user(user)

    return redirect(url_for('profile.profile'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))
