from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import City, UserProfile, Post
from .forms import ProfileForm, UserChangeForm
from django.contrib.auth.models import User


class AccountAdmin(BaseUserAdmin):
    form = ProfileForm
    add_form = ProfileForm

    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('is_superuser')

    fieldsets = (
        (None, {'fields': {'email', 'is_staff', 'is_superuser', 'password'}}),
        ('Personal Info', {
         'fields': ('first_name', 'lastname', 'location', 'picture')}),
        ('Group', {'fields': ('groups',)}),
        ('Permission', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff',
                           'is_superuser', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name',
                                      'last_name', 'locations', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'location')
    ordering = ('email')
    filter_horizontal = ()


admin.site.register(City)
admin.site.register(Post)
admin.site.register(UserProfile)
