from flask import Blueprint, render_template

resume_page = Blueprint('resume_page', __name__, template_folder='templates')


@resume_page.route('/resume')
def resume():
    return render_template('resume.html')
