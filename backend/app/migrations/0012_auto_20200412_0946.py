# Generated by Django 3.0.5 on 2020-04-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_flower_is_add_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basebouquet',
            name='reason',
            field=models.ManyToManyField(blank=True, to='app.Reason', verbose_name='Поводы'),
        ),
    ]
