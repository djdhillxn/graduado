# In forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, Optional

class ApplicationForm(FlaskForm):
    school_name = StringField('School Name', validators=[DataRequired(), Length(max=1000)])
    program = StringField('Program', validators=[DataRequired(), Length(max=1000)])
    deadline = DateField('Deadline', validators=[DataRequired()], format='%Y-%m-%d')


class ProfessorForm(FlaskForm):
    name = StringField('Professor Name', validators=[DataRequired(), Length(max=200)])
    letter_draft = TextAreaField('Letter Draft', validators=[Optional(), Length(max=5000)])
    contact_info = StringField('Contact Info', validators=[Optional(), Email(), Length(max=300)])
    status = SelectField('Status', choices=[('pending', 'Pending'), ('submitted', 'Submitted'), ('received', 'Received')], validators=[DataRequired()])

