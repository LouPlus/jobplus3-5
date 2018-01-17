"""
front.py
首页路由文件
"""

from flask import Blueprint, render_template,flash,redirect,url_for
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('base.html')


@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@front.route('/userregister',methods=['GET','POST'])
def userregister():

    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('userregister.html', form=form)

@front.route('/companyregister')
def companyregister():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html',form=form)
