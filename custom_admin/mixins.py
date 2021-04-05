from django.urls import reverse
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from custom_admin.filter_helpers import ListFormHelper
from custom_admin.forms import CreateUpdateFormHelper


class BaseTemplateResponseMixin:
    def get_template_names(self):
        if self.template_name:
            return self.template_name
        return 'custom_admin/{}.html'.format(self.template_name_suffix)


class FilteredSingleTableView(BaseTemplateResponseMixin, SingleTableMixin, FilterView):
    template_name_suffix = 'list'
    form_helper_class = None
    create_view_name = None
    paginate_by = 10

    def get_form_helper(self, form=None):
        if self.form_helper_class is None:
            return ListFormHelper(form=form)
        return self.form_helper_class()

    def get_filterset(self, filterset_class):
        kwargs = self.get_filterset_kwargs(filterset_class)
        filterset = filterset_class(**kwargs)
        filterset.form.helper = self.get_form_helper(form=filterset.form)
        return filterset

    def get_context_data(self, **kwargs):
        kwargs['title'] = 'Все {}'.format(self.model._meta.verbose_name_plural)
        kwargs['create_view_name'] = self.create_view_name
        return super().get_context_data(**kwargs)


class CreateUpdateMixin(BaseTemplateResponseMixin):
    template_name_suffix = 'edit'
    fields = '__all__'
    form_helper_class = CreateUpdateFormHelper
    success_view_name = None
    delete_view_name = None

    def get_delete_action(self):
        if self.delete_view_name:
            return reverse(self.delete_view_name, kwargs={'pk':self.object.pk})

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class()
        helper = self.form_helper_class(form=form, delete_action=self.get_delete_action())
        form_class.helper = property(lambda _: helper)
        return form_class(**self.get_form_kwargs())

    def get_success_url(self):
        return reverse(self.success_view_name, kwargs={'pk': self.object.pk})


class DeleteMixin(BaseTemplateResponseMixin):
    template_name_suffix = 'delete'
    update_view_name = None

    def get_context_data(self, **kwargs):
        kwargs['object_name'] = self.model._meta.verbose_name
        kwargs['back_link'] = reverse(self.update_view_name, kwargs={'pk': self.object.pk})
        return super().get_context_data(**kwargs)


class DetailMixin:
    template_name_suffix = 'detail'

    def get_context_data(self, **kwargs):
        kwargs['title'] = '{} пользователя {}'.format(self.model._meta.verbose_name, self.object.user)
        return super().get_context_data(**kwargs)
