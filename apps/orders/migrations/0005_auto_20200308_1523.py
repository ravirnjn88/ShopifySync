# Generated by Django 2.2.2 on 2020-03-08 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_lineitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='shopify_cusomer_id',
            new_name='shopify_customer_id',
        ),
    ]
