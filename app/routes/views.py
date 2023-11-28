from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.models import Application, Professor
from .. import db

from app.forms import ApplicationForm, ProfessorForm  

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    applications = Application.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', applications=applications)


@main.route('/profile')
@login_required
def profile():
    professors = Professor.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', professors=professors)



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




@main.route('/professor/new', methods=['GET', 'POST'])
@login_required
def new_professor():
    form = ProfessorForm()  # If using WTForms
    if form.validate_on_submit():
        new_professor = Professor(
            name=form.name.data,
            letter_draft=form.letter_draft.data,
            contact_info=form.contact_info.data,
            status=form.status.data,
            user_id=current_user.id
        )
        db.session.add(new_professor)
        db.session.commit()
        flash('New letter of recommendation added!', 'success')
        return redirect(url_for('main.profile'))

    return render_template('add_professor.html', form=form)  # Template for adding professor




@main.route('/professor/edit/<int:professor_id>', methods=['GET', 'POST'])
@login_required
def edit_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)
    form = ProfessorForm(obj=professor)

    if form.validate_on_submit():
        professor.name = form.name.data
        professor.letter_draft = form.letter_draft.data
        professor.contact_info = form.contact_info.data
        professor.status = form.status.data

        db.session.commit()
        flash('Letter of recommendation updated successfully!', 'info')
        return redirect(url_for('main.profile'))

    return render_template('edit_professor.html', form=form, professor_id=professor_id)


@main.route('/professor/delete/<int:professor_id>')
@login_required
def delete_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)
    db.session.delete(professor)
    db.session.commit()

    flash('Letter of recommendation deleted!', 'warning')
    return redirect(url_for('main.profile'))

