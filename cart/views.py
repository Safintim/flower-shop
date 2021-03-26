from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.views import generic

from cart.models import CartProduct, Cart
from main.models import Product

CartProductFormset = forms.modelformset_factory(CartProduct, fields=('qty', ), extra=0, can_delete=True)


class CartProductListView(LoginRequiredMixin, generic.FormView):
    model = CartProduct
    template_name = 'cart/product_list.html'
    form_class = CartProductFormset

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['queryset'] = CartProduct.objects.filter(cart__user=self.request.user)
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['formset'] = self.get_form()
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        kwargs['cart'] = cart
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('cart-product-update')


class AddProductToCartView(LoginRequiredMixin, generic.View):
    def post(self, request, product_pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_pk)
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        bouquet_size = request.GET.get('size')
        cart.add_product(product, bouquet_size)
        return JsonResponse({'cart_total': cart.price_total})


class DeleteProductFromCartView(LoginRequiredMixin, generic.View):
    model = CartProduct

    def post(self, request, pk, *args, **kwargs):
        cart_product = get_object_or_404(CartProduct, pk=pk)
        cart_product.delete()
        return JsonResponse({'status': 'ok'})

