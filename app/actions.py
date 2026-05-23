from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class UserPack(ObjectPack):
    model = User
    #'logentry', 'id', 'password', 'last_login', 'is_superuser', 'username', 
    #'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 
    #'groups', 'user_permissions'

    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group
    #'user', 'id', 'name', 'permissions'

    add_to_menu = True


class PermissionPack(ObjectPack):
    model = Permission
    #'group', 'user', 'id', 'name', 'content_type', 'codename'

    add_to_menu = True

class ContentTypePack(ObjectPack):
    model = ContentType
    #'logentry', 'permission', 'id', 'app_label', 'model'
    
    add_to_menu = True