from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow
from m3_ext.ui import all_components as ext
from datetime import date

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
            name='content_type_id',
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


class UserEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            input_type='password',
            allow_blank=False,
            anchor='100%')
        
        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%',
            format='d.m.Y')
        
        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            checked=False,
            anchor='100%')
        
        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')
        
        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')
        
        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')
        
        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%')
        
        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            checked=False,
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'active',
            name='is_active',
            checked=True,
            anchor='100%')
        
        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            anchor='100%',
            format='d.m.Y',
            value=date.today())
    
    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'

class UserPack(ObjectPack):
    model = User
    
    add_window = edit_window = UserEditWindow
    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group
        
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True

    
class PermissionPack(ObjectPack):
    model = Permission
    
    add_window = edit_window = PermissionEditWindow
    add_to_menu = True


class ContentTypePack(ObjectPack):
    model = ContentType
        
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True

   