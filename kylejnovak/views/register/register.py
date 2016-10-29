from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_user

from ...database import db
from ...forms.register import RegistrationForm
from ...models.user import User


register_page = Blueprint('register_page', __name__, template_folder='templates')


@register_page.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        user = User()
        register_form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home_page.home'))
    return render_template('register.html', register_form=register_form)
