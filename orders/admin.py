from django.contrib import admin

from orders.models import OrderProduct, Order
from core.admin import BaseModelAdmin


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(BaseModelAdmin):
    inlines = (OrderProductInline,)


admin.site.register(Order, OrderAdmin)

