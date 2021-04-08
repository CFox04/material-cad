from django.contrib.auth.models import Group
from django.db.models import Model
from rest_framework import permissions
from police.models import Officer


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def is_in_one_group(user, groups):
    for group in groups:
        if is_in_group(user, group) or group == '__all__' or user.is_staff:
            return True
    return False


class IsSuperUser(permissions.BasePermission):
    """
    Allows super user to read and write
    """

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow superusers
        if request.user.is_superuser:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user


class HasGroupPermission(permissions.BasePermission):
    """
    Enables certain REST methods to require certain groups. This is set via the 'required_groups' mapping in the view. Requires user to be authenticated. Can also specify __all__ for all groups or __owner__ for owners of the object. 
    """

    def has_object_permission(self, request, view, obj):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, "required_groups", {})

        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])

        if not request.user.is_authenticated:
            return False

        # Allow superusers
        if request.user.is_superuser:
            return True
        print(request.method)
        return is_in_one_group(request.user, required_groups) or ("__owner__" in required_groups and obj.user == request.user)


class ModifyIfOwner(permissions.BasePermission):
    """
    Allows user to modify (PUT, DELETE) object if they are the owner
    """

    def has_object_permission(self, request, view, obj):
        if not request.method in ['PUT', 'DELETE']:
            return True

        if not request.user.is_authenticated:
            return False

        # Allow superusers
        if request.user.is_superuser:
            return True
        print(obj.user, request.user)

        return obj.user and obj.user == request.user


class IsPolice(permissions.BasePermission):
    """
    Only allow police officers to write and read with exception to admins and superusers
    """

    def has_object_permission(self, request, view, obj):
        # Allow superusers
        if request.user.is_superuser:
            return True

        return Officer.objects.get(user=obj.user)


class IsPoliceOrOwner(permissions.BasePermission):
    """
    Only allow police officers and owners to write and read with exception to admins
    """

    def has_object_permission(self, request, view, obj):
        # Allow superusers
        if request.user.is_superuser:
            return True

        return Officer.objects.filter(user=obj.user).len() > 0 or obj.user == request.user
