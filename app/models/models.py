from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    applications = db.relationship('Application', backref='user', lazy=True)  # Relationship to Application
    professors = db.relationship('Professor', backref='user', lazy=True)  # Relationship to Professor


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(1000))
    program = db.Column(db.String(1000))
    deadline = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Add other application fields

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    letter_draft = db.Column(db.Text)
    contact_info = db.Column(db.String(300))
    status = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

