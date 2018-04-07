# coding=utf-8
import hashlib

import sqlite3
from flask import Flask, redirect, url_for, request, flash, render_template, g
from flask.ext.security import roles_required
from flask_login import  login_user, login_required, logout_user
from init import login_manager,app, db, DATABASE
from model import staticMem
from model.devicesView import Devices,DevicesView
from model.roleUser import   Roles_Users
from model.tools import tools


@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    from model.roleUser import Users
    user = Users.query.filter_by(id=id).first()
    return user


# 添加登录视图，如果是GET方法，返回一个简单的表单

@app.route('/login/', methods=['GET', 'POST'])
def login():
    from model.roleUser import Users
    if request.method == 'POST':
        name = request.form.get('name')
        print name
        user = Users.query.filter_by(name=name).first()
        print user

        if not user:
            flash(u'该用户不存在')
        elif hashlib.sha256(request.form.get('password')).hexdigest()  != user.password:
            flash(u'密码错误')
        else:
            login_user(user, remember=True)

            userRoles = Users.getUserRolesByName(name)
            print("userRoles:",userRoles)
            g.userRoles = userRoles
            print("g.userRoles is",g.userRoles)

            next_url = request.args.get('next')
            return redirect(next_url or url_for('index'))
    return redirect('/admin/')  # 如果密码是 123 就会跳转到视图函数 index 上


@app.route('/')
# @login_required
def index():
    # return render_template('index.html')
    return redirect('/admin')


@app.route('/succees/')
@login_required
def login_success():
    return render_template('base_notice.html')


@app.route('/logout/')
@login_required
def logout():
    logout_user()  # 登出用户
    return u'已经退出登录'
@app.route('/modifyPassword/', methods=['GET', 'POST'])
def modifyPassword():
    from model.roleUser import Users
    if request.method == 'POST':
        name = request.form.get('name')
        print name
        user = Users.query.filter_by(name=name).first()
        if not user:
            flash(u'该用户不存在')
        elif hashlib.sha256(request.form.get('password')).hexdigest()  != user.password:
            flash(u'密码错误')
        else:
            print("modifyPassword mehtod in common")
            print user.password
            user.password = hashlib.sha256(request.form.get('newPassword02')).hexdigest()
            db.session.commit()
            print user.password
            conn = sqlite3.connect(DATABASE)
            conn.cursor().execute(u"update users set password = '{password}' where name = '{name}'".format(password=user.password,name = name))
            conn.commit()
            conn.close()


            # login_user(user, remember=True)
            flash(u'密码修改成功')
            # next_url = request.args.get('next')
            # return redirect(next_url or url_for('index'))
    return redirect('/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


