from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask_simple_crypt import SimpleCrypt

from models import Password
from models import db

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile')
@login_required
def profile():
    entries = Password.query.filter_by(user_id=current_user.id).all()

    return render_template("profile.html", user_name=current_user.name, entries=entries)


@profile_bp.route('/profile', methods=['POST'])
def profile_post():
    user_id = current_user.id
    website = request.form['website']
    password = request.form['password']

    new_pass = Password(website=website, password=password, user_id=user_id)

    db.session.add(new_pass)
    db.session.commit()

    return redirect(url_for('profile.profile'))
