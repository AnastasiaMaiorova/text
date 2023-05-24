# Generated by Django 4.1.4 on 2023-05-11 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shop', '0002_category_product_filter_oil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(default=8, verbose_name='Итоговое количество товара')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('order_in', models.BooleanField(default=False)),
                ('user_anonym', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Продукт для корзины',
                'verbose_name_plural': 'Продукты для корзины',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='shop.productcart', verbose_name='Продукты'),
        ),
    ]
