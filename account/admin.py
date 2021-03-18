from django.contrib import admin
from account.models import User

from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = list_display_links = ('id', 'phone', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', )
    ordering = ('id', 'phone', 'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name', 'email')}),
        ('Права', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', ),
        }),
    )
