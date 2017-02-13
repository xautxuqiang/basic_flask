#coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
	name = StringField(u"你叫什么名字?", validators=[Required(),])
	submit = SubmitField(u"确认")
