from flask_admin import Admin

from ... import models
from ..database import db

from .model_views import CustomAdminIndexView, CustomFileAdmin, SecureModelView


admin = Admin(name='Kyle J. Novak',
              index_view=CustomAdminIndexView(),
              base_template='admin.html')

admin.add_view(SecureModelView(models.Project, db.session))
admin.add_view(SecureModelView(models.Resume, db.session))
admin.add_view(SecureModelView(models.About, db.session))
admin.add_view(SecureModelView(models.Contact, db.session))

admin.add_view(CustomFileAdmin(base_path='./kylejnovak/static/uploads',
                               base_url='/static/uploads/',
                               name='Image Upload'))
