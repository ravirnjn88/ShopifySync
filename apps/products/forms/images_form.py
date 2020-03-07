"""Contains form for product Image."""
from apps.products.models.images import Image
from django import forms


class ImageForm(forms.ModelForm):
    """Form for Images."""

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Image
        fields = ('position', 'src')
