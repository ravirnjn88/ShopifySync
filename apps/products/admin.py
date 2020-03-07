from django.contrib import admin
from apps.products.models.product import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Registering Order in admin."""

    model = Product