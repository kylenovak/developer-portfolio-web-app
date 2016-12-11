from flask import Blueprint, render_template, request, flash, g

from kylejnovak.forms.contact import ContactForm
from kylejnovak import app

contact_page = Blueprint('contact_page', __name__, template_folder='templates')


@contact_page.route('/contact', methods=('GET', 'POST'))
def contact():
    contact_form = ContactForm()

    if request.method == 'POST':
        app.logger.info('Attempting to send email for: {}'.format(contact_form.email))

        if contact_form.validate_on_submit():
            flash('Your email was sent.')
            app.logger.info('Email was sent for: {}'.format(contact_form.email))
        else:
            flash('All fields are required.')
            g.contact_form_errors = True

    return render_template('contact.html', contact_form=contact_form)
