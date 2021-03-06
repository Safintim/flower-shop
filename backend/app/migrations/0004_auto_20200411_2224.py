# Generated by Django 3.0.5 on 2020-04-11 22:24

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200411_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='basebouquet',
            name='category',
            field=mptt.fields.TreeManyToManyField(blank=True, db_index=True, to='app.Category', verbose_name='Категории'),
        ),
    ]
