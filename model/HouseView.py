#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/15 10:34
# @Author  : Aries
# @Site    : 
# @File    : HouseView.py
# @Software: PyCharm

from flask.ext.login import current_user
from init import *
from db.dbInit01 import conn
# Create database connection object
from model.MyBaseModelView import MyBaseModelView


db = SQLAlchemy(app)


class HouseEveryDayPrice(db.Model):
    __tablename__ = 'HouseEveryDayPrice'
    id = db.Column(db.Integer(), primary_key=True)
    houseCode = db.Column(db.Integer())
    date = db.Column(db.DATE)
    totalPrice = db.Column(db.FLOAT)
    unitPrice = db.Column(db.FLOAT)
    updateTime = db.Column(db.DATETIME)
class HouseEveryDayPriceView(MyBaseModelView):
    list_template = 'admin/HouseCustom_list.html'
    column_formatters = dict(houseCode=lambda v, c, m, p: {"houseCode":m.houseCode})
    column_filters =  ['houseCode']
    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(HouseEveryDayPriceView, self).__init__(HouseEveryDayPrice, session, **kwargs)
class HouseReduceDay(db.Model):
    __tablename__ = 'HouseReduceDay'

    id = db.Column(db.Integer(), primary_key=True)
    houseCode = db.Column(db.Integer())
    date = db.Column(db.DATE)
    reducePercent = db.Column(db.FLOAT)

class HouseReduceDayView(MyBaseModelView):
    list_template = 'admin/HouseCustom_list.html'
    column_formatters = dict(houseCode=lambda v, c, m, p: {"houseCode":m.houseCode})
    column_filters =  ['houseCode']
    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(HouseReduceDayView, self).__init__(HouseReduceDay, session, **kwargs)
class HouseBaseInfo(db.Model):
    __tablename__ = 'HouseBaseInfo'
    id = db.Column(db.Integer(), primary_key=True)
    houseCode = db.Column(db.Integer())
    houseInfo = db.Column(db.String)
    publishday = db.Column(db.Integer)
    url = db.Column(db.TEXT)
    visited = db.Column(db.Integer)
    region = db.Column(db.TEXT)
    area = db.Column(db.TEXT)
    attention = db.Column(db.Integer)
    sourceId = db.Column(db.Integer)

class HouseBaseInfoView(MyBaseModelView):
    list_template = 'admin/HouseCustom_list.html'
    column_formatters = dict(houseCode=lambda v, c, m, p: {"houseCode":m.houseCode})
    column_filters =  ['houseCode','area',]
    column_exclude_list = ['url','houseInfo' ]


    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(HouseBaseInfoView, self).__init__(HouseBaseInfo, session, **kwargs)

