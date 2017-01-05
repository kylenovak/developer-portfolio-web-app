from flask import Markup
from datetime import date


def get_copyright_text(app):
    year_app_built = app.config['YEAR_APP_BUILT']
    current_year = date.today().year

    copyright_text = 'Copyright &copy; {:d}'.format(year_app_built)

    if current_year > year_app_built:
        copyright_text += ' - {:d}'.format(current_year)

    copyright_text += ' {}'.format(app.config['AUTHOR'])

    return Markup(copyright_text)
