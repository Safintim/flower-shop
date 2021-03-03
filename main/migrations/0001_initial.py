# Generated by Django 3.1.7 on 2021-03-03 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('is_add_filter', models.BooleanField(default=True, verbose_name='Добавить в фильтр')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
                ('discount', models.FloatField(default=0, verbose_name='Скидка')),
                ('categories', models.ManyToManyField(to='main.Category', verbose_name='Категории')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.color', verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Повод',
                'verbose_name_plural': 'Поводы',
            },
        ),
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
            ],
            options={
                'verbose_name': 'Букет',
                'verbose_name_plural': 'Букеты',
                'ordering': ('title',),
            },
            bases=('main.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='reasons',
            field=models.ManyToManyField(to='main.Reason', verbose_name='Поводы'),
        ),
        migrations.CreateModel(
            name='BouquetFlowerMiddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.flower', verbose_name='Цветок')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bouquet', verbose_name='Букет')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы в средних букетах',
            },
        ),
        migrations.CreateModel(
            name='BouquetFlowerBig',
            fields=[
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы в больших букетах',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.bouquetflowermiddle',),
        ),
        migrations.CreateModel(
            name='BouquetFlowerSmall',
            fields=[
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы в маленьких букетах',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.bouquetflowermiddle',),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='big_size',
            field=models.ManyToManyField(blank=True, related_name='bg_size', through='main.BouquetFlowerBig', to='main.Flower', verbose_name='Цветы'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='middle_size',
            field=models.ManyToManyField(related_name='md_size', through='main.BouquetFlowerMiddle', to='main.Flower', verbose_name='Цветы'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='small_size',
            field=models.ManyToManyField(related_name='sm_size', through='main.BouquetFlowerSmall', to='main.Flower', verbose_name='Цветы'),
        ),
    ]
