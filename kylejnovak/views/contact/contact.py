from flask import Blueprint, render_template, request, flash, g
from flask_mail import Message

from kylejnovak.forms.contact import ContactForm
from kylejnovak import app, mail

from smtplib import SMTPAuthenticationError

contact_page = Blueprint('contact_page', __name__, template_folder='templates')


@contact_page.route('/contact', methods=('GET', 'POST'))
def contact():
    contact_form = ContactForm()

    if request.method == 'POST':
        app.logger.info('Attempting to send email for: {}'.format(contact_form.email.data))

        if contact_form.validate_on_submit():
            subject_heading = 'www.kylejnovak.com: '

            msg = Message(subject_heading + contact_form.subject.data,
                          sender=contact_form.email.data,
                          recipients=[app.config['MAIL_USERNAME']])
            msg.body = """
                  From: %s <%s>
                  %s
                  """ % (contact_form.name.data, contact_form.email.data, contact_form.message.data)

            try:
                mail.send(msg)
            except SMTPAuthenticationError | Exception as e:
                app.logger.error('Error sending email for: {}\n{}'.format(contact_form.email.data, e))
                flash('Email not sent. Internal server issue.')
                g.contact_form_errors = True
                return render_template('contact.html', contact_form=contact_form)

            flash('Your email was sent.')
            app.logger.info('Email was sent for: {}'.format(contact_form.email.data))
        else:
            flash('Contact form has errors. Fix them before continuing.')
            g.contact_form_errors = True

    return render_template('contact.html', contact_form=contact_form)
