"""
job.py
职位路由文件
"""

from flask import Blueprint,render_template,flash,redirect,url_for,request,current_app
from jobplus.models import User,Job,Resume,db
from flask_login import current_user,login_required
job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    page = request.args.get('page',default=1, type=int)
    pagination = Job.query.filter_by(status='1').paginate(
        page=page,
        per_page=current_app.config['INDEX_PRE_PAGE'],
        error_out=False
    )
    return render_template('job/job_list.html',pagination=pagination)


@job.route('/<int:job_id>')
def job_information(job_id):
    job_information = Job.query.get_or_404(job_id)
    return render_template('job/job_information.html',job_information=job_information)



@job.route('/<int:job_id>/apply')
def job_apply(job_id):
    job = Job.query.get_or_404(job_id)
    if job.current_user_is_applied:
        flash('已经投递过了','warning')
    else:
        resume = Resume(
            job_id = job.id,
            user_id=current_user.id
        )
        db.session.add(resume)
        db.session.commit()
        flash('投递成功','success')
    return redirect(url_for('job.job_information',job_id=job_id))



@job.route('/<int:company_id>/jobs')
def job_company_admin(company_id):
    company = User.query.get_or_404(company_id)
    return render_template('company/company_job_admin.html',jobs=company.jobs)


@job.route('/<int:job_id>/delete')
def job_delete(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash('职位已经删除','success')
    return redirect(url_for('company.job_company_admin',company_id=current_user.id))
