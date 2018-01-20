"""
company.py
企业路由文件
"""

from flask import Blueprint

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/')
def index():
    return 'company'