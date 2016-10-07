from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, ValidationError
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

from ..models.user import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

    user = None

    def validate_password(self, field):
        try:
            user = User.query.filter(User.username == self.username.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError('Invalid user')

        if user is None:
            raise ValidationError('Invalid user')
        if not user.check_password(self.password.data):
            raise ValidationError('Invalid password')

        self.user = user
