"""
models.py
存放数据模型相关代码
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Base(db.Model):
    """
    数据库基类，默认添加时间戳
    """

    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#通过建立辅助表，在user与job表建立多对多关系
user_job = db.Table('user_job',
                    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
                    db.Column('job_id',db.Integer,db.ForeignKey('job.id'))
                    )


class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_ADMIN = 30
    ROLE_COMPANY = 20
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=True)
    email = db.Column(db.String(64), unique=True, index=True,nullable=True)
    _password = db.Column('password', db.String(256), nullable=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    
    logo = db.Column(db.String(128),unique=True,index=True,nullable=True)
    companyname = db.Column(db.String(128),unique=True, index=True, nullable=True)
    website = db.Column(db.String(128),index=True, nullable=True)
    address = db.Column(db.String(32),index=True, nullable=True)
    intro = db.Column(db.String(512), index=True,nullable=True)
    desc = db.Column(db.String(1024))
    
    jobs = db.relationship('Job',secondary=user_job,backref='users') 
    is_disable = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_user(self):
        return self.role == self.ROLE_USER


class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    jobname = db.Column(db.String(32),index=True)
    salary = db.Column(db.String(32))
    exprequirement = db.Column(db.String(32))  # 经验要求
    edurequirement = db.Column(db.String(32))  # 学历要求
    address = db.Column(db.String(32))
    desc = db.Column(db.String(512))  # 职位描述
    requirement = db.Column(db.String(512))  # 职位要求
    status = db.Column(db.Boolean,default=1) #是否上线
    company_id = db.Column(db.Integer)
    def __repr__(self):
        return '<Job:{}>'.format(self.jobname)
    @property
    def current_user_is_applied(self):
        resume = Resume.query.filter_by(job_id=self.id,user_id=current_user.id).first()
        return (resume is not None)

class Resume(Base):
    __tablename = 'resume'

    STATUS_WAITING = 1
    STATUS_REJECT = 2
    STATUS_ACCEPT = 3

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='SET NULL'))   
    company_id = db.Column(db.Integer) 
    status = db.Column(db.SmallInteger, default=STATUS_WAITING)

    response = db.Column(db.String(256))












