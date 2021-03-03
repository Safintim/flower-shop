from django.contrib import admin

from main import models


class BouquetFlowerMiddleInline(admin.TabularInline):
    model = models.BouquetFlowerMiddle
    extra = 0


class BouquetFlowerSmallInline(admin.TabularInline):
    model = models.BouquetFlowerSmall
    extra = 0


class BouquetFlowerBigInline(admin.TabularInline):
    model = models.BouquetFlowerBig
    extra = 0


class BouquetAdmin(admin.ModelAdmin):
    inlines = (BouquetFlowerMiddleInline, BouquetFlowerSmallInline, BouquetFlowerBigInline)


admin.site.register(models.Reason)
admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Product)
admin.site.register(models.Flower)
admin.site.register(models.Bouquet, BouquetAdmin)
# admin.site.register(models.BouquetFlower)
