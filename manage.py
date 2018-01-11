"""
manage.py
项目入口文件
"""

# app = Flask(__name__)  　改为使用工厂函数创建gi
#  db = SQLAlchemy(app)   写入数据模型models.py


from jobplus.app import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()
