from flask import Blueprint, render_template, Markup
from kylejnovak.views.resume.services.resume_service import ResumeService

resume_service = ResumeService()

resume_page = Blueprint('resume_page', __name__, template_folder='templates')


@resume_page.route('/resume')
def resume():
    result = resume_service.get_resume()
    return render_template('resume.html', resume_content=Markup(result.resume_content))
