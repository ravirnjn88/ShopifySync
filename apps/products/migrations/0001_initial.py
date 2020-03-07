# Generated by Django 2.2.2 on 2020-03-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('shopify_id', models.BigIntegerField(unique=True)),
                ('title', models.CharField(max_length=500)),
                ('body_html', models.TextField()),
                ('vendor', models.CharField(max_length=200)),
                ('product_type', models.CharField(max_length=200)),
                ('handle', models.CharField(max_length=500)),
                ('published_scope', models.CharField(max_length=200)),
                ('admin_graphql_api_id', models.CharField(max_length=200)),
                ('published_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]
