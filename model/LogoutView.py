# coding=utf-8
import hashlib

from django.shortcuts import redirect
from flask import request, flash, url_for
from flask.ext.login import login_user, logout_user

from flask_admin import BaseView, expose

from init import db


class LogoutView(BaseView):

    @expose('/',methods=('GET', 'POST'))
    def logout(self):
        logout_user()  # 登出用户
        return self.render("index.html")
class ModifyPassword(BaseView):
    @expose('/',methods=('GET', 'POST'))
    def modifyPassword(self):
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
                print "password is ------"
                print user.password
                user.password = hashlib.sha256(request.form.get('newPassword02')).hexdigest()
                db.session.commit()
                print user.password
                login_user(user, remember=True)
                flash(u'密码修改成功')
                next_url = request.args.get('next')
                return redirect(next_url or url_for('index'))
        return self.render("modifyPassword.html")







