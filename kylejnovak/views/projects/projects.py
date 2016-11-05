from flask import Blueprint, render_template
from kylejnovak.database import db

from kylejnovak.models.project import Project

from sqlalchemy.orm.exc import NoResultFound

projects_page = Blueprint('projects_page', __name__, template_folder='templates')


@projects_page.route('/projects')
def projects_home():
    projects = db.session.query(Project)\
        .order_by(Project.create_date.desc()).all()
    return render_template('projects.html', projects=projects)


@projects_page.route('/projects/<url_slug>')
def project_view(url_slug):
    try:
        project = db.session.query(Project)\
            .filter(Project.url_slug == url_slug).one()
    except NoResultFound:
        return render_template('page_not_found.html'), 404

    projects = db.session.query(Project)\
        .order_by(Project.create_date.desc()).all()

    return render_template('project_view.html', project=project, projects=projects)
