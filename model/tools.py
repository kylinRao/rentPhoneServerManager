from model.devicesView import DevicesView
from model.rentLogView import RentLogView
from model.roleUser import Users, MyRoleView, MyUserView, MyRoles_UsersView


class tools:
    objs = [RentLogView,DevicesView,MyRoleView,MyUserView,MyRoles_UsersView]
    @staticmethod
    def reloadPermissonByUserName(name):
        if "Admin" in Users.getUserRolesByName(name):
            for obj in tools.objs:
                obj.can_create = True
                obj.can_delete = True
                obj.can_edit = True
    @staticmethod
    def resetRights():
        for obj in tools.objs:
            obj.can_create = False
            obj.can_delete = False
            obj.can_edit = False