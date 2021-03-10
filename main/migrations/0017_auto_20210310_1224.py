# Generated by Django 3.1.7 on 2021-03-10 12:24

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_category_parent'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('active', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
    ]
