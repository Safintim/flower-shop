# Generated by Django 3.1.7 on 2021-03-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210304_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Номер телефона')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='Город')),
                ('social_link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на соц сеть')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Отзыв')),
                ('rating', models.PositiveSmallIntegerField(default=1, verbose_name='Оценка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
