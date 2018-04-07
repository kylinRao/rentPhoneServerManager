# coding=utf-8
import hashlib
import json

from datetime import datetime, time
from flask import  request, g
from flask.ext.security import SQLAlchemyUserDatastore, Security
from flask.ext.sqlalchemy import SQLAlchemy

from logControl import logControl
from init import app,db
from model import staticMem
from model.devicesView import Devices
from model.rentLogView import Rentlog
from model.roleUser import Users, Roles


@app.route('/rentPhoneReport', methods=['POST', 'GET'])
def rentPhoneReport():


    user_datastore = SQLAlchemyUserDatastore(db, Users, Roles)
# rent method
    if request.form.get("method", 'getNoMethod') == "rent":
        phone, name, deviceId, rentPhoneType, battaryLevel, gameboxVersion, hiappVersion, hmsVersion, isRoot = request.form.get(
            "phone", 'getNoPhone'), \
                                                                                                               request.form.get(
                                                                                                                   "name",
                                                                                                                   'getNoName'), \
                                                                                                               request.form.get(
                                                                                                                   "deviceId",
                                                                                                                   'getNodeviceId'), \
                                                                                                               request.form.get(
                                                                                                                   "phoneType",
                                                                                                                   'getNophoneType'), \
                                                                                                               request.form.get(
                                                                                                                   "battaryLevel",
                                                                                                                   'getNobattaryLevel'), \
                                                                                                               request.form.get(
                                                                                                                   "gameboxVersion",
                                                                                                                   'getNogameboxVersion'), \
                                                                                                               request.form.get(
                                                                                                                   "hiappVersion",
                                                                                                                   'getNohiappVersion'), \
                                                                                                               request.form.get(
                                                                                                                   "hmsVersion",
                                                                                                                   'getNohmsVersion'), \
                                                                                                               request.form.get(
                                                                                                                   "isRoot",
                                                                                                                   'false');
        if 'true' in  isRoot.lower():
            isRoot = True
        else:
            isRoot = False
        # with db.session.no_autoflush:
# 创建新的手机出借纪录
        rentLog = Rentlog()
        rentLog.name = name
        rentLog.phone = phone

        rentLog.rentTime = datetime.now().replace(microsecond=0)

        rentLog.deviceId = deviceId
        rentLog.rentPhoneType = rentPhoneType
        rentLog.status = False
        rentLog.gameboxVersion = gameboxVersion
        rentLog.hiappVersion = hiappVersion
        rentLog.hmsVersion = hmsVersion
        db.session.add(rentLog)
#
        device = Devices.query.filter_by(deviceId = deviceId).first()
        if not device:
            device = Devices()
            device.renterName = name
            device.deviceId = deviceId
            device.rentPhoneType = rentPhoneType
            device.status = False
            device.gameboxVersion = gameboxVersion
            device.hiappVersion = hiappVersion
            device.hmsVersion = hmsVersion
            device.isRoot = isRoot
            db.session.merge(device)
        else:
            device.renterName = name
            device.deviceId = deviceId
            device.rentPhoneType = rentPhoneType
            device.status = False
            device.gameboxVersion = gameboxVersion
            device.hiappVersion = hiappVersion
            device.hmsVersion = hmsVersion
            device.isRoot = isRoot





# 创建新用户
        if not Users.query.filter_by(name = name).first():
            print(u"开始创建新用户")

            newUser = user_datastore.create_user(name=name,active=True, phone = phone,password=hashlib.sha256("123456").hexdigest())
            commonRole = user_datastore.find_role(staticMem.COMMON_GROUP)
            # user_datastore.add_role_to_user(newUser, commonRole)
        try:
            db.session.commit()
        except:
            data = {"responseCode":staticMem.RENT_DB_ERROR,"Msg":"db error"}
            logControl.getLogger().debug("some db error occored")

            return json.dumps(data)


# return method

    if request.form.get("method", 'getNoMethod') == "return":
        phone, name, deviceId, rentPhoneType, battaryLevel, gameboxVersion, hiappVersion, hmsVersion = request.form.get(
            "phone", 'getNoPhone'), request.form.get("name", 'getNoName'), \
                                                                                                       request.form.get(
                                                                                                           "deviceId",
                                                                                                           'getNodeviceId'), \
                                                                                                       request.form.get(
                                                                                                           "phoneType",
                                                                                                           'getNophoneType'), \
                                                                                                       request.form.get(
                                                                                                           "battaryLevel",
                                                                                                           'getNobattaryLevel'), \
                                                                                                       request.form.get(
                                                                                                           "gameboxVersion",
                                                                                                           'getNogameboxVersion'), \
                                                                                                       request.form.get(
                                                                                                           "hiappVersion",
                                                                                                           'getNohiappVersion'), \
                                                                                                       request.form.get(
                                                                                                           "hmsVersion",
                                                                                                           'getNohmsVersion');
        # with db.session.no_autoflush:
            # 更新数据库

        # 创建新的手机出借纪录

        rentlogs = Rentlog.query.filter(Rentlog.name == name).filter( Rentlog.status == False).all()
        for rentLog in rentlogs:
            logControl.getLogger().debug("rentlogs:{rentlogs}".format(
                    rentlogs=rentLog))
            rentLog.returnName = name
            rentLog.returnPhone = phone

            rentLog.returnTime = datetime.now().replace(microsecond=0)
            # rentlog.update({'returnTime':datetime.now().replace(microsecond=0)})


            rentLog.deviceId = deviceId
            rentLog.rentPhoneType = rentPhoneType

            rentLog.gameboxVersion = gameboxVersion
            rentLog.hiappVersion = hiappVersion
            rentLog.hmsVersion = hmsVersion
            rentLog.status = True

            logControl.getLogger().debug("returnName={returnName},returnPhone={returnPhone},returnTime={returnTime}".format(
                    returnName=rentLog.returnName,returnPhone=rentLog.returnPhone,returnTime=rentLog.returnTime))



        # 更新设备信息
        device = Devices.query.filter_by(deviceId = deviceId).first()
        if not device:
            device = Devices()
            device.renterName = ""
            device.deviceId = deviceId
            device.rentPhoneType = rentPhoneType
            device.status = True
            device.gameboxVersion = gameboxVersion
            device.hiappVersion = hiappVersion
            device.hmsVersion = hmsVersion
            db.session.add(device)
        else:
            device.renterName = ""
            device.deviceId = deviceId
            device.rentPhoneType = rentPhoneType
            device.status = True
            device.gameboxVersion = gameboxVersion
            device.hiappVersion = hiappVersion
            device.hmsVersion = hmsVersion

        try:
            db.session.commit()
        except:
            data = {"responseCode":staticMem.RENT_DB_ERROR,"Msg":"db error"}
            return json.dumps(data)
    return json.dumps({'responseCode':0})
