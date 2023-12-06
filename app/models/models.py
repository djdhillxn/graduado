from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    applications = db.relationship(
        "Application", backref="user", lazy=True
    )  
    professors = db.relationship(
        "Professor", backref="user", lazy=True
    ) 
    statements = db.relationship(
        "Statement", backref="user", lazy=True
    )  


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(1000))
    program = db.Column(db.String(1000))
    deadline = db.Column(
        db.DateTime(timezone=True), default=func.now()
    ) 
    application_status = db.Column(db.String(100), default="not_applied")
    fee_payment_done = db.Column(db.Boolean, default=False)
    lors_request = db.Column(db.String(100), default="not_sent")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    letter_draft = db.Column(db.Text)
    contact_info = db.Column(db.String(300))
    status = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Statement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    statement = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
