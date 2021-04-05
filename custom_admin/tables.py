import django_tables2 as tables
from django.contrib.auth import get_user_model

from core.models import Callback
from main.models import Category, Reason, Color, Flower, Product
from reviews.models import Review


class ConfigTable:
    attrs = {'class': 'table table-hover'}
    common_fields = ('id', 'title', 'is_active')


class TableWithLinkifyTitle(tables.Table):
    title = tables.Column(linkify=True)


class CategoryTable(TableWithLinkifyTitle):
    class Meta:
        model = Category
        attrs = ConfigTable.attrs
        fields = ConfigTable.common_fields + ('slug', 'parent')


class ReasonTable(TableWithLinkifyTitle):
    class Meta:
        model = Reason
        attrs = ConfigTable.attrs
        fields = ConfigTable.common_fields


class ColorTable(ReasonTable):
    class Meta(ReasonTable.Meta):
        model = Color


class FlowerTable(TableWithLinkifyTitle):
    class Meta:
        model = Flower
        attrs = ConfigTable.attrs
        fields = ConfigTable.common_fields + ('price', 'is_add_filter', 'updated_at')


def get_image():
    image_url = '''
    {% if record.small_image %} {{ record.small_image.url }} {% else %}https://via.placeholder.com/100/{% endif %}'''
    update_url = '{{ record.get_absolute_url }}'
    return f'<a href={update_url}><img src="{image_url}" width=100 height="100"></a>'


class ProductTable(TableWithLinkifyTitle):
    image = tables.TemplateColumn(template_code=get_image(), verbose_name='Изображение', orderable=False)

    class Meta:
        model = Product
        attrs = ConfigTable.attrs
        fields = ('id', 'image', 'title', 'price', 'is_active', 'is_hit', 'is_new', 'color')


class ReviewTable(tables.Table):
    name = tables.Column(linkify=True)

    class Meta:
        model = Review
        fields = ('id', 'name', 'is_active', 'created_at')


class CallbackTable(tables.Table):
    phone = tables.Column(linkify=True)

    class Meta:
        model = Callback
        fields = ('id', 'phone', 'is_new', 'created_at', 'updated_at')


User = get_user_model()


class UserTable(tables.Table):
    phone = tables.Column(linkify=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'is_active', 'first_name', 'last_name', 'last_login')
