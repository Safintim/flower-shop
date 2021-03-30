import django_tables2 as tables

from main.models import Category


class ConfigTable:
    url_params = {'pk': tables.A('pk')}
    attrs = {'class': 'table table-hover'}


class CategoryTable(tables.Table):
    title = tables.Column(linkify=('custom_admin:category-update', ConfigTable.url_params))

    class Meta:
        model = Category
        attrs = ConfigTable.attrs
        fields = ('id', 'title', 'is_active', 'slug', 'parent')

