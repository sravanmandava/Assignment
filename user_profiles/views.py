from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from user_profiles.forms import UserProfileCreationForm, UserProfileChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from user_profiles.models import UserProfile
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.views import (
	LoginView,
	PasswordChangeView,
	PasswordResetView,
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	)


class UserLogin(SuccessMessageMixin, LoginView):
	redirect_authenticated_user = True
	template_name = 'user_profiles/login.html'


class UserCreate(SuccessMessageMixin, CreateView):
	model = UserProfile
	form_class = UserProfileCreationForm
	template_name = 'user_profiles/user-new.html'
	success_url = reverse_lazy('index')
	success_message = 'User Created successfully'

	def get(self, request, *args, **kwargs):

		return super().get(request, *args, **kwargs)
		

class UserChange(SuccessMessageMixin, UpdateView):
	model = UserProfile
	form_class = UserProfileChangeForm
	template_name = 'user_profiles/user-change.html'
	success_url = reverse_lazy('index')
	success_message = 'Your profile change was successful'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)



class UserDelete(SuccessMessageMixin, DeleteView):
	model = UserProfile
	success_url = reverse_lazy('index')
	template_name = 'user_profiles/user-delete.html'

	def get_queryset(self):

		if self.request.user.is_authenticated:
			return self.model.objects.filter(username=self.request.user)

		else:
			return super().get_queryset().filter(username=None)


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
	template_name = 'user_profiles/password-change.html'
	success_url = reverse_lazy('index')
	success_message = 'Your password change was successful'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
	template_name = 'user_profiles/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
	success_message = 'Your password has been reset correctly. Log in to start'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
	template_name = 'user_profiles/password-reset-complete.html'
	success_message = 'Your password has been reset correctly. Log in to start'

	# For use with a html template, don't subscrive the 'get' method
	# and use the template 'template_name = '
	def get(self, request, *args, **kwargs):

		return redirect('login')
