import bcrypt

from flask_blog import db
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import current_user

from flask_blog.models import User
from flask_blog.users.forms import RegistrationForm

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt(14)).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, passowrd=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Ваша учетная запись создана', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)
