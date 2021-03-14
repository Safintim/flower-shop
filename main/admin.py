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


from django import forms
from PIL import Image
import logging

class ProductAdminForm(forms.ModelForm):
    SMALL_RESOLUTION = (372, 372)
    BIG_RESOLUTION = (640, 640)

    class Meta:
        model = models.Product
        fields = '__all__'


    def clean(self):
        small_image = self.cleaned_data.get('small_image')
        sm_img = Image.open(small_image)
        width, height = self.SMALL_RESOLUTION
        if sm_img.width != width or sm_img.height != height:
            self.add_error('small_image', f'Размер должен быть {width}x{height}')

        big_image = self.cleaned_data.get('big_image')
        bg_img = Image.open(big_image)
        width, height = self.BIG_RESOLUTION
        if bg_img.width != width or big_img.height != height:
            self.add_error('big_image', f'Размер должен быть {width}x{height}')

        # Validation work not correct
        type_product = self.cleaned_data.get('type')
        if type_product != models.Product.TYPE_BOUQUET:
            return self.cleaned_data

        bouquets = self.cleaned_data.get('bouquets')
        exists_bouquets_count = 0
        if self.instance.id:
            exists_bouquets_count = self.instance.bouquets.count()
        logging.info(exists_bouquets_count)
        bouquets_count = bouquets.count() + exists_bouquets_count
        logging.info(bouquets_count)
        logging.info(bouquets.count())
        if bouquets_count > 3 or bouquets_count == 0:
            self.add_error('bouquets', 'Создайте хотя бы 1 букет (не больше 3)')
        return self.cleaned_data


class ProductAdmin(BaseModelAdmin):
    form = ProductAdminForm
    change_form_template = 'admin.html'
    save_on_top = True
    filter_horizontal = ('bouquets',)
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('type', 'title', 'slug', ('small_image', 'big_image'), 'small_image_detail')
        }),
        ('Цена', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('price', 'discount'),
        }),
        ('Настройки для букета', {
            'classes': ('collapse',),
            'fields': (('get_small_bouquet_price', 'get_middle_bouquet_price', 'get_big_bouquet_price'), 'bouquets')
        }),
        ('Фильтры', {
            'classes': ('collapse',),
            'fields': (('is_active', 'is_hit', 'is_new', 'color'), 'categories', 'reasons')
        })
    )
    list_display = ('id', 'small_image_list','title', 'price', 'is_active', 'is_hit', 'is_new', 'color')
    list_display_links = ('id', 'small_image_list', 'title')
    list_filter = ('price', 'type', 'is_active', 'is_hit', 'is_new', 'color')
    list_editable = ('is_active', 'is_hit', 'is_new', 'color')
    search_fields = ('title',)
    readonly_fields = ('get_small_bouquet_price', 'get_middle_bouquet_price', 'get_big_bouquet_price', 'small_image_detail')

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

    def small_image_detail(self, obj):
        url = obj.small_image.url if obj.small_image else 'https://via.placeholder.com/100'
        return mark_safe(f'<img src="{url}"/>')
    small_image_detail.short_description = 'Изображение'


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
