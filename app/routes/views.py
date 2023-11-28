from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import app, db
from app.models.models import Application, Professor, Statement
from app.forms import ApplicationForm, ProfessorForm, StatementForm

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
    statements = Statement.query.filter_by(user_id=current_user.id).all()  # Add this line
    return render_template('profile.html', professors=professors, statements=statements)  # Update this line


@main.route('/application/new', methods=['GET', 'POST'])
@login_required
def new_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        new_application = Application(
            school_name=form.school_name.data, 
            program=form.program.data, 
            deadline=form.deadline.data,
            application_status=form.application_status.data,
            fee_payment_done=form.fee_payment_done.data,
            lors_request=form.lors_request.data,
            user_id=current_user.id
        )
        db.session.add(new_application)
        db.session.commit()
        flash('New application added successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('form_template.html', action='Add', item_type='Application', form=form, url=url_for('main.new_application'))
    #return render_template('add_application.html', form=form)

@main.route('/application/edit/<int:application_id>', methods=['GET', 'POST'])
@login_required
def edit_application(application_id):
    application = Application.query.get_or_404(application_id)
    form = ApplicationForm(obj=application)

    if form.validate_on_submit():
        application.school_name = form.school_name.data
        application.program = form.program.data
        application.deadline = form.deadline.data
        application.application_status = form.application_status.data
        application.fee_payment_done = form.fee_payment_done.data
        application.lors_request = form.lors_request.data

        db.session.commit()
        flash('Application updated successfully!', 'info')
        return redirect(url_for('main.dashboard'))
    return render_template('form_template.html', action='Edit', item_type='Application', form=form, url=url_for('main.edit_application', application_id=application_id))
    #return render_template('edit_application.html', form=form, application_id=application_id)

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

    #return render_template('add_professor.html', form=form)  # Template for adding professor
    return render_template('form_template.html', action='Add', item_type='Professor', form=form, url=url_for('main.new_professor'))


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

    #return render_template('edit_professor.html', form=form, professor_id=professor_id)
    return render_template('form_template.html', action='Edit', item_type='Professor', form=form, url=url_for('main.edit_professor', professor_id=professor_id))



@main.route('/professor/delete/<int:professor_id>')
@login_required
def delete_professor(professor_id):
    professor = Professor.query.get_or_404(professor_id)
    db.session.delete(professor)
    db.session.commit()

    flash('Letter of recommendation deleted!', 'warning')
    return redirect(url_for('main.profile'))


@main.route('/statement/new', methods=['GET', 'POST'])
@login_required
def new_statement():
    form = StatementForm()
    if form.validate_on_submit():
        new_statement = Statement(
            name=form.name.data,
            statement=form.statement.data,
            user_id=current_user.id
        )
        db.session.add(new_statement)
        db.session.commit()
        flash('New statement added successfully!', 'success')
        return redirect(url_for('main.profile'))
    return render_template('form_template.html', action='Add', item_type='Statement', form=form, url=url_for('main.new_statement'))
    #return render_template('add_statement.html', form=form)

@main.route('/statement/edit/<int:statement_id>', methods=['GET', 'POST'])
@login_required
def edit_statement(statement_id):
    statement = Statement.query.get_or_404(statement_id)
    form = StatementForm(obj=statement)

    if form.validate_on_submit():
        statement.name = form.name.data
        statement.statement = form.statement.data

        db.session.commit()
        flash('Statement updated successfully!', 'info')
        return redirect(url_for('main.profile'))
    return render_template('form_template.html', action='Edit', item_type='Statement', form=form, url=url_for('main.edit_statement', statement_id=statement_id))
    #return render_template('edit_statement.html', form=form, statement_id=statement_id)

@main.route('/statement/delete/<int:statement_id>')
@login_required
def delete_statement(statement_id):
    statement = Statement.query.get_or_404(statement_id)
    db.session.delete(statement)
    db.session.commit()

    flash('Statement deleted!', 'warning')
    return redirect(url_for('main.profile'))
