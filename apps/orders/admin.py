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
    # fields = ('position', 'src', 'width', 'height', 'alt')
    # readonly_fields = ('position', 'src', 'width', 'height', 'alt')
    # extra = 0

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


class AddressInline(nested_admin.NestedTabularInline):
    """this inline class is used in Orders for showing related customer address directly."""

    model = Address
    form = AddressForm
    # fields = ('name',)
    # readonly_fields = ('name',)
    # extra = 0

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


class CustomerInline(nested_admin.NestedTabularInline):
    """this inline class is used in Orders for showing customer directly."""

    model = Customer
    form = CustomerForm
    # fields = ('option_name', 'position')
    # readonly_fields = ('option_name', 'position')
    inlines = [AddressInline]
    # extra = 0

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False



# Register your models here.
@admin.register(Order)
class OrderAdmin(nested_admin.NestedModelAdmin):
    """Registering PRoduct in admin."""

    model = Order
    inlines = [LineItemInline]
    extra = 0
    # read_only = True
    # fields = ('__all__',)
    # readonly_fields = ('shopify_product_id', 'title', 'body_html', 'vendor', 'product_type',
    #           'handle', 'published_scope', 'admin_graphql_api_id', 'published_at')

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(OrderAdmin, self).changeform_view(request, object_id, extra_context=extra_context)