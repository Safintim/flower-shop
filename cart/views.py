from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import redirect
from django.views import generic

from cart.models import CartProduct


CartProductFormset = modelformset_factory(CartProduct, fields=('qty', ), extra=0, can_delete=True)


class CartProductListView(LoginRequiredMixin, generic.FormView):
    model = CartProduct
    template_name = 'cart/product_list.html'
    form_class = CartProductFormset

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['queryset'] = CartProduct.objects.filter(cart__user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('cart-product-update')
