from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '000000')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')




# Initialize Database
db = SQLAlchemy(app)

# After initializing your SQLAlchemy object (db)
migrate = Migrate(app, db)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from app.models.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Blueprints
from .auth.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .routes.views import main as main_blueprint
app.register_blueprint(main_blueprint)
