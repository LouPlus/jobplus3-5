"""
job.py
职位路由文件
"""

from flask import Blueprint

job = Blueprint('job', __name__, url_prefix='/job')

@job.route('/')
def index():
    return 'job'