"""Contains all manager functions for line_item."""
from apps.orders.models.line_item import LineItem


class LineItemManager(object):
    """Manager for all line_item related functions.."""

    def load_by_id(self, pk):
        """Load line_item by pk"""
        try:
            line_item = LineItem.objects.get(pk=pk)
        except LineItem.DoesNotExist:
            line_item = None

        return line_item

    def load_by_shopify_line_item_id(self, shopify_line_item_id):
        """Load line_item by shopify_line_item_id"""
        try:
            line_item = LineItem.objects.get(shopify_line_item_id=shopify_line_item_id)
        except LineItem.DoesNotExist:
            line_item = None

        return line_item

    def load_by_customer(self, order):
        """Load all line_item for order."""
        try:
            line_item = LineItem.objects.filter(order=order)
        except LineItem.DoesNotExist:
            line_item = None

        return line_item


    def create(self, **kwargs):
        """Create line_item."""
        return LineItem.objects.create(shopify_line_item_id=kwargs['shopify_line_item_id'],
                                        variant=kwargs['variant'],
                                        product=kwargs['product'],
                                        title=kwargs['title'],
                                        quantity=kwargs['quantity'],
                                        sku=kwargs['sku'],
                                        variant_title=kwargs['variant_title'],
                                        vendor=kwargs['vendor'],
                                        fulfillment_service=kwargs['fulfillment_service'],
                                        requires_shipping=kwargs['requires_shipping'],
                                        taxable=kwargs['taxable'],
                                        gift_card=kwargs['gift_card'],
                                        name=kwargs['name'],
                                        variant_inventory_management=kwargs['variant_inventory_management'],
                                        properties=kwargs['properties'],
                                        product_exists=kwargs['product_exists'],
                                        fulfillable_quantity=kwargs['fulfillable_quantity'],
                                        grams=kwargs['grams'],
                                        price=kwargs['price'],
                                        total_discount=kwargs['total_discount'],
                                        fulfillment_status=kwargs['fulfillment_status'],
                                        price_set=kwargs['price_set'],
                                        total_discount_set=kwargs['total_discount_set'],
                                        discount_allocations=kwargs['discount_allocations'],
                                        tax_lines=kwargs['tax_lines'],
                                        order=kwargs['order'])

    def update(self, pk, **kwargs):
        """Update line_item."""
        return LineItem.objects.filter(pk=pk).update(variant=kwargs['variant'],
                                        product=kwargs['product'],
                                        title=kwargs['title'],
                                        quantity=kwargs['quantity'],
                                        sku=kwargs['sku'],
                                        variant_title=kwargs['variant_title'],
                                        vendor=kwargs['vendor'],
                                        fulfillment_service=kwargs['fulfillment_service'],
                                        requires_shipping=kwargs['requires_shipping'],
                                        taxable=kwargs['taxable'],
                                        gift_card=kwargs['gift_card'],
                                        name=kwargs['name'],
                                        variant_inventory_management=kwargs['variant_inventory_management'],
                                        properties=kwargs['properties'],
                                        product_exists=kwargs['product_exists'],
                                        fulfillable_quantity=kwargs['fulfillable_quantity'],
                                        grams=kwargs['grams'],
                                        price=kwargs['price'],
                                        total_discount=kwargs['total_discount'],
                                        fulfillment_status=kwargs['fulfillment_status'],
                                        price_set=kwargs['price_set'],
                                        total_discount_set=kwargs['total_discount_set'],
                                        discount_allocations=kwargs['discount_allocations'],
                                        tax_lines=kwargs['tax_lines'],
                                        order=kwargs['order'])
