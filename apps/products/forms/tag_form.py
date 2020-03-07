"""Contains form for product tags."""
from apps.products.models.tags import Tag
from django import forms


class TagForm(forms.ModelForm):
    """Form for Tags."""

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Tag
        fields = ('name',)
