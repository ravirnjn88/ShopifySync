# Generated by Django 2.2.2 on 2020-03-07 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200307_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variable_product',
        ),
    ]