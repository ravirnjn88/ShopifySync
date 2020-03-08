"""Contains form for Order Line Items."""
from apps.orders.models.line_item import LineItem
from django import forms


class LineItemForm(forms.ModelForm):
    """Form for LineItem."""

    def __init__(self, *args, **kwargs):
        super(LineItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = LineItem
        fields = ('variant', 'product', 'title', 'quantity', 'sku', 'variant_title', 'vendor',  
                  'fulfillment_service', 'requires_shipping', 'taxable', 'gift_card', 'name', 'variant_inventory_management',
                  'properties', 'product_exists', 'fulfillable_quantity', 'grams', 'price', 'total_discount', 'fulfillment_status',
                  'price_set', 'total_discount_set', 'discount_allocations', 'tax_lines')
