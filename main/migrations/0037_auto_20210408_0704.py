# Generated by Django 3.1.7 on 2021-04-08 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20210401_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]