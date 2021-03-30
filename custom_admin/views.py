from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from custom_admin.filters import CategoryFilter, CategoryFilterFormHelper
from custom_admin.tables import CategoryTable
from main.models import Category


class BaseTemplateResponseMixin:
    def get_template_names(self):
        if self.template_name:
            return self.template_name
        return 'custom_admin/{}.html'.format(self.template_name_suffix)


TEMPLATE_NAME_PATTERN = 'custom_admin/{}.html'


class IndexTemplateView(generic.TemplateView):
    template_name = 'custom_admin/index.html'


class FilteredSingleTableView(BaseTemplateResponseMixin, SingleTableMixin, FilterView):
    form_helper_class = None
    paginate_by = 10

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.form_helper_class()
        return filterset

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Все {}'.format(self.model._meta.verbose_name_plural)
        return super().get_context_data(**kwargs)


class CategoryListView(FilteredSingleTableView):
    template_name_suffix = 'list'
    model = Category
    table_class = CategoryTable
    filterset_class = CategoryFilter
    form_helper_class = CategoryFilterFormHelper


class CategoryUpdateView(generic.UpdateView):
    template_name_suffix = 'edit'
    model = Category
    fields = '__all__'
