# Generated by Django 3.1.7 on 2021-04-06 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20210326_1103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created_at',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
