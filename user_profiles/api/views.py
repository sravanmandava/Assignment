from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import filters,generics
from user_profiles.models import UserProfile
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from user_profiles.api.serializers import UserProfileSerializer,ChangePasswordSerializer
from user_profiles.api.permissions import UpdateOwnProfile,IsSuperUser
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404
from user_profiles.api.permissions import UpdateOwnProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset=UserProfile.objects.all()
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsSuperUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','email',)

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'update':
            return [UpdateOwnProfile(),IsAuthenticated()]
        return super(UserProfileViewSet, self).get_permissions()





class UserLoginApiView(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = UserProfile
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
