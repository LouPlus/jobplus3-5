"""
job.py
职位路由文件
"""

from flask import Blueprint,render_template,flash,redirect,url_for,request,current_app
from jobplus.models import User,Job
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


#@job.route('/admin')
#def job_admin():
#    return render_template()

#@job.route('/<int:job_id>/apply')
#def job_apply(job_id):
#    job



#@job.route('/<int:job_id>/edit')
#def job_edit(job_id):


#@job.route('/<int:job_id>/delete')
#def job_delete(job_id):



#@job.route('/<int:job_id>/disable')
