"""
 admin.py
 管理者路由文件
"""

from flask import Blueprint,render_template,flash,redirect,url_for
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm, UserEditForm, CompanyEditForm
from jobplus.models import User,Job,db
from jobplus.decorators import admin_required
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/admin_base.html')


@admin.route('/users')
@admin_required
def admin_users():
    lis = User.query.all()
    return render_template('admin/users.html',ones=lis)

@admin.route('/users/adduser',methods=['GET','POST'])
@admin_required
def add_user():
    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录!','success')
        return redirect(url_for('admin.admin_users'))
    return render_template('admin/adduser.html', form=form)

@admin.route('/users/addcompany',methods=['GET','POST'])
@admin_required
def add_company():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        form.create_company()
        flash('注册成功,请登录!','success')
        return redirect(url_for('admin.admin_users'))
    return render_template('admin/addcompany.html',form=form)

@admin.route('/users/<int:user_id>/edit',methods=['GET','POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_company:
        form = CompanyEditForm(obj=user)
    else:
        form = UserEditForm(obj=user)
    if form.validate_on_submit():
        form.edit_user(user)
        flash('update success','success')
        return redirect(url_for('admin.admin_users'))
    return render_template('admin/edit_user.html',form=form, user=user)



@admin.route('/users/<int:user_id>/disable',methods=['GET','POST'])
@admin_required
def disable_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_disable:
        user.is_disable = False
        flash('已经成功禁止用户','success')
    else:
        user.is_disable = True
        flash('已经成功启用用户','success')
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('admin.admin_users'))
