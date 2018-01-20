"""
 admin.py
 管理者路由文件
"""

from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return 'admin'