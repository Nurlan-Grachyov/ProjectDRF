from rest_framework.permissions import BasePermission


class OwnerOrStaffOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user ==  obj.owner:
            return True

        return False