import phonenumbers
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from main import models
from main.filter import ProductFilter
from reviews.models import Review


class BaseProductListMixin:
    model = models.Product
    paginate_by = 1
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = self.model.objects.active()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self):
        context = super().get_context_data(object_list=self.get_queryset())
        context['reasons'] = models.Reason.objects.all()
        context['colors'] = models.Color.objects.all()
        context['flowers'] = models.Flower.objects.all()
        context['filter'] = ProductFilter()
        return context


class ProductByCategory(BaseProductListMixin, generic.ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(categories__slug=self.kwargs['slug'])


class ProductList(BaseProductListMixin, generic.ListView):
    def get_queryset(self):
        return super().get_queryset().bouquets()


class ProductFilterView(BaseProductListMixin, generic.ListView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        return render(request, 'main/list.html', context)


class ProductDetail(generic.DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context['object']
        if obj.is_bouquet:
            context['bouquets'] = obj.bouquets.order_by('-size')
        context['reviews'] = Review.objects.active().random(6)
        context['similar_products'] = models.Product.objects.active().filter(
            categories__in=obj.categories.all()).random(4).exclude(pk=obj.pk)
        return context


class CallbackView(generic.View):
    def post(self, request, *args, **kwargs):
        phone = request.POST.get('phone')
        try:
            phone_parse = phonenumbers.parse(phone, settings.PHONENUMBER_DEFAULT_REGION)
            if phonenumbers.is_valid_number(phone_parse):
                models.Callback.objects.create(phone=phone)
                return JsonResponse({'status': 'ok'})
        except phonenumbers.phonenumberutil.NumberParseException:
            pass
        return JsonResponse({'status': 'error'})


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hit_products'] = models.Product.objects.active().bouquets().hits().random(6)
        context['new_products'] = models.Product.objects.active().bouquets().new().random(6)
        context['reviews'] = Review.objects.active().random(6)
        return context


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ShippingAndPaymentView(generic.TemplateView):
    template_name = 'shipping_and_payment.html'


class Contacts(generic.TemplateView):
    template_name = 'contacts.html'
