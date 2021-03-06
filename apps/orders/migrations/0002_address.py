# Generated by Django 2.2.2 on 2020-03-08 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('shopify_address_id', models.BigIntegerField(unique=True)),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('address1', models.CharField(blank=True, max_length=256)),
                ('address2', models.CharField(blank=True, max_length=256)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('province', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(blank=True, max_length=64)),
                ('zip', models.CharField(blank=True, max_length=16, null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('province_code', models.CharField(blank=True, max_length=32, null=True)),
                ('country_code', models.CharField(blank=True, max_length=32, null=True)),
                ('country_name', models.CharField(blank=True, max_length=32, null=True)),
                ('default', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='orders.Customer')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'address',
            },
        ),
    ]
