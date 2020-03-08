"""Contains all manager functions for Product option."""
from apps.products.models.option import Option


class OptionManager(object):
    """Manager for all product option related functions.."""

    def load_by_id(self, pk):
        """Load option by pk"""
        try:
            option = Option.objects.get(pk=pk)
        except Option.DoesNotExist:
            option = None

        return option

    def load_by_shopify_option_id(self, shopify_option_id):
        """Load option by shopify_option_id"""
        try:
            option = Option.objects.get(shopify_option_id=shopify_option_id)
        except Option.DoesNotExist:
            option = None

        return option


    def load_by_product(self, product):
        """Load all option for product."""
        try:
            option = Option.objects.filter(product=product)
        except Option.DoesNotExist:
            option = None

        return option

    def create(self, **kwargs):
        """Create option corresponding to a product."""
        return Option.objects.create(shopify_option_id=kwargs['shopify_option_id'],
                                        product=kwargs['product'],
                                        position=kwargs['position'],
                                        option_name=kwargs['option_name'])

    def update(self, pk, **kwargs):
        """Update option corresponding to a product."""
        return Option.objects.filter(pk=pk).update(product=kwargs['product'],
                                        position=kwargs['position'],
                                        option_name=kwargs['option_name'])
