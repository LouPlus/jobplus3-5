"""
user.py
求职者路由文件
"""

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/')
def index():
    return 'user'
