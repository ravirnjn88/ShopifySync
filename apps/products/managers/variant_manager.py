"""Contains all manager functions for Product Variant."""
from apps.products.models.variant import Variant


class VariantManager(object):
    """Manager for all product variant related finctions.."""

    def load_by_id(self, pk):
        """Load variant by pk"""
        try:
            variant = Variant.objects.get(pk=pk)
        except Variant.DoesNotExist:
            variant = None

        return variant

    def load_by_shopify_variant_id(self, shopify_variant_id):
        """Load variant by shopify_variant_id"""
        try:
            variant = Variant.objects.get(shopify_variant_id=shopify_variant_id)
        except Variant.DoesNotExist:
            variant = None

        return variant


    def load_by_product(self, product):
        """Load all variants for product."""
        try:
            variants = Variant.objects.filter(product=product)
        except Variant.DoesNotExist:
            variants = None

        return variants

    def create(self, **kwargs):
        """Create variant corresponding to a product."""
        return Variant.objects.create(shopify_variant_id=kwargs['shopify_variant_id'],
                                        product=kwargs['product'],
                                        title=kwargs['title'],
                                        price=kwargs['price'],
                                        sku=kwargs['sku'],
                                        position=kwargs['position'],
                                        inventory_policy=kwargs['inventory_policy'],
                                        compare_at_price=kwargs['compare_at_price'],
                                        fulfillment_service=kwargs['fulfillment_service'],
                                        inventory_management=kwargs['inventory_management'],
                                        option1=kwargs['option1'],
                                        option2=kwargs['option2'],
                                        option3=kwargs['option3'],
                                        taxable=kwargs['taxable'],
                                        barcode=kwargs['barcode'],
                                        weight=kwargs['weight'],
                                        weight_unit=kwargs['weight_unit'],
                                        image=kwargs['image'],
                                        inventory_quantity=kwargs['inventory_quantity'],
                                        requires_shipping=kwargs['requires_shipping'])

    def update(self, pk, **kwargs):
        """U vpdateariant corresponding to a product."""
        return Variant.objects.filter(pk=pk).update( product=kwargs['product'],
                                        title=kwargs['title'],
                                        price=kwargs['price'],
                                        sku=kwargs['sku'],
                                        position=kwargs['position'],
                                        inventory_policy=kwargs['inventory_policy'],
                                        compare_at_price=kwargs['compare_at_price'],
                                        fulfillment_service=kwargs['fulfillment_service'],
                                        inventory_management=kwargs['inventory_management'],
                                        option1=kwargs['option1'],
                                        option2=kwargs['option2'],
                                        option3=kwargs['option3'],
                                        taxable=kwargs['taxable'],
                                        barcode=kwargs['barcode'],
                                        weight=kwargs['weight'],
                                        weight_unit=kwargs['weight_unit'],
                                        image=kwargs['image'],
                                        inventory_quantity=kwargs['inventory_quantity'],
                                        requires_shipping=kwargs['requires_shipping'])