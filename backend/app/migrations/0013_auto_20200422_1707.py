# Generated by Django 3.0.5 on 2020-04-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200412_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basebouquet',
            name='color',
            field=models.CharField(blank=True, choices=[('SOFT', 'Нежный'), ('BRIGHT', 'Яркий')], default=None, max_length=6, null=True, verbose_name='Цвет'),
        ),
    ]
