#coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo, Regexp
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
	email = StringField(u"邮箱", validators=[Required(), Email(u"无效的邮箱地址"), Length(1,64)])
	password = PasswordField(u"密码", validators=[Required()])
	remember_me = BooleanField(u"记住我")
	submit = SubmitField(u"登录")


class RegistrationForm(FlaskForm):
	email = StringField(u"邮箱", validators=[Required(), Email(u"无效的邮箱地址"), Length(1,64)])
	username = StringField(u"用户名",validators=[Required(),Length(1,64),Regexp("^[A-Za-z][A-Za-z0-9._]*$", 0, u"用户名必须以字母开头，其后只能包括字母，数字，点和下划线")])
	password = PasswordField(u"密码",validators=[Required()])
	password2 = PasswordField(u"确认密码", validators=[Required(),EqualTo('password', message=u"两次密码必须一致")])
	submit = SubmitField(u'注册')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError(u"邮箱已被注册")

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError(u"用户名已被使用")

