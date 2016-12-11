from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired('Name cannot be blank')])
    email = EmailField('Email',  validators=[InputRequired('Email cannot be blank'),
                                             Email('Email must be valid')])
    subject = StringField('Subject', validators=[InputRequired('Subject cannot be blank')])
    message = TextAreaField('Message', validators=[InputRequired('Message cannot be blank')])
    submit = SubmitField('Send')
