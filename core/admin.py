from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    list_per_page = 10

