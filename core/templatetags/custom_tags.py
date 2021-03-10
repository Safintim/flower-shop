from django import template


register = template.Library()


@register.filter('get_field_name')
def get_field_name(object, field):
    verbose_name = object._meta.get_field(field).verbose_name
    return verbose_name
