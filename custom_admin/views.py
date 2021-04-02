from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from custom_admin.filter_helpers import CategoryFilterFormHelper, ReasonFilterFormHelper, ColorFilterFormHelper, \
    FlowerFilterFormHelper, ProductFilterFormHelper
from custom_admin.filters import CategoryFilter, ReasonFilter, ColorFilter, FlowerFilter, ProductFilter
from custom_admin.forms import ProductPresentForm, ProductBouquetForm, BouquetFlowerFormSet
from custom_admin.mixins import FilteredSingleTableView, CreateUpdateMixin, DeleteMixin, BaseTemplateResponseMixin
from custom_admin.tables import CategoryTable, ReasonTable, ColorTable, FlowerTable, ProductTable
from main.models import Category, Reason, Color, Flower, Product, Bouquet, BouquetFlower


class IndexTemplateView(generic.TemplateView):
    template_name = 'custom_admin/index.html'


class CategoryListView(FilteredSingleTableView):
    model = Category
    table_class = CategoryTable
    filterset_class = CategoryFilter
    form_helper_class = CategoryFilterFormHelper
    create_view_name = 'custom_admin:category-create'


class CategoryUpdateView(CreateUpdateMixin, generic.UpdateView):
    model = Category
    success_view_name = 'custom_admin:category-update'
    delete_view_name = 'custom_admin:category-delete'


class CategoryCreateView(CreateUpdateMixin, generic.CreateView):
    model = Category
    success_view_name = 'custom_admin:category-update'


class CategoryDeleteView(DeleteMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy('custom_admin:category-list')
    update_view_name = 'custom_admin:category-update'


class ReasonListView(FilteredSingleTableView):
    model = Reason
    table_class = ReasonTable
    filterset_class = ReasonFilter
    form_helper_class = ReasonFilterFormHelper
    create_view_name = 'custom_admin:reason-create'


class ReasonUpdateView(CreateUpdateMixin, generic.UpdateView):
    model = Reason
    success_view_name = 'custom_admin:reason-update'
    delete_view_name = 'custom_admin:reason-delete'


class ReasonCreateView(CreateUpdateMixin, generic.CreateView):
    model = Reason
    success_view_name = 'custom_admin:reason-update'


class ReasonDeleteView(DeleteMixin, generic.DeleteView):
    model = Reason
    success_url = reverse_lazy('custom_admin:reason-list')
    update_view_name = 'custom_admin:reason-update'


class ColorListView(FilteredSingleTableView):
    model = Color
    table_class = ColorTable
    filterset_class = ColorFilter
    form_helper_class = ColorFilterFormHelper
    create_view_name = 'custom_admin:color-create'


class ColorUpdateView(CreateUpdateMixin, generic.UpdateView):
    model = Color
    success_view_name = 'custom_admin:color-update'
    delete_view_name = 'custom_admin:color-delete'


class ColorCreateView(CreateUpdateMixin, generic.CreateView):
    model = Color
    success_view_name = 'custom_admin:color-update'


class ColorDeleteView(DeleteMixin, generic.DeleteView):
    model = Color
    success_url = reverse_lazy('custom_admin:color-list')
    update_view_name = 'custom_admin:color-update'


class FlowerListView(FilteredSingleTableView):
    model = Flower
    table_class = FlowerTable
    filterset_class = FlowerFilter
    form_helper_class = FlowerFilterFormHelper
    create_view_name = 'custom_admin:flower-create'


class FlowerUpdateView(CreateUpdateMixin, generic.UpdateView):
    model = Flower
    success_view_name = 'custom_admin:flower-update'
    delete_view_name = 'custom_admin:flower-delete'


class FlowerCreateView(CreateUpdateMixin, generic.CreateView):
    model = Flower
    success_view_name = 'custom_admin:flower-update'


class FlowerDeleteView(DeleteMixin, generic.DeleteView):
    model = Flower
    success_url = reverse_lazy('custom_admin:flower-list')
    update_view_name = 'custom_admin:flower-update'


class ProductListView(FilteredSingleTableView):
    model = Product
    table_class = ProductTable
    filterset_class = ProductFilter
    form_helper_class = ProductFilterFormHelper
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
    model = Product
    form_class = ProductBouquetForm

    def get_success_url(self):
        return reverse('custom_admin:product-bouquet-update', kwargs={'pk': self.object.pk})


class ProductBouquetCreateView(BouquetUpdateCreate, generic.CreateView):
    template_name_suffix = 'edit'


class ProductBouquetUpdateView(BouquetUpdateCreate, generic.UpdateView):
    template_name_suffix = 'bouquet_edit'


# TODO удалить все ниже
class BouquetSmallCreateView(BaseTemplateResponseMixin, generic.FormView):
    template_name_suffix = 'bouquet_size_edit'
    form_class = BouquetFlowerFormSet

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Создать букет (маленький)'
        kwargs['action'] = reverse('custom_admin:bouquet-small-create', kwargs={'pk': self.kwargs['pk']})
        kwargs['formset'] = kwargs.get('form') or self.get_form()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        if self.product.bouquets.filter(size=Bouquet.Size.SM).exists():
            return redirect('custom_admin:product-bouquet-update', kwargs={'pk': self.product.pk})

        bouquet = Bouquet.objects.create(size=Bouquet.Size.SM)
        formset = self.form_class(instance=bouquet, **self.get_form_kwargs())
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            return self.form_invalid(formset)

    def form_valid(self, formset):
        formset.save()
        self.product.bouquets.add(formset.instance)
        return redirect('custom_admin:product-bouquet-update', kwargs={'pk': self.product.pk})


class BouquetSmallUpdateView(BaseTemplateResponseMixin, generic.FormView):
    template_name_suffix = 'bouquet_size_edit'
    form_class = BouquetFlowerFormSet
    model = BouquetFlower

    def get_context_data(self, **kwargs):
        kwargs['formset'] = kwargs.get('form') or self.get_form()
        return super().get_context_data(**kwargs)

    def get_object(self, queryset=None):
        self.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        bouquet = self.product.bouquets.filter(size=Bouquet.Size.SM).first()
        return bouquet

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return self.form_class(**self.get_form_kwargs(), instance=self.object)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, formset):
        formset.save()
        self.product.bouquets.add(formset.instance)
        return super().form_valid(formset)

    def get_success_url(self):
        return reverse('custom_admin:product-bouquet-update', kwargs={'pk': self.product.pk})
