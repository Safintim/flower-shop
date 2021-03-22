from django.views import generic

from orders.forms import OrderForm
from orders.models import Order


class OrderCreateView(generic.CreateView):
    model = Order
    template_name = 'orders/order_create.html'
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderListView(generic.ListView):
    model = Order
