from django.contrib import admin

from cart.models import CartProduct, Cart
from core.admin import BaseModelAdmin


class CartProductInline(admin.TabularInline):
    model = CartProduct
    extra = 0


class CartAdmin(BaseModelAdmin):
    fields = ('user', )
    inlines = (CartProductInline,)


admin.site.register(Cart, CartAdmin)
