from flask import Blueprint, render_template

admin_page = Blueprint('admin', __name__, template_folder='templates')


@admin_page.route('/admin')
def admin():
    return render_template('admin.html')
