from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from . import models
from .database import db


admin = Admin(name='Kyle J. Novak', template_mode='bootstrap3')


# Add administrative views here
class SecureModelView(ModelView):
    def is_accessible(self):
        print(current_user.is_authenticated)
        return current_user.is_authenticated

admin.add_view(SecureModelView(models.Project, db.session))
admin.add_view(SecureModelView(models.Resume, db.session))
admin.add_view(SecureModelView(models.About, db.session))
admin.add_view(SecureModelView(models.Contact, db.session))