from flask import Blueprint, render_template

projects_page = Blueprint('projects_page', __name__, template_folder='templates')


@projects_page.route('/projects')
def projects():
    return render_template('projects.html')
