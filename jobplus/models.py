"""
models.py
存放数据模型相关代码
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
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
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True,nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    company = db.relationship('Company', uselist=False)

    jobs = db.relationship('Job',secondary=user_job,backref='users')

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


class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(64), unique=True, index=True, nullable=False)
    logo = db.Column(db.String(128), unique=True)
    website = db.Column(db.String(128), unique=True, index=True, nullable=False)
    address = db.Column(db.String(32), index=True, nullable=False)
    # 一句话介绍
    intro = db.Column(db.String(512), index=True, nullable=False)
    #公司描述
    desc = db.Column(db.String(1024))
    jobs = db.relationship('Job')

    def __repr__(self):
        return '<Company:{}>'.format(self.companyname)


class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    jobname = db.Column(db.String(32), unique=True, index=True)
    salary = db.Column(db.String(32))
    exprequirement = db.Column(db.String(32))  # 经验要求
    edurequirement = db.Column(db.String(32))  # 学历要求
    address = db.Column(db.String(32))
    desc = db.Column(db.String(512))  # 职位描述
    requirement = db.Column(db.String(512))  # 职位要求
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    status =db.Column(db.Boolean,default=1) #是否上线

    def __repr__(self):
        return '<Job:{}>'.format(self.jobname)
