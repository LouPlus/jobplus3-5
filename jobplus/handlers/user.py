"""
user.py
求职者路由文件
"""

from flask import Blueprint,flash,render_template,redirect,url_for
from jobplus.models import User,Job
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm,CompanyEditForm,UserEditForm
from flask_login import current_user
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def index():
    return 'user'

@user.route('/profile',methods=['GET','POST'])
def profile():
    form = UserEditForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.edit_user(current_user)
        flash('the user information has been updated successfully!')
    return render_template('user/userprofile.html',form=form)
