"""Contains all manager functions for Product tags."""
from apps.products.models.tags import Tag


class TagManager(object):
    """Manager for all product tag related functions.."""

    def load_by_id(self, pk):
        """Load tag by pk"""
        try:
            tag = Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            tag = None

        return tag

    def load_by_product(self, product):
        """Load all tag for product."""
        try:
            tag = Tag.objects.filter(product=product)
        except Tag.DoesNotExist:
            tag = None

        return tag

    def filter_by_name_product(self, name, product):
        try:
            tag = Tag.objects.filter(name=name, product=product)
        except Tag.DoesNotExist:
            tag = None
        return tag

    def create(self, **kwargs):
        """Create tag corresponding to a product."""
        return Tag.objects.create(name=kwargs['name'], product=kwargs['product'])

    def update(self, pk, **kwargs):
        """Update tag corresponding to a product."""
        return Tag.objects.filter(pk=pk).update(name=kwargs['name'])