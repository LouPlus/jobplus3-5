"""
forms.py
存放表单相关代码
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db,User,Job
from flask_login import current_user

class UserRegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        user.role = 10
        db.session.add(user)
        db.session.commit()
        return user
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username has been existed')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email has been existed')




class UserEditForm(FlaskForm):
    username = StringField('用户名')
    email = StringField('邮箱')
    password = PasswordField('密码')
    repeat_password = PasswordField('重复密码')
    submit = SubmitField('保存')

    def edit_user(self,user):
        user.username = self.username.data
        user.email = self.email.data
        
        if self.password.data:
            user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user
       


class CompanyRegisterForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    companyname = StringField('公司名称', validators=[Required(), Length(8, 256)])
    logo = StringField('logo address',validators=[Required(),Length(1,256)])
    website = StringField('website',validators=[Required(),Length(8,256)])
    address = StringField('address',validators=[Required(),Length(8,256)])
    intro = StringField('intro',validators=[Required(),Length(8,256)])
    desc = StringField('description',validators=[Required(),Length(8,256)])
    
    submit = SubmitField('提交')

    def create_company(self):
        company = User()
        company.companyname = self.companyname.data
        company.email = self.email.data
        company.password = self.password.data
        company.role = 20
        company.website = self.website.data
        company.address = self.address.data
        company.intro = self.intro.data
        company.desc = self.desc.data
        company.logo = self.logo.data
        db.session.add(company)
        db.session.commit()
        return company
    def validate_companyname(self,field):
        if User.query.filter_by(companyname=field.data).first():
            raise ValidationError('companyname has been existed')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email has been existed')




class CompanyEditForm(FlaskForm):
    email = StringField('邮箱')
    password = PasswordField('密码')
    repeat_password = PasswordField('重复密码')
    companyname = StringField('公司名称')
    logo = StringField('logo address')
    website = StringField('website')
    address = StringField('address')
    intro = StringField('intro')
    desc = StringField('description')
    
    submit = SubmitField('保存')

    def edit_company(self,user):
        user.companyname = self.companyname.data
        if self.password.data:
            user.password = self.password.data
        user.email = self.email.data
        user.website = self.website.data
        user.address = self.address.data
        user.intro = self.intro.data
        user.desc = self.desc.data
        user.logo = self.logo.data
        db.session.add(user)
        db.session.commit()
        return user

class JobRegisterForm(FlaskForm):
    jobname = StringField('职位名称',validators=[Required(),Length(3,24)])
    salary = StringField('薪水',validators=[Required(),Length(1,20)])
    exprequirement = StringField('经验要求')
    edurequirement = StringField('受教育程度')
    address = StringField('地址')
    desc = StringField('简介')
    requirement = StringField('其他要求')
    submit = SubmitField('提交')
    def create_job(self):
        job = Job()
        job.jobname = self.jobname.data
        job.salary = self.salary.data
        job.exprequirement = self.exprequirement.data
        job.edurequirement = self.edurequirement.data
        job.address = self.address.data
        job.desc = self.desc.data
        job.requirement = self.requirement.data
        db.session.add(job)
        db.session.commit()
        return job

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码')#validators=[Required(),Length(0,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email has not been registered!')
    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('password error!')
