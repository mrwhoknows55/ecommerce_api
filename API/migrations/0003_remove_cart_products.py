# Generated by Django 3.1.3 on 2020-11-26 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20201126_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]
