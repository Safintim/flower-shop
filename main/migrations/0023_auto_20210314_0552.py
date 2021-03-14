# Generated by Django 3.1.7 on 2021-03-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210314_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='big_image',
            field=models.ImageField(help_text='Размер 640x640', upload_to='static/uploads/images/', verbose_name='Изображение(большое)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_image',
            field=models.ImageField(help_text='Размер 372х372', upload_to='static/uploads/images/', verbose_name='Изображение(маленькое)'),
        ),
    ]