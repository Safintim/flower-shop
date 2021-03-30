from django.urls import reverse_lazy
from django.views import generic

from custom_admin.filter_helpers import CategoryFilterFormHelper, ReasonFilterFormHelper, ColorFilterFormHelper
from custom_admin.filters import CategoryFilter, ReasonFilter, ColorFilter
from custom_admin.mixins import FilteredSingleTableView, CreateUpdateMixin, DeleteMixin
from custom_admin.tables import CategoryTable, ReasonTable, ColorTable
from main.models import Category, Reason, Color


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
    views = {
        'create_update': 'custom_admin:category-update',
        'delete': 'custom_admin:category-delete',
        'success': 'custom_admin:category-update',
    }


class CategoryCreateView(CreateUpdateMixin, generic.CreateView):
    model = Category
    views = {
        'create_update': 'custom_admin:category-create',
        'success': 'custom_admin:category-update',
    }


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
    views = {
        'create_update': 'custom_admin:reason-update',
        'delete': 'custom_admin:reason-delete',
        'success': 'custom_admin:reason-update',
    }


class ReasonCreateView(CreateUpdateMixin, generic.CreateView):
    model = Reason
    views = {
        'create_update': 'custom_admin:reason-create',
        'success': 'custom_admin:reason-update',
    }


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
    views = {
        'create_update': 'custom_admin:color-update',
        'delete': 'custom_admin:color-delete',
        'success': 'custom_admin:color-update',
    }


class ColorCreateView(CreateUpdateMixin, generic.CreateView):
    model = Color
    views = {
        'create_update': 'custom_admin:color-create',
        'success': 'custom_admin:color-update',
    }


class ColorDeleteView(DeleteMixin, generic.DeleteView):
    model = Color
    success_url = reverse_lazy('custom_admin:color-list')
    update_view_name = 'custom_admin:color-update'


