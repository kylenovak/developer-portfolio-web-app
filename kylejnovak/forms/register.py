from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email, ValidationError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from ..models.user import User


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired(), Email()])
    password = StringField('password', validators=[InputRequired()])

    def validate_email(self, field):
        user = User.query.filter(User.email == self.email.data).first()
        if user is not None:
            raise ValidationError('That email already exists.')

    def validate_username(self, field):
        user = User.query.filter(User.username == self.username.data).first()
        if user is not None:
            raise ValidationError('That username is already taken.')
