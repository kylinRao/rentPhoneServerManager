from flask.ext.admin.contrib.sqla import ModelView


class MyBaseModelView(ModelView):
    can_create = False
    can_delete = False
    can_edit = False

    edit_modal = True
    create_modal = True

    can_export = True
    page_size = 40