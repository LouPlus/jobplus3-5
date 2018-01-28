"""
company.py
企业路由文件
"""

from flask import Blueprint,render_template,flash,redirect,url_for,request,current_app
from jobplus.models import User,Job
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm,CompanyEditForm
from flask_login import current_user
company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():
    page = request.args.get('page',default=1, type=int)
    pagination = User.query.filter_by(role=20).paginate(
        page=page,
        per_page=current_app.config['INDEX_PRE_PAGE'],
        error_out=False
    )
    return render_template('company/company_list.html',pagination=pagination)

@company.route('/admin/profile',methods=['GET','POST'])
def profile():
    form = CompanyEditForm()
    form.companyname.data = current_user.companyname
    form.email.data = current_user.email
    form.website.data = current_user.website
    form.address.data = current_user.address
    form.intro.data = current_user.intro
    form.desc.data = current_user.desc
    form.logo.data = current_user.logo
    if form.validate_on_submit():
        form.edit_company(current_user)
        flash('the company information has been updated succeessfully!')
        return redirect(url_for('front.index'))
    return render_template('company/company_profile.html',form=form)

@company.route('/<int:company_id>')
def company_information(company_id):
    company_information = User.query.get_or_404(company_id)
    return render_template('company/company_information.html',company_information=company_information)
