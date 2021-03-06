# Generated by Django 3.1.3 on 2020-11-26 18:21

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentMethod', models.CharField(max_length=20, null=True)),
                ('finalAmount', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True)),
                ('orderState', models.CharField(max_length=15, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('paymentMethod', models.CharField(max_length=20, null=True)),
                ('finalAmount', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of product', max_length=200)),
                ('price', models.PositiveBigIntegerField(default=0, help_text='Price of Product')),
                ('manufacturer', models.CharField(default='', help_text='Name of manufacturer', max_length=200)),
                ('thumbnails', models.CharField(blank=True, default='', help_text='Paste link of thumbnail photo', max_length=300)),
                ('stock', models.PositiveBigIntegerField(default=0, help_text='Available quantity of product')),
                ('isInStock', models.BooleanField(default=False, help_text='is product available for purchases?')),
                ('paymentOption', models.CharField(default='Cash On Delivery (C.O.D.)', help_text="What's the payment options available on product", max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('product_id', models.OneToOneField(help_text='Select product ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='API.product')),
                ('description', models.TextField(default='', help_text='Description of the product')),
                ('countryOfOrigin', models.CharField(default=None, help_text="What's the Country of Origin", max_length=20)),
                ('photos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=450), blank=True, default=None, help_text='Paste links for the photos of products separated by commas', size=None)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=20), blank=True, default=None, help_text='Define category of product', size=None)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, help_text='rating out of 5', max_digits=5)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, help_text='how much discount is ongoing for product (in %)', max_digits=12)),
                ('coupons', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=20), blank=True, default=None, help_text='coupon codes for this product separated by commas', size=None)),
            ],
        ),
        migrations.CreateModel(
            name='QuantityProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_quantity', models.PositiveIntegerField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.product')),
            ],
        ),
    ]
