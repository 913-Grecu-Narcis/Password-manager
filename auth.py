from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from models import User
from models import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup')
def signup():
    return render_template('register.html')


def signup_validation(user_name, email, confirm_email, password, confirm_pass):
    if email != confirm_email:
        return False, "Emails don't match!"

    if password != confirm_pass:
        return False, "Passwords don't match!"

    if len(user_name) < 4:
        return False, "Username must be at least 4 characters long!"

    if len(password) < 5:
        return False, "Password must be at least 5 characters long!"

    return True, "Signup successfully!"


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    user_name = request.form['username']
    email = request.form['email']
    confirm_email = request.form['confirm_email']
    password = request.form['password']
    confirm_pass = request.form['confirm_password']

    status, message = signup_validation(user_name, email, confirm_email, password, confirm_pass)

    if not status:
        return render_template('register.html', message=message)

    user = User.query.filter_by(email=email).first()
    print(user)
    if user:
        return render_template('register.html', message='There exists an account with this email!')

    new_user = User(email=email, password=generate_password_hash(password), name=user_name)
    db.session.add(new_user)
    db.session.commit()

    flash('Your account has been created!')
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
