# In forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, Length

class ApplicationForm(FlaskForm):
    school_name = StringField('School Name', validators=[DataRequired(), Length(max=1000)])
    program = StringField('Program', validators=[DataRequired(), Length(max=1000)])
    deadline = DateField('Deadline', validators=[DataRequired()], format='%Y-%m-%d')

