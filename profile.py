from cryptography.fernet import Fernet
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from flask_simple_crypt import SimpleCrypt

from models import Password
from models import db

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile')
@login_required
def profile():
    decryptor = Fernet(current_app.secret_key)

    entries = Password.query.filter_by(user_id=current_user.id).all()

    for entry in entries:
        entry.password = decryptor.decrypt(entry.password).decode()

    return render_template("profile.html", user_name=current_user.name, entries=entries)


@profile_bp.route('/profile', methods=['POST'])
def profile_post():
    user_id = current_user.id
    website = request.form['website']
    password = request.form['password']
    encrypted_password = Fernet(current_app.secret_key).encrypt(bytes(password, 'utf-8'))

    entry = Password(website=website, password=encrypted_password, user_id=user_id)

    db.session.add(entry)
    db.session.commit()

    return redirect(url_for('profile.profile'))
