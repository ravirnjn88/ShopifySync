# Generated by Django 2.2.2 on 2020-03-07 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200307_1621'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='option',
            unique_together={('product_id', 'option_name'), ('product_id', 'position')},
        ),
    ]
