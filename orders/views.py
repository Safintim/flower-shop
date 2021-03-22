from django.views import generic

from cart.models import Cart
from orders.forms import OrderForm
from orders.models import Order


class OrderCreateView(generic.CreateView):
    model = Order
    template_name = 'orders/order_create.html'
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        cart = Cart.objects.filter(user=self.request.user).first()
        kwargs['cart_products'] = cart.products.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderListView(generic.ListView):
    model = Order
