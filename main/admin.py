from django.contrib import admin

from main import models


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
    fields = (
        'type',
        'title',
        'slug',
        'price',
        'get_small_bouquet_price',
        'get_middle_bouquet_price',
        'get_big_bouquet_price',
        'image',
        'is_active',
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


admin.site.register(models.Reason)
admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Flower)
admin.site.register(models.Configuration)
admin.site.register(models.Bouquet, BouquetAdmin)
