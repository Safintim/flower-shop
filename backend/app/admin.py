from django import forms
from django.core.exceptions import ValidationError
from django.db import models as django_models
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
    search_fields = ('title',)


@admin.register(models.Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display_links = list_display = (
        'id',
        'title',
    )

    search_fields = ('title',)


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
    )

    search_fields = ('title',)
    list_filter = (
        'is_add_filter',
    )


class RequireOneFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        super().clean()
        if not self.is_valid():
            return
        if not self.forms or not self.forms[0].cleaned_data:
            raise ValidationError(
                'Как минимум один {} должен существовать'.format(
                    self.model._meta.verbose_name,
                )
            )


class FlowerInline(nested_admin.NestedTabularInline):
    model = models.BouquetFlower
    extra = 0
    min_num = 1
    formset = RequireOneFormSet


class FlowerCompactInline(CompactInline):
    model = models.BouquetFlower
    extra = 0


class ProductInline(nested_admin.NestedStackedInline):
    extra = 0
    model = models.Product
    inlines = (FlowerInline, )
    formfield_overrides = {
        django_models.TextField: {
            'widget': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        },
    }
    fields = (
        'size',
        'title',
        'price',
        'description',
    )
    readonly_fields = ('price', )
    verbose_name = 'Букет'
    verbose_name_plural = 'Букеты'
    min_num = 1
    formset = RequireOneFormSet


@admin.register(models.BaseBouquet)
class BaseBouquetAdmin(nested_admin.NestedModelAdmin):
    list_display = list_display_links = (
        'id',
        'photo_list_tag',
        'title',
        'is_active',
        'color',
        'min_price',
        'max_price',
        'discount',
    )

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'title',
                'description',
                'discount',
                'height',
                'width',
                'photo',
                'photo_detail_tag',
            ),
        }),
        ('Флаги', {
            'fields': ('is_active', 'is_new', 'is_hit', 'is_show_on_main_page'),
        }),
        ('Фильтры', {'fields': ('color', 'category', 'reason')}),
    )

    readonly_fields = ('photo_list_tag', 'photo_detail_tag')
    search_fields = ('title',)
    list_filter = ('is_active', 'color')
    inlines = (ProductInline, )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_display = list_display_links = (
        'id',
        'photo_list_tag',
        'title',
        'is_active',
        'kind',
        'present_price',
        'bouquet_price',

    )

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'kind',
                'title',
                'description',
                'price',
                'discount',
                'present_price',
                'photo',
                'photo_detail_tag',
            ),
        }),
        ('Флаги', {
            'fields': ('is_active', 'is_new', 'is_hit'),
        }),
        ('Дополнительная информация', {
            'fields': ('base', 'size', 'bouquet_price'),
        }),
    )
    readonly_fields = (
        'photo_list_tag',
        'photo_detail_tag',
        'present_price',
        'bouquet_price',
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


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = list_display_links = (
        'price_coefficient',
        'updated_at',
    )
