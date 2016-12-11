from flask import Blueprint, render_template, redirect, flash, url_for, request, g
from flask_login import login_user, login_required, logout_user, current_user

from kylejnovak.forms.login import LoginForm
from kylejnovak import app

login_page = Blueprint('login_page', __name__, template_folder='templates')


@login_page.route('/login', methods=('GET', 'POST'))
def login():
    login_form = LoginForm()

    if request.method == 'POST':
        app.logger.info('Attempting to login as: {}'.format(login_form.username))

        if login_form.validate_on_submit():
            # Tell Flask-Login that user has been authenticated.
            login_user(login_form.user)

            flash('User logged in successfully.')
            app.logger.info('Logged in as user: {}'.format(login_form.user))

            return redirect(url_for('admin.index'))
        else:
            # Login failed, show login template.
            flash('Login attempt failed.')
            app.logger.warning('Login attempt failed for: {}'.format(login_form.username))
            g.login_form_errors = True

    return render_template('login.html', login_form=login_form)


@login_page.route('/logout')
@login_required
def logout():
    app.logger.info('Logging out for user: {}'.format(current_user.username))
    # Tell Flask-Login to destroy the session->User connection for this session.
    logout_user()
    return redirect(url_for('home_page.home'))
