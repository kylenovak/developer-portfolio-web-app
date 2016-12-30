from flask import Blueprint, render_template, Markup

from kylejnovak.views.about.services.about_service import AboutService

about_service = AboutService()

about_page = Blueprint('about_page', __name__, template_folder='templates')


@about_page.route('/about')
def about():
    result = about_service.get_about()
    return render_template('about.html', about_content=Markup(result.content))
