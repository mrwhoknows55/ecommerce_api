# Generated by Django 3.1.3 on 2020-12-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_product_productslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productSlug',
            field=models.SlugField(default='', max_length=500, unique=True),
        ),
    ]