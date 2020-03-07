"""Contains form for product Image."""
from apps.products.models.option import Option
from django import forms


class OptionForm(forms.ModelForm):
    """Form for OPtion."""

    def __init__(self, *args, **kwargs):
        super(OptionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Option
        fields = ('option_name', 'position')
