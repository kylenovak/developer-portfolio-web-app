from flask import Blueprint, render_template, Markup

from kylejnovak.views.about.services.about_service import AboutService

about_service = AboutService()

about_page = Blueprint('about_page', __name__, template_folder='templates')


@about_page.route('/about')
def about():
    about_content = about_service.get_about()

    if about_content is not None and len(about_content) > 0:
        about_content = Markup(about_content[0])

    return render_template('about.html', about_content=about_content)
