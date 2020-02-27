from django.contrib import admin
from apps.orders.models import OrderProduct, Order

# Register your models here.

class OrderProductsInline(admin.TabularInline):
    """Used to Show order products inline."""

    model = OrderProduct
    fields = ['product']

    def has_add_permission(self, request):
        """Removing add permission."""
        return False

    def has_delete_permission(self, request, obj=None):
        """Removing delete permission."""
        return False

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Registering Order in admin."""

    model = Order
    inlines = [OrderProductsInline]