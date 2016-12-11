from kylejnovak.database import db
from kylejnovak.models.project import Project


class ProjectsService(object):

    def __init__(self):
        self.query = db.session.query
        self.project = Project

    def get_all_projects(self):
        return self.query(self.project).order_by(self.project.create_date.desc()).all()

    def get_project_by_url_slug(self, url_slug):
        return self.query(self.project).filter(self.project.url_slug == url_slug).first()
