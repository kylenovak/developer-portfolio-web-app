from flask import Blueprint, render_template, redirect, url_for, request, flash, g
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
            subject_heading = 'kylejnovak.com: '

            msg = Message(subject_heading + contact_form.subject.data,
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[app.config['MAIL_USERNAME']],
                          reply_to=contact_form.email.data)

            msg.body = 'From: {0!s} <{1!s}>\n{2!s}'.format(contact_form.name.data,
                                                           contact_form.email.data,
                                                           contact_form.message.data)

            try:
                mail.send(msg)
            except SMTPAuthenticationError as e:
                app.logger.error('Error sending email for: {0}\n{1}'.format(contact_form.email.data, e))
                flash('Email not sent. Internal server issue.')
                g.contact_form_errors = True
                return render_template('contact.html', contact_form=contact_form)
            except Exception as e:
                app.logger.error('Something unexpected happened while '
                                 'trying to send an email for: {0}\n{1!s}'.format(contact_form.email.data, e))
                g.contact_form_errors = True
                return render_template('contact.html', contact_form=contact_form)
            else:
                flash('Your email was sent!')
                app.logger.info('Email was sent for: {}'.format(contact_form.email.data))
                return redirect(url_for('contact_page.contact'))
        else:
            flash('Contact form has errors. Fix them before continuing.')
            g.contact_form_errors = True

    return render_template('contact.html', contact_form=contact_form)
