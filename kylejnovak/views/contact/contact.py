from flask import Blueprint, render_template, request, flash, g
from flask_mail import Message

from kylejnovak.forms.contact import ContactForm
from kylejnovak import app, mail

contact_page = Blueprint('contact_page', __name__, template_folder='templates')


@contact_page.route('/contact', methods=('GET', 'POST'))
def contact():
    contact_form = ContactForm()

    if request.method == 'POST':
        app.logger.info('Attempting to send email for: {}'.format(contact_form.email))

        if contact_form.validate_on_submit():
            msg = Message(contact_form.subject.data,
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[app.config['MAIL_USERNAME']])
            msg.body = """
                  From: %s <%s>
                  %s
                  """ % (contact_form.name.data, contact_form.email.data, contact_form.message.data)

            mail.send(msg)

            flash('Your email was sent.')
            app.logger.info('Email was sent for: {}'.format(contact_form.email))
        else:
            flash('Contact form has errors. Fix them before continuing.')
            g.contact_form_errors = True

    return render_template('contact.html', contact_form=contact_form)
