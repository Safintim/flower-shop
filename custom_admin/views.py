from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from custom_admin.filter_helpers import CategoryFilterFormHelper, ReasonFilterFormHelper, ColorFilterFormHelper, \
    FlowerFilterFormHelper, ProductFilterFormHelper
from custom_admin.filters import CategoryFilter, ReasonFilter, ColorFilter, FlowerFilter, ProductFilter
from custom_admin.forms import ProductPresentForm, ProductBouquetForm, BouquetFlowerFormSet
from custom_admin.mixins import FilteredSingleTableView, CreateUpdateMixin, DeleteMixin, BaseTemplateResponseMixin
from custom_admin.tables import CategoryTable, ReasonTable, ColorTable, FlowerTable, ProductTable
from main.models import Category, Reason, Color, Flower, Product, Bouquet


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


class ProductPresentCreateView(PresentUpdateCreate, generic.CreateView):
    def get_success_url(self):
        return reverse('custom_admin:product-list')


class ProductPresentUpdateView(PresentUpdateCreate, generic.UpdateView):
    def get_success_url(self):
        return reverse('custom_admin:product-present-update', kwargs={'pk': self.object.pk})


class BouquetUpdateCreate(BaseTemplateResponseMixin):
    model = Product
    form_class = ProductBouquetForm


class ProductBouquetCreateView(BouquetUpdateCreate, generic.CreateView):
    template_name_suffix = 'edit'


class ProductBouquetUpdateView(BouquetUpdateCreate, generic.UpdateView):
    template_name_suffix = 'bouquet_edit'


class BouquetSmallCreateView(BaseTemplateResponseMixin, generic.FormView):
    template_name_suffix = 'bouquet_size_edit'
    form_class = BouquetFlowerFormSet

    def get_context_data(self, **kwargs):
        return super().get_context_data(formset=self.get_form(), **kwargs)

    def post(self, request, pk, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=pk)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, formset):
        bouquet = Bouquet.objects.create(size=Bouquet.Size.SM)
        flowers = formset.save(commit=False)
        flowers.instance = bouquet
        flowers.save()
        self.product.bouquets.add(bouquet)
        return redirect('custom_admin:product-bouquet-update')
