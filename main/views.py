from django.views import generic

from main import models


class ProductList(generic.ListView):
    model = models.Product
    paginate_by = 60


class ProductDetail(generic.DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context['object']
        if obj.is_bouquet():
            context['bouquets'] = obj.bouquets.order_by('-size')
        return context


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ShippingAndPaymentView(generic.TemplateView):
    template_name = 'shipping_and_payment.html'


class Contacts(generic.TemplateView):
    template_name = 'contacts.html'
