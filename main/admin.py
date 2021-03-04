from django.contrib import admin

from main import models


class BouquetFlowerInline(admin.TabularInline):
    model = models.BouquetFlower
    extra = 0


class BouquetAdmin(admin.ModelAdmin):
    inlines = (BouquetFlowerInline, )

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.price = models.Bouquet.calculate_bouquet_price(form.instance)
        form.save()


admin.site.register(models.Reason)
admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Product)
admin.site.register(models.Flower)
admin.site.register(models.Bouquet, BouquetAdmin)
