# Generated by Django 3.1.7 on 2021-03-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20210326_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Активно'),
        ),
        migrations.AddField(
            model_name='flower',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Активно'),
        ),
        migrations.AddField(
            model_name='reason',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Активно'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Активно'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Активно'),
        ),
    ]
