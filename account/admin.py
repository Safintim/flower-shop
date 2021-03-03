from django.contrib import admin
from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('id', 'login',)
    search_fields = ('login',)
    ordering = ('id', 'login',)
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Права', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login',),
        }),
    )
