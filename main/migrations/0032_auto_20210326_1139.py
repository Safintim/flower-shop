# Generated by Django 3.1.7 on 2021-03-26 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210326_1118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Callback',
        ),
        migrations.DeleteModel(
            name='Configuration',
        ),
    ]
