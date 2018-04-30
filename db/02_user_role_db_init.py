# coding=utf-8
import hashlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.roleUser import db, Users,  Roles
from flask_security import SQLAlchemyUserDatastore, Security
from init import app
from model.devicesView import Devices
from model.rentLogView import Rentlog

# Setup Flask-Security
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建用户等几张比较特殊的表，用户角色这块有特殊的方法可以使用
user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
security = Security(app, user_datastore)
db.create_all()

admin = user_datastore.create_user(name='admin',email='admin@4paradigm.com', password=hashlib.sha256("admin").hexdigest())
user = user_datastore.create_user(name='user',email='user@4paradigm.com', password=hashlib.sha256("user").hexdigest())
# 生成普通用户角色和admin用户角色
common_role = user_datastore.create_role(name='User', description='Common user role')
admin_role = user_datastore.create_role(name='Admin', description='Admin user role')
# 为admin添加Admin角色
user_datastore.add_role_to_user(admin, admin_role)
user_datastore.add_role_to_user(user, common_role)
db.session.commit()
