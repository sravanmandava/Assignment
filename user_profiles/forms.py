from user_profiles.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserProfileCreationForm(UserCreationForm):

	class Meta():
		model = UserProfile
		fields = ('username','email','first_name','last_name', 'date_of_birth')
		widgets = {
            'date_of_birth': forms.DateInput(attrs={'class':'datepicker'}),
        }


	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["username"]

		if commit:
			user.save()

		return user









class UserProfileChangeForm(UserChangeForm):

	class Meta():
		model = UserProfile
		fields = ('username','email', 'date_of_birth','first_name','last_name',)
		widgets = {
            'date_of_birth': forms.DateInput(attrs={'class':'datepicker'}),
        }

	def save(self, commit=True):
		user = super().save(commit=False)
		user.username = self.cleaned_data["username"]

		if commit:
			user.save()

		return user
