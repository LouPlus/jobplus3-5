"""
front.py
首页路由文件
"""

from flask import Blueprint

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return 'front'
