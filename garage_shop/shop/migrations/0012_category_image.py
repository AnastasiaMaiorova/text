# Generated by Django 4.1.4 on 2023-05-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_name_product_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='media', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
