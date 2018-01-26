"""
app.py
Flask APP配置 、创建相关代码
"""

from flask import Flask
from jobplus.config import configs
from jobplus.models import db
from flask_login import LoginManager
from flask_migrate import Migrate  #管理数据库
from jobplus.models import User,Job
def create_app(config):
    """App 工厂"""

    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    login_manager.login_view = 'front.login'
def register_blueprints(app):
    """Blueprint 注册函数"""

    from .handlers import front, admin, user, job, company
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(job)
    app.register_blueprint(company)
