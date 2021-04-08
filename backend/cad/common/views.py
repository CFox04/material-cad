from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from user.permissions import HasGroupPermission, is_in_one_group, is_in_group


class GroupPermsModelViewSet(viewsets.ModelViewSet):
    permission_classes = [HasGroupPermission]

    def get_queryset(self):
        # Get required groups for GET requests
        if 'GET' in self.required_groups and self.request.user.is_authenticated:
            required_groups = self.required_groups['GET']

            reqUser = self.request.user
            # If in one group, one group return all objects
            if is_in_one_group(reqUser, required_groups):
                return self.model.objects.all().order_by('-id')

            # Otherwise, return all character objects created by the user
            if "__owner__" in required_groups:
                return self.model.objects.filter(user=reqUser.id).order_by('-id')

            # Last case, return none
            raise PermissionDenied()
        elif not self.request.user.is_authenticated:
            raise NotAuthenticated()
        else:
            return self.model.objects.none()
