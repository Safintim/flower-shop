from django.contrib import admin

from core.models import Configuration, Callback


class BaseModelAdmin(admin.ModelAdmin):
    list_per_page = 10


class ConfigurationAdmin(BaseModelAdmin):
    list_display = ('__str__', 'bouquet_price_coefficient',)
    list_editable = ('bouquet_price_coefficient',)


class CallbackAdmin(BaseModelAdmin):
    list_display = ('id', 'is_new', 'phone', 'created_at', 'updated_at')
    list_display_links = ('id', 'phone')
    list_editable = ('is_new',)
    list_filter = ('is_new',)


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Callback, CallbackAdmin)
