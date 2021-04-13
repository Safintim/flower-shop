from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import generic

from cart.models import Cart
from core.models import Callback, Configuration
from custom_admin.filter_helpers import ProductFilterFormHelper
from custom_admin.filters import CategoryFilter, ReasonFilter, ColorFilter, FlowerFilter, ProductFilter, ReviewFilter, \
    CallbackFilter, UserFilter, CartFilter, OrderFilter
from custom_admin.forms import ProductPresentForm, ProductBouquetForm, BouquetFlowerFormSet
from custom_admin.mixins import FilteredSingleTableView, DeleteMixin, BaseTemplateResponseMixin, \
    DetailMixin, UpdateMixin, CreateMixin
from custom_admin.tables import CategoryTable, ReasonTable, ColorTable, FlowerTable, ProductTable, ReviewTable, \
    CallbackTable, UserTable, CartTable, OrderTable
from main.models import Category, Reason, Color, Flower, Product, Bouquet, BouquetFlower
from orders.models import Order
from reviews.models import Review


class IndexTemplateView(BaseTemplateResponseMixin, generic.TemplateView):
    template_name_suffix = 'index'


class CategoryListView(FilteredSingleTableView):
    model = Category
    table_class = CategoryTable
    filterset_class = CategoryFilter


class CategoryUpdateView(UpdateMixin, generic.UpdateView):
    model = Category


class CategoryCreateView(CreateMixin, generic.CreateView):
    model = Category


class CategoryDeleteView(DeleteMixin, generic.DeleteView):
    model = Category


class ReasonListView(FilteredSingleTableView):
    model = Reason
    table_class = ReasonTable
    filterset_class = ReasonFilter


class ReasonUpdateView(UpdateMixin, generic.UpdateView):
    model = Reason


class ReasonCreateView(CreateMixin, generic.CreateView):
    model = Reason


class ReasonDeleteView(DeleteMixin, generic.DeleteView):
    model = Reason


class ColorListView(FilteredSingleTableView):
    model = Color
    table_class = ColorTable
    filterset_class = ColorFilter


class ColorUpdateView(UpdateMixin, generic.UpdateView):
    model = Color


class ColorCreateView(CreateMixin, generic.CreateView):
    model = Color


class ColorDeleteView(DeleteMixin, generic.DeleteView):
    model = Color


class FlowerListView(FilteredSingleTableView):
    model = Flower
    table_class = FlowerTable
    filterset_class = FlowerFilter


class FlowerUpdateView(UpdateMixin, generic.UpdateView):
    model = Flower


class FlowerCreateView(CreateMixin, generic.CreateView):
    model = Flower


class FlowerDeleteView(DeleteMixin, generic.DeleteView):
    model = Flower


class ReviewListView(FilteredSingleTableView):
    model = Review
    table_class = ReviewTable
    filterset_class = ReviewFilter


class ReviewUpdateView(UpdateMixin, generic.UpdateView):
    model = Review


class ReviewCreateView(CreateMixin, generic.CreateView):
    model = Review


class ReviewDeleteView(DeleteMixin, generic.DeleteView):
    model = Review


class CallbackListView(FilteredSingleTableView):
    model = Callback
    table_class = CallbackTable
    filterset_class = CallbackFilter


class CallbackUpdateView(UpdateMixin, generic.UpdateView):
    model = Callback
    fields = ('phone',)

    def set_read(self):
        obj = self.get_object()
        obj.is_new = False
        obj.save()

    def get(self, request, *args, **kwargs):
        self.set_read()
        return super().get(request, *args, **kwargs)


class CallbackCreateView(CreateMixin, generic.CreateView):
    model = Callback


class CallbackDeleteView(DeleteMixin, generic.DeleteView):
    model = Callback


class ConfigurationUpdateView(UpdateMixin, generic.UpdateView):
    model = Configuration
    success_view_name = 'custom_admin:configuration-update'

    def get_object(self, queryset=None):
        return Configuration.load()

    def get_success_url(self):
        return reverse(self.success_view_name)


User = get_user_model()


class UserListView(FilteredSingleTableView):
    model = User
    table_class = UserTable
    filterset_class = UserFilter


class UserUpdateView(UpdateMixin, generic.UpdateView):
    model = User
    fields = ('phone', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined')


class UserCreateView(CreateMixin, generic.CreateView):
    model = User
    fields = ('phone', 'password', 'first_name', 'last_name', 'email', 'is_active')


class UserDeleteView(DeleteMixin, generic.DeleteView):
    model = User


class CartListView(FilteredSingleTableView):
    model = Cart
    table_class = CartTable
    filterset_class = CartFilter
    show_button_create = False


class CartDetailView(DetailMixin, BaseTemplateResponseMixin, generic.DetailView):
    model = Cart
    extra_context = {'is_cart': True}


class OrderListView(FilteredSingleTableView):
    model = Order
    table_class = OrderTable
    filterset_class = OrderFilter
    show_button_create = False


class OrderDetailView(DetailMixin, UpdateMixin, generic.UpdateView):
    model = Order
    show_button_delete = False
    fields = ('status',)


class ProductListView(FilteredSingleTableView):
    model = Product
    table_class = ProductTable
    filterset_class = ProductFilter
    form_helper_class = ProductFilterFormHelper
    show_button_create = False
    extra_context = {
        'present_create_view_name': 'custom_admin:product-present-create',
        'bouquet_create_view_name': 'custom_admin:product-bouquet-create'
    }


class PresentUpdateCreate(BaseTemplateResponseMixin):
    template_name_suffix = 'edit'
    model = Product
    form_class = ProductPresentForm

    def get_success_url(self):
        return reverse('custom_admin:product-present-update', kwargs={'pk': self.object.pk})


class ProductPresentCreateView(PresentUpdateCreate, generic.CreateView):
    pass


class ProductPresentUpdateView(PresentUpdateCreate, generic.UpdateView):
    pass


class BouquetUpdateCreate(BaseTemplateResponseMixin):
    template_name_suffix = 'edit'
    model = Product
    form_class = ProductBouquetForm

    def get_success_url(self):
        return reverse('custom_admin:product-bouquet-update', kwargs={'pk': self.object.pk})


class ProductBouquetCreateView(BouquetUpdateCreate, generic.CreateView):
    pass


class ProductBouquetUpdateView(BouquetUpdateCreate, generic.UpdateView):
    pass
