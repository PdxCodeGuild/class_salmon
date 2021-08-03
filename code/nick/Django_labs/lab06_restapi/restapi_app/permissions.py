from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.method in permissions.SAFE_METHODS else False

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.username in ['nick']

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.last_name == request.user#assigned last name here to match the user last name for editing purposes, corruptable