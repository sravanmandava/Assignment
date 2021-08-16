from rest_framework import serializers
from user_profiles.models import UserProfile
from user_profiles.api.permissions import IsSuperUser
from django.contrib.auth.decorators import user_passes_test
from rest_framework.permissions import IsAuthenticated


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfile
        fields=('id','email','username','first_name','last_name','date_of_birth','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            },
        }

    def create(self,validated_data):
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            username = validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth = validated_data['date_of_birth'],
            password=validated_data['password'],
        )
        return user


    def update(self, instance, validated_data):
        """Handle updating user account"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)






class ChangePasswordSerializer(serializers.Serializer):
    model = UserProfile

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
