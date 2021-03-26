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
        kwargs = {
            'reasons': models.Reason.objects.active(),
            'colors': models.Color.objects.active(),
            'flowers': models.Flower.objects.active(),
            'filter': ProductFilter(),
        }
        return super().get_context_data(object_list=self.get_queryset(), **kwargs)


class ProductByCategoryListView(BaseProductListMixin, generic.ListView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(categories__slug=self.kwargs['slug'])


class BouquetListView(BaseProductListMixin, generic.ListView):
    def get_queryset(self):
        return super().get_queryset().bouquets()


class ProductFilterView(BaseProductListMixin, generic.ListView):
    def get(self, request, *args, **kwargs):
        context = super().get_context_data()
        return render(request, 'main/list.html', context)


class ProductDetailView(generic.DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        if obj.is_bouquet:
            kwargs['bouquets'] = obj.bouquets.order_by('-size')
        kwargs['reviews'] = Review.objects.active().random(6)
        kwargs['similar_products'] = models.Product.objects.active().filter(
            categories__in=obj.categories.all()).random(4).exclude(pk=obj.pk)
        return super().get_context_data(**kwargs)


class IndexTemplateView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['hit_products'] = models.Product.objects.active().bouquets().hits().random(6)
        kwargs['new_products'] = models.Product.objects.active().bouquets().new().random(6)
        kwargs['reviews'] = Review.objects.active().random(6)
        return super().get_context_data(**kwargs)

