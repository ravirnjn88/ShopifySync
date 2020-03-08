"""Contains form for product Image."""
from apps.orders.models.address import Address
from django import forms


class AddressForm(forms.ModelForm):
    """Form for Address."""

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Address
        fields = ('first_name', 'last_name', 'phone', 'address1',
                  'address2', 'city', 'country', 'zip')
