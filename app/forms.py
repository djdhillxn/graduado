from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateTimeField,
    DateField,
    TextAreaField,
    SelectField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Email, Optional


class ApplicationForm(FlaskForm):
    school_name = StringField(
        "School Name", validators=[DataRequired(), Length(max=1000)]
    )
    program = StringField("Program", validators=[DataRequired(), Length(max=1000)])
    deadline = DateField(
        "Deadline", validators=[DataRequired()], format="%Y-%m-%d"
    )  
    application_status = SelectField(
        "Application Status",
        choices=[
            ("not_applied", "Not Applied"),
            ("submitted", "Submitted"),
            ("in_process", "In Process"),
        ],
        validators=[DataRequired()],
    )
    fee_payment_done = BooleanField("Fee Payment Done")
    lors_request = SelectField(
        "LORs Request Status",
        choices=[("not_sent", "Not Sent"), ("sent", "Sent")],
        validators=[DataRequired()],
    )


class ProfessorForm(FlaskForm):
    name = StringField("Professor Name", validators=[DataRequired(), Length(max=200)])
    letter_draft = TextAreaField(
        "Letter Draft", validators=[Optional(), Length(max=5000)]
    )
    contact_info = StringField(
        "Contact Info", validators=[Optional(), Email(), Length(max=300)]
    )
    status = SelectField(
        "Status",
        choices=[
            ("pending", "Pending"),
            ("submitted", "Submitted"),
            ("received", "Received"),
        ],
        validators=[DataRequired()],
    )


class StatementForm(FlaskForm):
    name = StringField("Statement Name", validators=[DataRequired(), Length(max=200)])
    statement = TextAreaField(
        "Statement", validators=[DataRequired(), Length(max=5000)]
    )
