#coding=utf-8
from flask import render_template, flash, request, abort, redirect, url_for
from .forms import LoginForm, RegistrationForm
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			flash(u"登录成功")
			#原地址保存在查询字符串的next参数里			
			return redirect(request.args.get('next') or url_for('main.index'))
		flash(u"无效的邮箱或密码")
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash(u"你已经成功注销")
	return redirect(url_for('main.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data, username=form.username.data, password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash(u"你现在可以登陆了")
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)

