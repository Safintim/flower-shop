from django.urls import reverse, reverse_lazy
from django.views import generic
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from custom_admin.filters import CategoryFilter, CategoryFilterFormHelper
from custom_admin.forms import CreateUpdateFormHelper
from custom_admin.tables import CategoryTable
from main.models import Category


class BaseTemplateResponseMixin:
    def get_template_names(self):
        if self.template_name:
            return self.template_name
        return 'custom_admin/{}.html'.format(self.template_name_suffix)


# TEMPLATE_NAME_PATTERN = 'custom_admin/{}.html'


class IndexTemplateView(generic.TemplateView):
    template_name = 'custom_admin/index.html'


class FilteredSingleTableView(BaseTemplateResponseMixin, SingleTableMixin, FilterView):
    template_name_suffix = 'list'
    form_helper_class = None
    create_view_name = None
    paginate_by = 10

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.form_helper_class()
        return filterset

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Все {}'.format(self.model._meta.verbose_name_plural)
        kwargs['create_view_name'] = self.create_view_name
        return super().get_context_data(**kwargs)


class CreateUpdateMixin(BaseTemplateResponseMixin):
    template_name_suffix = 'edit'
    fields = '__all__'
    form_helper_class = CreateUpdateFormHelper
    actions = None
    success_view_name = None
    views = {}

    def get_actions(self):
        kwargs = {}
        if self.object:
            kwargs['pk'] = self.object.pk

        actions = {
            'create_update_action': reverse(self.views.get('create_update'), kwargs=kwargs),
        }
        if self.views.get('delete'):
            actions['delete_action'] = reverse(self.views.get('delete'), kwargs=kwargs)
        return actions

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = self.form_helper_class(form=form, **self.get_actions())
        return form

    def get_success_url(self):
        return reverse(self.views.get('success'), kwargs={'pk': self.object.pk})


class DeleteMixin(BaseTemplateResponseMixin):
    template_name_suffix = 'delete'
    update_view_name = None

    def get_context_data(self, **kwargs):
        kwargs['object_name'] = self.model._meta.verbose_name
        kwargs['back_link'] = reverse(self.update_view_name, kwargs={'pk': self.object.pk})
        return super().get_context_data(**kwargs)


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

