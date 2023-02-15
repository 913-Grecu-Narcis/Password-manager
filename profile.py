from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile')
@login_required
def profile():
    return render_template("user.html", user_name=current_user.name)


@profile_bp.route('/profile', methods=['POST'])
def profile_post():
    pass