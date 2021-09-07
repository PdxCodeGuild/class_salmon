# https://www.django-rest-framework.org/api-guide/permissions/#allowany
from rest_framework import permissions

# class ReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return True if request.method in permissions.SAFE_METHODS else False

# class IsAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user.username in ['nick']

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.author == request.user#assigned last name here to match the user last name for editing purposes, corruptable
#this should allow anything to fly for lab purposes.
class AllowAny(permissions.BasePermission):
    def has_permission(self, request, view):
        return True