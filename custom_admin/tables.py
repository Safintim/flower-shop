import django_tables2 as tables

from main.models import Category, Reason, Color, Flower, Product


class ConfigTable:
    url_params = {'pk': tables.A('pk')}
    attrs = {'class': 'table table-hover'}


class CategoryTable(tables.Table):
    title = tables.Column(linkify=('custom_admin:category-update', ConfigTable.url_params))

    class Meta:
        model = Category
        attrs = ConfigTable.attrs
        fields = ('id', 'title', 'is_active', 'slug', 'parent')


class ReasonTable(tables.Table):
    title = tables.Column(linkify=('custom_admin:reason-update', ConfigTable.url_params))

    class Meta:
        model = Reason
        attrs = ConfigTable.attrs
        fields = ('id', 'title', 'is_active')


class ColorTable(ReasonTable):
    title = tables.Column(linkify=('custom_admin:color-update', ConfigTable.url_params))

    class Meta(ReasonTable.Meta):
        model = Color


class FlowerTable(tables.Table):
    title = tables.Column(linkify=('custom_admin:flower-update', ConfigTable.url_params))

    class Meta:
        model = Flower
        attrs = ConfigTable.attrs
        fields = ('id', 'title', 'is_active', 'price', 'is_add_filter', 'updated_at')


def get_image():
    image_url = '{% if record.small_image %} {{ record.small_image.url }} {% else %}https://via.placeholder.com/100/{% endif %}'
    update_url = '{% url "custom_admin:product-present-update" record.pk %}'
    return f'<a href={update_url}><img src="{image_url}" width=100 height="100"></a>'


class ProductTable(tables.Table):
    title = tables.Column(linkify=('custom_admin:product-bouquet-update', ConfigTable.url_params))
    image = tables.TemplateColumn(template_code=get_image(), verbose_name='Изображение', orderable=False)

    class Meta:
        model = Product
        attrs = ConfigTable.attrs
        fields = ('id', 'image', 'title', 'price', 'is_active', 'is_hit', 'is_new', 'color')
