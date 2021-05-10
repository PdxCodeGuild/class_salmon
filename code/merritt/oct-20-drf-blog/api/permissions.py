from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.method in permissions.SAFE_METHODS else False
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # return False

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class IsMerritt(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.username == "merritt"