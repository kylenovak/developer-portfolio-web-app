from flask import redirect, url_for
from flask_login import current_user

from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.form import SecureForm
from flask_admin import AdminIndexView, expose

from kylejnovak.models.project import Project

from kylejnovak.views.admin.ckeditor import CKTextModelView


class CustomAdminIndexView(AdminIndexView):
    """This class is used very that the current_user is
    authorized to view the admin index page / home page."""
    @expose('/')
    def index(self):
        if current_user.is_authenticated and current_user.user_role == 'A':
            return super(CustomAdminIndexView, self).index()
        return redirect(url_for('login_page.login'))


class SecureModelView(CKTextModelView):
    """This class ensures that only authorized users are
    able to view the model views via is_authroized method.

    This class also includes the CKEditor for content/textarea input,
    and ensures CSRF protection on the forms as well."""
    # add CSRF protection
    form_base_class = SecureForm
    # Can delete rows of a table/model
    can_delete = True
    # number of entries to display on the list view
    page_size = 20
    # remove these columns from the list and create views
    column_exclude_list = ['create_date', 'update_date']
    form_excluded_columns = ['create_date', 'update_date']

    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == 'A'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_page.login'))

    def on_model_change(self, form, model, is_created):
        if isinstance(model, Project) and is_created:
            model.url_slug = model.title.replace(' ', '-').lower()


class ProjectModelView(SecureModelView):
    """Project model view. Excludes the content field from the form."""
    form_excluded_columns = ['url_slug', 'create_date', 'update_date']


class CustomFileAdmin(FileAdmin):
    """This class extends FileAdmin to ensure
    only certain image types are uploaded."""
    # only these file types can be uploaded
    allowed_extensions = ('jpg', 'jpeg', 'gif', 'png')

    # add CSRF protection
    form_base_class = SecureForm

    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == 'A'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_page.login'))
