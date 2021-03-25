from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from cart.models import Cart
from orders.forms import OrderForm, OrderCheckStatusForm
from orders.models import Order


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'orders/order_create.html'
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        cart = Cart.objects.filter(user=self.request.user).first()
        kwargs['cart'] = cart
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        order = form.save()
        order.create_order_products()
        return redirect('user-detail')


class OrderCheckStatus(generic.FormView):
    model = Order
    template_name = 'orders/check_order.html'
    form_class = OrderCheckStatusForm

    def form_valid(self, form):
        return redirect('order-check-status-show', pk=form.cleaned_data['pk'])


class OrderCheckStatusShow(generic.TemplateView):
    template_name = 'orders/check_order_show.html'

    def get_context_data(self, **kwargs):
        kwargs['order'] = Order.objects.get(pk=kwargs.get('pk'))
        return super().get_context_data(**kwargs)

