from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as FlatpageFormOld
from django.contrib.flatpages.models import FlatPage
from django.db import models as django_models

from ckeditor.widgets import CKEditorWidget
from django.db.models import Min

from main import models


class FlatPageAdmin(FlatpageFormOld):
    formfield_overrides = {
        django_models.TextField: {'widget': CKEditorWidget}
    }


class BouquetFlowerInline(admin.TabularInline):
    model = models.BouquetFlower
    extra = 0


class BouquetAdmin(admin.ModelAdmin):
    fields = ('size', 'title', 'price', 'bouquet_price_coefficient')
    readonly_fields = ('price', 'bouquet_price_coefficient')
    inlines = (BouquetFlowerInline, )

    def bouquet_price_coefficient(self, obj):
        return models.Configuration.load().bouquet_price_coefficient
    bouquet_price_coefficient.short_description = 'Наценка на цветы'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.price = models.Bouquet.calculate_bouquet_price(form.instance)
        form.save()


class ProductAdmin(admin.ModelAdmin):
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
        if form.instance.type == models.Product.TYPE_BOUQUET:
            min_price = form.instance.bouquets.aggregate(Min('price'))['price__min']
            form.instance.price = min_price
            form.save()


class CartProductInline(admin.TabularInline):
    model = models.CartProduct
    extra = 0


class CartAdmin(admin.ModelAdmin):
    fields = ('user', )
    inlines = (CartProductInline,)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(models.Reason)
admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Flower)
admin.site.register(models.Configuration)
admin.site.register(models.Bouquet, BouquetAdmin)
admin.site.register(models.Cart, CartAdmin)
