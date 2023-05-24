# Generated by Django 4.1.4 on 2023-05-11 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255, verbose_name='Наименование')),
                ('artikul', models.CharField(max_length=255, verbose_name='Артикул')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='media', verbose_name='Фотография')),
                ('description', models.TextField(null=True, verbose_name='Описание товара')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Производитель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтра',
            },
            bases=('shop.product',),
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('valume', models.CharField(max_length=255, verbose_name='Объем')),
            ],
            options={
                'verbose_name': 'Масло',
                'verbose_name_plural': 'Масла',
            },
            bases=('shop.product',),
        ),
    ]