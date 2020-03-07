"""Contains all manager functions for Product Images."""
from apps.products.models.images import Image


class ImageManager(object):
    """Manager for all product image related finctions.."""

    def load_by_id(self, pk):
        """Load image by pk"""
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            image = None

        return image

    def load_by_shopify_image_id(self, shopify_image_id):
        """Load image by shopify_image_id"""
        try:
            image = Image.objects.get(shopify_image_id=shopify_image_id)
        except Image.DoesNotExist:
            image = None

        return image


    def load_by_product(self, product):
        """Load all Images for product."""
        try:
            images = Image.objects.filter(product=product)
        except Image.DoesNotExist:
            images = None

        return images

    def create(self, **kwargs):
        """Create image corresponding to a product."""
        return Image.objects.create(shopify_image_id=kwargs['shopify_image_id'],
                                        product=kwargs['product'],
                                        position=kwargs['position'],
                                        src=kwargs['src'],
                                        admin_graphql_api_id=kwargs['admin_graphql_api_id'],
                                        alt=kwargs['alt'],
                                        width=kwargs['width'],
                                        height=kwargs['height'])
