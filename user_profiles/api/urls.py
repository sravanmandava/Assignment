from rest_framework.routers import DefaultRouter
from user_profiles.api.views import UserProfileViewSet,UserLoginApiView,ChangePasswordView
from django.urls import path, include

router = DefaultRouter()
router.register('profiles',UserProfileViewSet)



urlpatterns = [
	path('',include(router.urls)),
    path('login/', UserLoginApiView.as_view()),
	path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
