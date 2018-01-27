"""
job.py
职位路由文件
"""

from flask import Blueprint,render_template
from jobplus.models import Job
job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    jobdata = Job.query.all()
    return render_template('job.html',jobs=jobdata)

