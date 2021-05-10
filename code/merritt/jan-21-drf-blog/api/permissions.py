from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.method in permissions.SAFE_METHODS else False
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # return False

class IsPete(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.username == "pete"