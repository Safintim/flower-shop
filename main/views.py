from django.views import generic

from main import models


class ProductList(generic.ListView):
    model = models.Product


class ProductDetail(generic.DetailView):
    model = models.Product
