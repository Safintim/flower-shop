# Generated by Django 3.1.7 on 2021-03-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20210326_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Слаг'),
        ),
    ]
