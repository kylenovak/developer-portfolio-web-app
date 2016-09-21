from flask import Blueprint, render_template

projects_page = Blueprint('projects',
                          __name__,
                          url_prefix='/portfolio',
                          template_folder='templates')


@projects_page.route('/projects')
def projects():
    return render_template('projects.html')
