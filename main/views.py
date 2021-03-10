from django.views import generic

from main import models


class BaseProductListMixin:
    model = models.Product
    paginate_by = 60


class ProductByCategory(BaseProductListMixin, generic.ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(categories__slug=self.kwargs['slug'])


class ProductList(BaseProductListMixin, generic.ListView):
   pass


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
