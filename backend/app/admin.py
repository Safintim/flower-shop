from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from mptt.admin import MPTTModelAdmin
from jet.admin import CompactInline
import nested_admin

from app import models

admin.site.unregister(Group)


@admin.register(models.User)
class UserAdminCustom(UserAdmin):
    list_display = list_display_links = (
        'id',
        'email',
    )

    fieldsets = (
        ('Личная информация', {
            'fields': ('email', 'password'),
        }),
        ('Права', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ('id', )

    search_fields = ('email',)


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display_links = list_display = (
        'id',
        'title',
    )


@admin.register(models.Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display_links = list_display = (
        'id',
        'title',
    )


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display_links = list_display = (
        'id',
        'rating',
        'city',
        'phone',
        'name',
    )


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display_links = list_display = (
        'title',
        'id',
    )
    fields = (
        'title',
        'parent',
    )
    mptt_level_indent = 20


@admin.register(models.Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'price',
        'is_add_filter',
    )

    search_fields = ('title',)
    list_filter = ('is_add_filter',)


class FlowerInline(nested_admin.NestedTabularInline):
    model = models.BouquetFlower
    extra = 0


class FlowerCompactInline(CompactInline):
    model = models.BouquetFlower
    extra = 0


class ProductInline(nested_admin.NestedTabularInline):
    extra = 0
    model = models.Product
    inlines = (FlowerInline, )


@admin.register(models.BaseBouquet)
class BaseBouquetAdmin(nested_admin.NestedModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'is_active',
        'color',
        'discount',
    )

    search_fields = ('title',)
    list_filter = ('is_active', 'color')
    inlines = (ProductInline, )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'title',
        'is_active',
        'kind',
        'price',
    )

    search_fields = ('title',)
    list_filter = ('is_active', 'kind')
    inlines = (FlowerCompactInline, )


class OrderItemInline(CompactInline):
    extra = 0
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'id',
        'status',
        'customer_name',
        'is_paid',
        'created_at',
        'updated_at',
    )

    list_filter = ('is_paid', 'status')
    inlines = (OrderItemInline, )
