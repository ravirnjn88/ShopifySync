"""Contains all manager functions for Product option value."""
from apps.products.models.option_value import OptionValue


class OptionValueManager(object):
    """Manager for all product option value related functions.."""

    def load_by_id(self, pk):
        """Load option_value by pk"""
        try:
            option_value = OptionValue.objects.get(pk=pk)
        except OptionValue.DoesNotExist:
            option_value = None

        return option_value

    def load_by_option(self, option):
        """Load all option value for option."""
        try:
            option_value = OptionValue.objects.filter(option=option)
        except OptionValue.DoesNotExist:
            option_value = None

        return option_value

    def create(self, **kwargs):
        """Create option value corresponding to a option."""
        return OptionValue.objects.create(name=kwargs['name'], option=kwargs['option'])
