# coding=utf-8
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

from init import *
from flask_security import RoleMixin, UserMixin, roles_required

# Create database connection object
from model.MyBaseModelView import MyBaseModelView

db = SQLAlchemy(app)


class Roles_Users(db.Model):

    __tablename__ = 'roles_users'
    # def __init__(self, role_id, user_id):
    #     self.role_id = role_id
    #     self.user_id = user_id

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    user = db.relationship('Users', backref=db.backref('roles_users', lazy='select'))
    role = db.relationship('Roles', backref=db.backref('roles_users', lazy='select'))

    def __repr__(self):
        return u"{user_id}_{role_id}".format(user_id=self.user_id, role_id=self.role_id)


class MyRoles_UsersView(MyBaseModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    column_labels = dict(user_id=u'用户', role_id=u'角色')
    # form_columns = ('id','user_id','role_id')






    form_ajax_refs = {
        'user':{
            'fields':['name','phone'],
            'page_size':10
        }
    }
    # Override displayed fields
    # column_list = ('id', 'user_id','role_id')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyRoles_UsersView, self).__init__(Roles_Users, session, **kwargs)



class Roles(db.Model, RoleMixin):
    __tablename = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return u"{id}_{name}".format(id=self.id, name=self.name)


class MyRoleView(MyBaseModelView):
    # 登陆后的用户可以看见该菜单
    def is_accessible(self):
        return current_user.is_authenticated
    column_labels = dict(name=u'角色名', description=u'角色描述')



    # Override displayed fields


    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyRoleView, self).__init__(Roles, session, **kwargs)


class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Roles', secondary=Roles_Users.__tablename__,
                            backref=db.backref('users', lazy='dynamic'))

    @staticmethod
    def getUserRolesByName(name):
        print(u"getUserRolesByName method====,name is ", name)
        userRoles = []
        userOfName = Users.query.filter_by(name=name).first()
        if userOfName:
            user_id = Users.query.filter_by(name=name).first().id
            rus = Roles_Users.query.filter_by(user_id=user_id).all()
            print(rus)
            for ru in rus:
                userRoles.append(Roles.query.filter_by(id=ru.role_id).first().name)
                print ru.role_id
        print userRoles
        return userRoles

    def __repr__(self):
        print self.name
        return u"{id}_{name}".format(id=self.id, name=self.name)


class MyUserView(MyBaseModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    column_labels = dict(name=u'用户', email=u'邮箱', phone=u'联系电话', password=u'密码', active=u'是否激活', confirmed_at=u'激活时间')



    # Override displayed fields
    column_list = ('id', 'name','phone','active','phone')
    column_filters =  ['name']

    # excluded_columns = ('password','email',u'密码',u'邮箱')


    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(MyUserView, self).__init__(Users, session, **kwargs)
