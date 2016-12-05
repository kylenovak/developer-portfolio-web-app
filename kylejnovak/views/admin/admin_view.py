from flask_admin import Admin

from kylejnovak import models
from kylejnovak.database import db

from kylejnovak.views.admin.model_views import CustomAdminIndexView, CustomFileAdmin, SecureModelView, ProjectModelView


admin = Admin(name='Kyle J. Novak',
              index_view=CustomAdminIndexView(),
              base_template='admin.html')

admin.add_view(SecureModelView(models.Welcome, db.session))
admin.add_view(SecureModelView(models.Bio, db.session))
admin.add_view(ProjectModelView(models.Project, db.session))
admin.add_view(SecureModelView(models.Resume, db.session))
admin.add_view(SecureModelView(models.About, db.session))
admin.add_view(SecureModelView(models.Contact, db.session))

admin.add_view(CustomFileAdmin(base_path='./kylejnovak/static/uploads',
                               base_url='/static/uploads/',
                               name='Image Upload'))
