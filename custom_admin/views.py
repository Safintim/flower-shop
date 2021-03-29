from django.views import generic


class IndexTemplateView(generic.TemplateView):
    template_name = 'custom_admin/index.html'
