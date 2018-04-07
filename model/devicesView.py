# coding=utf-8
from flask import g, request
from flask.ext.login import current_user
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from init import *
from wtforms.fields import SelectField

from flask_admin.contrib.sqla import ModelView
from init import db
from model import staticMem


# 创建对象的基类:
from model.MyBaseModelView import MyBaseModelView

Base = declarative_base()
class Devices(db.Model,Base):
    __tablename__ = 'devices'
    deviceName = db.Column(db.String(80), unique=False)
    status = db.Column(db.Boolean())
    renterName =  db.Column(db.String(80), unique=False)
    rentPhoneType = db.Column(db.String(80), unique=False)

    deviceId = db.Column(db.String(80),primary_key=True, unique=False)

    gameboxVersion =  db.Column(db.String(80), unique=False)
    hiappVersion = db.Column(db.String(80), unique=False)
    hmsVersion = db.Column(db.String(80), unique=False)
    owner = db.Column(db.String(80), unique=False)
    isRoot = db.Column(db.Boolean())

    # user = db.relationship('Users', backref=db.backref('devices', lazy='select'))


    # column_list = ('name', 'phone')
    # def __init__(self, name, phone):
    #     self.name = name
    #     self.phone = phone


    def __repr__(self):
        return '<devices %r>' % self.name
class DevicesView(MyBaseModelView):
    # column_formatters = dict(status=lambda v, c, m, p: u"在库" if m.status == 1 else u"已借出"  )
    column_labels = dict(rentPhoneType=u'手机型号', status=u'是否在库', renterName=u'手机在谁手上', deviceId=u'设备标识',  owner=u'手机属主', isRoot=u'是否root',deviceName = u"手机中文名")
    column_editable_list = ['owner','deviceName']
    # column_searchable_list = ['owner','status']
    column_filters =  ['owner','status']

    def is_accessible(self):
        print("is_accessible method ====")
        print("app.app_context().g.userRoles is ",request.form.get('name'))

        if hasattr(app.app_context().g,'userRoles'):
            if staticMem.MANAGER_GROUP in app.app_context().g.userRoles:
                print("is_accessible method userRoles====")
                can_create = False
                can_delete = True
                can_edit = True
        return True

    # # Disable model creation
    can_create = False
    can_delete = False
    can_edit = False


    # Override displayed fields
    # column_list = ('login', 'email')

    # form_overrides = dict(status=SelectField)
    # form_args = dict(
    #     # Pass the choices to the `SelectField`
    #     status=dict(
    #         choices=[(0, 1), (1, '出借中')]
    #     ))

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(DevicesView, self).__init__(Devices, session, **kwargs)

# Setup Flask-Security
engine = create_engine('sqlite:///../db/phone.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)