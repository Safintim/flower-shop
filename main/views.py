from django.shortcuts import render
from django.views import generic

from main import models
from main.filter import ProductFilter


class BaseProductListMixin:
    model = models.Product
    paginate_by = 1
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = self.model.objects.all()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self):
        context = super().get_context_data(object_list=self.get_queryset())
        context['reasons'] = models.Reason.objects.all()
        context['filter'] = ProductFilter()
        return context


class ProductByCategory(BaseProductListMixin, generic.ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(categories__slug=self.kwargs['slug'])


class ProductList(BaseProductListMixin, generic.ListView):
    pass


class ProductFilterView(BaseProductListMixin, generic.ListView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        return render(request, 'main/list.html', context)


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
