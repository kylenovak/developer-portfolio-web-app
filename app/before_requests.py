from flask import g, Markup
from app import app
from datetime import date


def get_copyright_text():
    # app built on this year
    YEAR_APP_BUILT = app.config['YEAR_APP_BUILT']
    CURRENT_YEAR = date.today().year

    copyright_text = '&copy; Copyright {:d} '.format(YEAR_APP_BUILT)

    if CURRENT_YEAR > YEAR_APP_BUILT:
        copyright_text += '- {:d} '
        copyright_text.format(CURRENT_YEAR)
    else:
        copyright_text += 'by {}'.format(app.config['AUTHOR'])

    return copyright_text


@app.before_request
def before_requests():
    # mark this text as safe
    g.copyright_text = Markup(get_copyright_text())
