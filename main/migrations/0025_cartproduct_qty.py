# Generated by Django 3.1.7 on 2021-03-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_callback'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='qty',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='Количество'),
        ),
    ]
