"""Contains form for product option value."""
from apps.products.models.option_value import OptionValue
from django import forms


class OptionValueForm(forms.ModelForm):
    """Form for Option Value."""

    def __init__(self, *args, **kwargs):
        super(OptionValueForm, self).__init__(*args, **kwargs)

    class Meta:
        model = OptionValue
        fields = ('name',)
