from django.contrib import admin
from django.db.models import Min
from django.utils.safestring import mark_safe

from core.admin import BaseModelAdmin
from main import models


class BouquetFlowerInline(admin.TabularInline):
    model = models.BouquetFlower
    extra = 0


class BouquetAdmin(BaseModelAdmin):
    fields = ('size', 'title', 'price', 'bouquet_price_coefficient')
    list_display = ('id', 'title', 'size', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('size',)
    readonly_fields = ('price', 'bouquet_price_coefficient')
    inlines = (BouquetFlowerInline, )

    def bouquet_price_coefficient(self, obj):
        return models.Configuration.load().bouquet_price_coefficient
    bouquet_price_coefficient.short_description = 'Наценка на цветы'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.price = models.Bouquet.calculate_bouquet_price(form.instance)
        form.save()


class ProductAdmin(BaseModelAdmin):
    change_form_template = 'admin.html'
    save_on_top = True
    fields = (
        'type',
        'title',
        'slug',
        'price',
        'get_small_bouquet_price',
        'get_middle_bouquet_price',
        'get_big_bouquet_price',
        'small_image',
        'big_image',
        'is_active',
        'is_hit',
        'is_new',
        'discount',
        'categories',
        'color',
        'reasons',
        'bouquets',
    )
    list_display = ('id', 'small_image_list','title', 'price', 'is_active', 'is_hit', 'is_new', 'color')
    list_display_links = ('id', 'small_image_list', 'title')
    list_filter = ('price', 'type', 'is_active', 'is_hit', 'is_new', 'color')
    list_editable = ('is_active', 'is_hit', 'is_new', 'color')
    search_fields = ('title',)
    readonly_fields = ('get_small_bouquet_price', 'get_middle_bouquet_price', 'get_big_bouquet_price')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('type', )
        return self.readonly_fields

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = {'object': self.get_object(request, object_id)}
        return super().change_view(request, object_id, form_url, extra_context)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        for formset in formsets:
            print(formset.model)
        if form.instance.type == models.Product.TYPE_BOUQUET:
            min_price = form.instance.bouquets.aggregate(Min('price'))['price__min']
            form.instance.price = min_price
            form.save()

    def small_image_list(self, obj):
        url = obj.small_image.url if obj.small_image else 'https://via.placeholder.com/100'
        return mark_safe(f'<img src="{url}" width=100 height="100" />')
    small_image_list.short_description = 'Изображение'


class CartProductInline(admin.TabularInline):
    model = models.CartProduct
    extra = 0


class CartAdmin(BaseModelAdmin):
    fields = ('user', )
    inlines = (CartProductInline,)


class FlowerAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'price', 'is_add_filter')
    list_display_links = ('id', 'title')
    list_filter = ('is_add_filter',)
    list_editable = ('price', 'is_add_filter')
    search_fields = ('title',)


class ConfigurationAdmin(BaseModelAdmin):
    list_display = ('__str__', 'bouquet_price_coefficient',)
    list_editable = ('bouquet_price_coefficient',)


class CategoryAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_active')
    list_display_links = ('id', 'title')
    list_editable = ('parent', 'is_active')
    list_filter = ('is_active', 'parent')


admin.site.register(models.Reason)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Color)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Flower, FlowerAdmin)
admin.site.register(models.Configuration, ConfigurationAdmin)
admin.site.register(models.Bouquet, BouquetAdmin)
admin.site.register(models.Cart, CartAdmin)
