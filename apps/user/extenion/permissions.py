from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class Permission(BasePermission):

    def has_permission(self, request: Request, view):

        if getattr(view, '_ignore_model_permissions', False):
            return True

        if request.user.is_anonymous:
            return False
        return True
