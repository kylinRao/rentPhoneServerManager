# coding=utf-8
import sqlite3

from flask.ext.login import current_user


from init import db,app,DATABASE
from flask_sqlalchemy import SQLAlchemy
from flask import g, request
from flask.ext.admin import Admin, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView

from api.common import login,index,login_success,logout,page_not_found
from api.rentPhoneReport import rentPhoneReport
from model.HouseView import  HouseEveryDayPriceView, HouseBaseInfoView, HouseReduceDayView

from model.LogoutView import  LogoutView, ModifyPassword
from model.tools import tools
from model.roleUser import MyRoleView, MyUserView, MyRoles_UsersView




def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    if not current_user.is_anonymous:
        name = current_user.name
        tools.reloadPermissonByUserName(name)
    g.db = connect_db()
    g.user = current_user
    print("====before request====")


@app.teardown_request
def teardown_request(exception):
    tools.resetRights()
    print current_user
    if hasattr(g, 'db'):
        g.db.close()
        print("====after request====")
from model.devicesView import DevicesView
from model.rentLogView import RentLogView
from model.FilesView import FilesView






if __name__ == '__main__':

    admin = Admin(app,index_view=AdminIndexView(
        name='首页',
        template='index.html',
        url='/admin',endpoint='admin'
    ))

    admin.add_view(RentLogView(db.session, name=u'手机借还记录', endpoint='RentLogView',category=u"手机借用登记"))
    admin.add_view(DevicesView(db.session, name=u'手机状态', endpoint='DevicesView',category=u"手机借用登记"))

    admin.add_view(MyRoleView(db.session, name=u'角色管理', endpoint='RoleView',category=u"用户与角色"))
    admin.add_view(MyUserView(db.session, name=u'用户管理', endpoint='UserView',category=u"用户与角色"))
    admin.add_view(MyRoles_UsersView(db.session, name=u'角色分配', endpoint='Roles_UsersView',category=u"用户与角色"))

    admin.add_view(HouseEveryDayPriceView(db.session,name='房屋每日价格信息', endpoint='HouseEveryDayPriceView',category=u"链家房产"))
    admin.add_view(HouseBaseInfoView(db.session,name='房屋详细信息', endpoint='HouseBaseInfoView',category=u"链家房产"))
    admin.add_view(HouseReduceDayView(db.session,name='房价涨幅信息', endpoint='HouseReduceDayView',category=u"链家房产"))
    admin.add_view(FilesView(name='文件下载', endpoint='FilesView', category=u"相关文件"))
    admin.add_view(ModifyPassword(name='密码修改', endpoint='modifyPassword',category=u"与我相关"))
    admin.add_view(LogoutView(name='登出', endpoint='logout',category=u"与我相关"))


    app.run(host="0.0.0.0", port=9999, debug=False)


