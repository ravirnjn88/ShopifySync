from django.contrib import admin
from apps.orders.forms.line_item_form import LineItemForm
from apps.orders.forms.customer_form import CustomerForm
from apps.orders.forms.address_form import AddressForm
from apps.orders.models.line_item import LineItem
from apps.orders.models.order import Order
from apps.orders.models.customer import Customer
from apps.orders.models.address import Address


import nested_admin


class LineItemInline(nested_admin.NestedStackedInline):
    """this inline class is used in Orders for showing related line items directly."""

    model = LineItem
    form = LineItemForm
    extra = 0

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

class AddressInline(nested_admin.NestedTabularInline):
    """this inline class is used in Orders for showing related customer address directly."""

    model = Address
    form = AddressForm

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class OrderInline(nested_admin.NestedTabularInline):
    """this inline class is used in Orders for showing customer directly."""

    model = Order
    # inlines = [AddressInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False



# Register your models here.
@admin.register(Order)
class OrderAdmin(nested_admin.NestedModelAdmin):
    """Registering PRoduct in admin."""

    model = Order
    inlines = [LineItemInline]
    extra = 0
    list_display = ('order_number', 'customer', 'email', 'total_price')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(OrderAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

@admin.register(Customer)
class CustomerAdmin(nested_admin.NestedModelAdmin):
    """Registering Customer"""

    model = Customer
    inlines = [OrderInline]
    list_display = ('first_name', 'last_name', 'email', 'orders_count', 'total_spent')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(CustomerAdmin, self).changeform_view(request, object_id, extra_context=extra_context)