from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
'''
class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [rest_framework.authentication.BasicAuthentication, rest_framework.authentication.SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated():
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES)
        return False
'''
class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
