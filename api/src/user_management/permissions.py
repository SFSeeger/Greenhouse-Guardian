from rest_framework import permissions


class IsDevice(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.device)


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return not bool(request.device)
