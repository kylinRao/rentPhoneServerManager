# coding=utf-8
from flask import g
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.ext.declarative import declarative_base
from wtforms.fields import SelectField
from init import db



# 创建对象的基类:
from model.MyBaseModelView import MyBaseModelView

Base = declarative_base()
class RentLogView(MyBaseModelView):
    # column_formatters = dict(status=lambda v, c, m, p: u"在库" if m.status == 1 else u"已借出"  )
    column_labels = dict(rentPhoneType=u'手机型号', status=u'是否在库', name=u'谁借的', deviceId=u'设备标识',  phone=u'联系方式（借者）', returnName=u'谁还的',
                         returnPhone=u'联系方式（还者）', rentTime=u'借出时间', returnTime=u'归还时间')

    __tablename__ = 'rentlog'
    # Disable model creation
    can_create = False
    can_delete = False
    can_edit = False

    column_filters =  ['name','deviceId','status','returnName','rentPhoneType']


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
        super(RentLogView, self).__init__(Rentlog, session, **kwargs)

class Rentlog(db.Model,Base):
    can_create = False
    can_delete = False
    can_edit = False
    id = db.Column(db.Integer, primary_key=True,unique=True)
    rentPhoneType = db.Column(db.String(80), unique=False)
    name =  db.Column(db.String(80), unique=False)
    phone = db.Column(db.String(80), unique=False)
    deviceId = db.Column(db.String(80), unique=False)
    status = db.Column(db.BOOLEAN)
    returnName = db.Column(db.Integer, unique=False)
    returnPhone = db.Column(db.Integer, unique=False)
    rentTime = db.Column(db.DATETIME, unique=False)
    returnTime = db.Column(db.DATETIME, unique=False)
    gameboxVersion =  db.Column(db.String(80), unique=False)
    hiappVersion = db.Column(db.String(80), unique=False)
    hmsVersion = db.Column(db.String(80), unique=False)

    # column_list = ('name', 'phone')
    # def __init__(self, ):
    #     pass
    # def __init__(self, name, phone):
    #
    #     self.name = name
    #     self.phone = phone


    def __repr__(self):
        return '<rentLog %r>' % self.name