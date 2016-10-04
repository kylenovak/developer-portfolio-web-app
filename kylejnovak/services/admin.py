from flask import redirect, url_for

from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from .. import models
from .database import db


# Add administrative views here
class SecureModelView(ModelView):
    # Can delete rows of a tabele/model
    can_delete = True
    # number of entries to display on the list view
    page_size = 20
    # remove these columns from the list and create views
    column_exclude_list = ['create_date', 'update_date']
    form_excluded_columns = ['create_date', 'update_date']

    def is_accessible(self):
        # TODO: get User and check if admin privileges/roles
        return current_user.is_authenticated and current_user.user_role == 'A'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_page.login'))


class ProjectView(SecureModelView):
    # search by these columns
    column_searchable_list = ['title']
    # enable inline editting for faster editing in the list view
    column_editable_list = ['title', 'subtitle']


class CustomAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated and current_user.user_role == 'A':
            return super(CustomAdminIndexView, self).index()
        return redirect(url_for('login_page.login'))


admin = Admin(name='Kyle J. Novak',
              index_view=CustomAdminIndexView(),
              base_template='admin.html')
admin.add_view(ProjectView(models.Project, db.session))
admin.add_view(SecureModelView(models.Resume, db.session))
admin.add_view(SecureModelView(models.About, db.session))
admin.add_view(SecureModelView(models.Contact, db.session))