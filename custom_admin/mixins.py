from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
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


class CustomSuccessMessageMixin(SuccessMessageMixin):
    success_message_suffix = None

    def get_success_message(self, cleaned_data=None):
        model_name = self.model._meta.verbose_name
        return f'{model_name} №{self.object.pk} успешно {self.success_message_suffix}'


class ActionMixin:
    model = None
    namespace = 'custom_admin'
    show_button_delete = True
    show_button_create = True

    def get_model_name(self):
        return self.model.__name__.lower()

    def get_action_kwargs(self):
        return {'pk': self.object.pk}

    def get_prefix_url(self):
        part = f'{self.namespace}:{self.get_model_name()}'
        return part + '{}'

    def get_delete_action(self):
        if self.show_button_delete:
            return reverse(self.get_prefix_url().format('-delete'), kwargs=self.get_action_kwargs())

    def get_create_action(self):
        if self.show_button_create:
            return reverse(self.get_prefix_url().format('-create'))

    def get_list_action(self):
        return reverse(self.get_prefix_url().format('-list'))

    def get_update_action(self):
        return reverse(self.get_prefix_url().format('-update'), kwargs=self.get_action_kwargs())

    def get_context_data(self, **kwargs):
        kwargs['show_button_create'] = self.show_button_create
        kwargs['show_button_delete'] = self.show_button_delete
        return super().get_context_data(**kwargs)


class FilteredSingleTableView(ActionMixin, BaseTemplateResponseMixin, SingleTableMixin, FilterView):
    template_name_suffix = 'list'
    form_helper_class = None
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
        kwargs['create_url'] = self.get_create_action()
        return super().get_context_data(**kwargs)


class CreateUpdateMixin(ActionMixin, BaseTemplateResponseMixin):
    template_name_suffix = 'edit'
    fields = '__all__'
    form_helper_class = CreateUpdateFormHelper
    is_update_view = True

    def get_form_helper_extra_kwargs(self):
        return {
            'is_update': self.is_update_view
        }

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class()
        helper = self.form_helper_class(
            form=form,
            delete_action=self.get_delete_action(),
            **self.get_form_helper_extra_kwargs()
        )
        form_class.helper = property(lambda _: helper)
        return form_class(**self.get_form_kwargs())

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return self.get_update_action()

    def form_valid(self, form):
        self.object = form.save()
        if 'continue' in self.request.POST:
            return HttpResponseRedirect(self.get_success_url())
        elif 'save' in self.request.POST:
            return HttpResponseRedirect(self.get_list_action())


class CreateMixin(CustomSuccessMessageMixin, CreateUpdateMixin):
    success_message_suffix = 'создан'
    show_button_delete = False
    is_update_view = False


class UpdateMixin(CustomSuccessMessageMixin, CreateUpdateMixin):
    success_message_suffix = 'обновлен'


class DeleteMixin(ActionMixin, CustomSuccessMessageMixin, BaseTemplateResponseMixin):
    success_message_suffix = 'удален'
    template_name_suffix = 'delete'

    def get_context_data(self, **kwargs):
        kwargs['object_name'] = self.model._meta.verbose_name
        kwargs['back_link'] = self.get_update_action()
        return super().get_context_data(**kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        success_message = self.get_success_message()
        self.object.delete()
        messages.success(request, success_message)
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return self.get_list_action()


class DetailMixin:
    template_name_suffix = 'detail'

    def get_context_data(self, **kwargs):
        kwargs['title'] = '{} пользователя {}'.format(self.model._meta.verbose_name, self.object.user)
        return super().get_context_data(**kwargs)
