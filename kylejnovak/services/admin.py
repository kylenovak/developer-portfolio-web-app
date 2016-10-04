from flask import redirect, url_for, flash

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from .. import models
from .database import db


# Add administrative views here
class SecureModelView(ModelView):
    def is_accessible(self):
        # TODO: get User and check if admin privileges/roles
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        flash('You must login to access the Admin interface.')
        return redirect(url_for('login_page.login'))

admin = Admin(name='Kyle J. Novak', template_mode='bootstrap3')
admin.add_view(SecureModelView(models.Project, db.session))
admin.add_view(SecureModelView(models.Resume, db.session))
admin.add_view(SecureModelView(models.About, db.session))
admin.add_view(SecureModelView(models.Contact, db.session))