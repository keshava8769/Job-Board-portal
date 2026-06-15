from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config

# Create extensions (not attached to app yet)
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Attach extensions to the app
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Where to redirect if user isn't logged in
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Register blueprints (routes)
    from app.routes.auth import auth
    from app.routes.jobs import jobs
    from app.routes.applications import applications

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(jobs, url_prefix='/jobs')
    app.register_blueprint(applications, url_prefix='/apply')

    return app