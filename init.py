# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
import sys
from flask_babelex import Babel

reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)


app.secret_key = 'Sqsdsffqrhgh***'
DATABASE = 'D:\projects\github\loginTest\db\phone.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/house.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True

db = SQLAlchemy(app)

babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"  # 定义登录的 视图
login_manager.login_message = u'请登录以访问此页面'  # 定义需要登录访问页面的提示消息
