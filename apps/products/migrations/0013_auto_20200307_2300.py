# Generated by Django 2.2.2 on 2020-03-07 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200307_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='shopify_varient_id',
            new_name='shopify_variant_id',
        ),
    ]
