"""
forms.py
存放表单相关代码
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from jobplus.models import db,User,Company,Job


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
        db.session.add(user)
        db.session.commit()
        return user
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username has been existed')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email has been existed')

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
        company = Company()
        company.companyname = self.companyname.data
        company.email = self.email.data
        company.password = self.password.data
        db.session.add(company)
        db.session.commit()
        return company
    def validate_companyname(self,field):
        if Company.query.filter_by(companyname=field.data).first():
            raise ValidationError('companyname has been existed')

    def validate_email(self, field):
        if Company.query.filter_by(email=field.data).first():
            raise ValidationError('email has been existed')

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = StringField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('email has not been registered!')
    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('password error!')
