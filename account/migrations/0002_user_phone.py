# Generated by Django 3.1.7 on 2021-03-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='Номер телефона'),
        ),
    ]
