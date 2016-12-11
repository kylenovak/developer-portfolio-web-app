from flask import Blueprint, render_template

from kylejnovak.views.projects.services.projects_service import ProjectsService

projects_service = ProjectsService()

projects_page = Blueprint('projects_page', __name__, template_folder='templates')


@projects_page.route('/projects')
def projects_home():
    projects = projects_service.get_all_projects()
    return render_template('projects.html', projects=projects)


@projects_page.route('/projects/<url_slug>')
def project_view(url_slug):
    projects = projects_service.get_all_projects()

    project = projects_service.get_project_by_url_slug(url_slug)
    if project is None:
        return render_template('page_not_found.html', projects=projects), 404

    return render_template('project_view.html', project=project, projects=projects)
