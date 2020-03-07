"""Contains form for product Image."""
from apps.products.models.variant import Variant
from django import forms


class VariantForm(forms.ModelForm):
    """Form for Variation."""

    def __init__(self, *args, **kwargs):
        super(VariantForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Variant
        fields = ('title', 'price', 'sku', 'position', 'compare_at_price',
                  'option1', 'option2', 'option3', 'taxable', 'barcode',
                  'weight', 'weight_unit', 'image', 'inventory_quantity',
                  'requires_shipping')
