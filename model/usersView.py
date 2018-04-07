# coding=utf-8
from flask.ext.login import UserMixin, current_user
from flask.ext.security import roles_required
from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from init import db

class Users(db.Model, UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key=True)

  name = db.Column(db.String(10), unique=True)
  password = db.Column(db.String(16))
  groupid = db.Column(db.Integer)


  def __init__(self, name, password):
    self.name = name
    self.password = password
  def __repr__(self):
    return '<User %r|%r>' % (self.name,self.password)



class UsersView(ModelView):
    # def is_accessible(self):
    #     return False
    # Disable model creation

    print current_user
    can_create = False
    can_delete = False
    can_edit = False



    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(UsersView, self).__init__(Users, session, **kwargs)

class userstable(db.Model):
    can_create = False
    can_delete = False
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))

    column_list = ('name', 'phone')
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def __repr__(self):
        return '<rentLog %r>' % self.name
