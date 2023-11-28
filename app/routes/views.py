from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.models import Application
from .. import db

from app.forms import ApplicationForm 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    applications = Application.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', applications=applications)

@main.route('/application/new', methods=['GET', 'POST'])
@login_required
def new_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        new_application = Application(
            school_name=form.school_name.data, 
            program=form.program.data, 
            deadline=form.deadline.data, 
            user_id=current_user.id
        )
        db.session.add(new_application)
        db.session.commit()
        flash('New application added successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('add_application.html', form=form)

@main.route('/application/edit/<int:application_id>', methods=['GET', 'POST'])
@login_required
def edit_application(application_id):
    application = Application.query.get_or_404(application_id)
    form = ApplicationForm(obj=application)

    if form.validate_on_submit():
        application.school_name = form.school_name.data
        application.program = form.program.data
        application.deadline = form.deadline.data

        db.session.commit()
        flash('Application updated successfully!', 'info')
        return redirect(url_for('main.dashboard'))

    return render_template('edit_application.html', form=form, application_id=application_id)

@main.route('/application/delete/<int:application_id>')
@login_required
def delete_application(application_id):
    application = Application.query.get_or_404(application_id)
    db.session.delete(application)
    db.session.commit()

    flash('Application has been deleted!','warning')
    return redirect(url_for('main.dashboard'))

