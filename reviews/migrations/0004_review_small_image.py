# Generated by Django 3.1.7 on 2021-03-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210311_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='small_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/reviews/', verbose_name='Изображение'),
        ),
    ]
