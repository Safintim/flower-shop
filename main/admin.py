from django.contrib import admin

from main import models

admin.site.register(models.Reason)
admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Product)
