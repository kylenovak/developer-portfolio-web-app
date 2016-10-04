from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin
import bcrypt

from ..services.database import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(120), unique=True)
    _hashed_password = db.Column(db.String)

    @hybrid_property
    def password(self):
        return self._hashed_password

    @password.setter
    def password(self, password):
        """Sets the password and makes sure the password
        is hashed and salted before getting saved to the database."""
        self._hashed_password = bcrypt.hashpw(password.encode('utf-8'),
                                              bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'),
                             self._hashed_password.encode('utf-8')).decode('utf-8') == self._hashed_password

    def __repr__(self):
        return '<User {:d}>'.format(self.id)

    def __str__(self):
        return self.username
