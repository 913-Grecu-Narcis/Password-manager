from flask import Flask
from flask_login import LoginManager

from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from .home import home_bp
    from .auth import auth_bp
    from .profile import profile_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    return app


app = create_app()
