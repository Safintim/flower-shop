# Generated by Django 3.1.7 on 2021-03-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='social_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на соц сеть'),
        ),
    ]