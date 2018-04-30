# coding=utf-8
import ast

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
import sys
from flask_babelex import Babel
from jinja2 import environment


def str2dic(value,key):
    return ast.literal_eval(value)[key]



reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)

env = app.jinja_env
env.filters['str2dic'] = str2dic


app.secret_key = 'Sqsdsffqrhgh***'
DATABASE = '.\db\house.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/house.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Huawei123@192.168.1.112:3306/adminserver?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True

db = SQLAlchemy(app)

babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"  # 定义登录的 视图
login_manager.login_message = u'请登录以访问此页面'  # 定义需要登录访问页面的提示消息
