"""
company.py
企业路由文件
"""

from flask import Blueprint,render_template,flash,redirect,url_for,request,current_app
from jobplus.models import User,Job,db
from jobplus.forms import LoginForm, UserRegisterForm, CompanyRegisterForm,CompanyEditForm, JobRegisterForm, JobEditForm
from flask_login import current_user
from jobplus.decorators import company_required
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




@company.route('/<int:company_id>/jobs')
def job_company_admin(company_id):
    company = User.query.get_or_404(company_id)
    return render_template('company/company_job_admin.html',jobs=company.jobs)



@company.route('/job/<int:company_id>/addjob',methods=['GET','POST'])
def add_job(company_id):
    form = JobRegisterForm()
    if form.validate_on_submit():
        form.company_create_job(company_id)
        flash('职位已添加')
        return redirect(url_for('company.job_company_admin',company_id=company_id))
    return render_template('job/job_add.html',form=form)

@company.route('/job/<int:job_id>/online',methods=['GET','POST'])
@company_required
def online_job(job_id):
    job = Job.query.get_or_404(job_id)
    if job.status:
        job.status = False
        flash('已经成功下线职位','success')
    else:
        job.status = True
        flash('已经成功上线职位','success')
    db.session.add(job)
    company = User.query.filter_by(id=current_user.id).first()
    company.jobs.append(job)
    db.session.commit()
    return redirect(url_for('company.job_company_admin',company_id=current_user.id))
@company.route('/job/<int:job_id>/edit',methods=['GET','POST'])
@company_required
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    form = JobEditForm(obj=job)
    if form.validate_on_submit():
        form.edit_job(job)
        flash('update success','success')
        return redirect(url_for('company.job_company_admin',company_id=current_user.id))
    return render_template('job/job_edit.html',job_id=job_id,form=form)
