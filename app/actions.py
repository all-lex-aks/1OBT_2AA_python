from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow
from m3_ext.ui import all_components as ext

class PermissionEditWindow(BaseEditWindow):
    def _init_components(self):
        super(PermissionEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')
        
        self.field__content_type = ext.ExtDictSelectField(
            label=u'content_type',
            name='content_type',
            pack=ContentTypePack,
            allow_blank=False,
            anchor='100%',
            value_field='id', 
            display_field='model')
        
        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')
    
    def _do_layout(self):
        super(PermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionEditWindow, self).set_params(params)
        self.height = 'auto'


class UserPack(ObjectPack):
    model = User
    #'logentry', 'id', 'password', 'last_login', 'is_superuser', 'username', 
    #'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 
    #'groups', 'user_permissions'

    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group
    #'user', 'id', 'name', 'permissions'
    
    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True

    columns = [
         {
            'data_index': 'user',
            'header': u'user',
            'width': 1,
        },
        {
            'data_index': 'id',
            'header': u'id',
            'width': 1,
        },
        {
            'data_index': 'name',
            'header': u'name',
            'width': 1,
        },
        {
            'data_index': 'permissions',
            'header': u'permissions',
            'width': 1,
        },

    ]

class PermissionPack(ObjectPack):
    model = Permission
    #'group', 'user', 'id', 'name', 'content_type', 'codename'

    add_window = edit_window = PermissionEditWindow

    add_to_menu = True

    # columns = [
    #      {
    #         'data_index': 'group',
    #         'header': u'group',
    #         'width': 1,
    #     },
    #     {
    #         'data_index': 'user',
    #         'header': u'user',
    #         'width': 1,
    #     },
    #     {
    #         'data_index': 'id',
    #         'header': u'id',
    #         'width': 1,
    #     },
    #     {
    #         'data_index': 'name',
    #         'header': u'name',
    #         'width': 1,
    #     },
    #     {
    #         'data_index': 'content_type',
    #         'header': u'content_type',
    #         'width': 1,
    #     },
    #      {
    #         'data_index': 'codename',
    #         'header': u'codename',
    #         'width': 1,
    #     },

    # ]


class ContentTypePack(ObjectPack):
    model = ContentType
    #'logentry', 'permission', 'id', 'app_label', 'model'
    
    #add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True

    columns = [
         {
            'data_index': 'logentry',
            'header': u'logentry',
            'width': 1,
        },
        {
            'data_index': 'permission',
            'header': u'permission',
            'width': 1,
        },
        {
            'data_index': 'id',
            'header': u'id',
            'width': 1,
        },
        {
            'data_index': 'app_label',
            'header': u'app_label',
            'width': 1,
        },
        {
            'data_index': 'model',
            'header': u'model',
            'width': 1,
        },
         
    ]