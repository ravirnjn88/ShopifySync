"""Contains form for Customer."""
from apps.orders.models.customer import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    """Form for Customer."""

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Customer
        fields = ('email', 'accepts_marketing', 'first_name', 'last_name', 'orders_count',
                  'state', 'total_spent', 'last_order_id', 'note', 'verified_email',
                  'multipass_identified', 'tax_exempt', 'phone', 'tags', 'last_order_name',
                  'currency', 'marketing_opt_in_level')
