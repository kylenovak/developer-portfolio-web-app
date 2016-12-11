from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, ValidationError

from kylejnovak.models.user import User
from kylejnovak import app


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

    user = None

    def validate_password(self, field):
        user = User.query.filter(User.username == self.username.data).first()

        if user is None:
            app.logger.error('User not found for username: {}'.format(self.username.data))
            raise ValidationError()
        if not user.check_password(self.password.data):
            raise ValidationError()

        self.user = user
