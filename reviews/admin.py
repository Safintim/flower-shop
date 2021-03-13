from django.contrib import admin
from django.utils.safestring import mark_safe

from core.admin import BaseModelAdmin
from reviews.models import Review




class ReviewAdmin(BaseModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('name', 'text', 'city', 'phone')
    readonly_fields = ('image_detail',)

    def image_detail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=100 height="100"/>')
        return ''
    image_detail.short_description = 'Изображение'


admin.site.register(Review, ReviewAdmin)

