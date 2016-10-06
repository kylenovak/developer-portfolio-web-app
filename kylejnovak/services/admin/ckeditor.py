from flask_admin.contrib.sqla import ModelView

from wtforms import TextAreaField
from wtforms.widgets import TextArea


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class CKTextModelView(ModelView):
    # determine which field names get the CKEditor
    form_overrides = dict(content=CKTextAreaField)

    create_template = 'ckeditor.html'
    edit_template = 'ckeditor.html'
