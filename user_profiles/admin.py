from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user_profiles.forms import UserProfileChangeForm,UserProfileCreationForm
from user_profiles.models import UserProfile

class UserProfileAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserProfileChangeForm
    add_form = UserProfileCreationForm
    model = UserProfile

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username','email','first_name','last_name','date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','first_name','last_name','date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('username','email',)
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(UserProfile, UserProfileAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)
