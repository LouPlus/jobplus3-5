"""
app.py
Flask APP配置 、创建相关代码
"""

from flask import Flask
from jobplus.config import configs
from jobplus.models import db


def create_app(config):
    """App 工厂"""

    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Blueprint 注册函数"""

    from .handlers import front, admin, user, job, company
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(job)
    app.register_blueprint(company)
