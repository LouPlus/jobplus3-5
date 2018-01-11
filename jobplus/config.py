"""
config.py
存放配置
"""

class BaseConfig(object):
    """
    配置基类
    """
    pass

class DevelopmentConfig(BaseConfig):
    """
    开发环境配置
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
    """
    生产环境配置
    """
    pass

class TestingConfig(BaseConfig):
    """
    测试环境配置d
    """
    pass

configs = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}