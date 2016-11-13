from kylejnovak import app

from dateutil import parser


@app.template_filter('datetime')
def _jinja2_filter_datetime(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format = '%b %d, %Y'
    return native.strftime(format)
