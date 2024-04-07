from rest_framework import permissions


class IsDevice(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.device)
        return bool(request.device)
