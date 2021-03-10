from django import template


register = template.Library()


@register.filter('get_field_name')
def get_field_name(object, field):
    verbose_name = object._meta.get_field(field).verbose_name
    return verbose_name


@register.simple_tag
def querystring(request, **kwargs):
    params = dict(request.GET.items())
    params.update(kwargs)

    query = '&'.join(f'{key}={value}' for key, value in params.items())
    url = request.path
    return f'{url}?{query}'
