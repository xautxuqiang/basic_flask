#coding:utf-8
from datetime import datetime
from flask import render_template, redirect, url_for, session, flash

from . import main
from ..models import User, Role
from .forms import NameForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
