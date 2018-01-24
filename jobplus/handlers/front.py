"""
front.py
首页路由文件
"""

from flask import Blueprint, render_template,flash,redirect,url_for
from jobplus.models import User,Company,Job
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm
from flask_login import login_user, logout_user, login_required
front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('front.index'))
    return render_template('login.html', form=form)

@front.route('/userregister',methods=['GET','POST'])
def userregister():

    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('userregister.html', form=form)

@front.route('/companyregister',methods=['GET','POST'])
def companyregister():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        form.create_company()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html',form=form)


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been loged out!','success')
    return redirect(url_for('.index'))
