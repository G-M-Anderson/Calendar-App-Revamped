from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app context
    db.init_app(app)
    login_manager.init_app(app)
    
    # Set up login manager configuration
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    # Register Blueprints for modular routes
    from app.routes.auth_routes import auth_bp
    from app.routes.calendar_routes import calendar_bp
    from app.routes.user_routes import user_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(calendar_bp, url_prefix='/calendar')
    app.register_blueprint(user_bp, url_prefix='/user')
    
    return app
