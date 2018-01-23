"""
 admin.py
 管理者路由文件
"""

from flask import Blueprint,render_template
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm
from jobplus.models import User,Company,Job
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return render_template('admin/admin_base.html')


@admin.route('/users')
def admin_users():
    return render_template('admin/users.html')

@admin.route('/users/adduser')
def add_user():
    form = UserRegisterForm()
    return render_template('admin/adduser.html', form=form)

@admin.route('/users/addcompany')
def add_company():
    form = CompanyRegisterForm()
    return render_template('admin/addcompany.html',form=form)

#注释为edit company的实现,需要在具有数据库数据的情况下调试,先注释掉,但是保留html中的链接
#@admin.route('/users/<int:company_id>/editcompany',methods=['GET','POST'])
#def edit_company(company_id):
#    company = Company.query.get_or_404(company_id)
#    form = RegisterForm(obj=company)
#    if form.is_submitted():
#        form.populate_obj(company)
#        db.session.add(company)
#        try:
#            db.session.commit()
#        except:
#            db.session.rollback()
#            flash('has existed','error')
#        else:
#            flash('company has been edited','success')
#            return redirect(url_for('admin.users'))
#    return render_template('admin/edituser.html',form=form, user=user)
#@admin.route('/users/edituser')
#def edit_user
