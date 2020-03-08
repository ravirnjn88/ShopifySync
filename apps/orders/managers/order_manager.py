"""Contains all manager functions for order."""
from apps.orders.models.order import Order
from apps.orders.managers.address_manager import AddressManager
from apps.orders.managers.customer_manager import CustomerManager
from apps.orders.managers.line_item_manager import LineItemManager
from apps.products.managers.variant_manager import VariantManager
from apps.products.managers.product_manager import ProductManager
from django.db import transaction


class OrderManager(object):
    """Manager for all order related functions.."""

    def __init__(self):
        self.address_manager = AddressManager()
        self.customer_manager = CustomerManager()
        self.line_item_manager = LineItemManager()
        self.variant_manager = VariantManager()
        self.product_manager = ProductManager()

    def load_by_id(self, pk):
        """Load order by pk"""
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            order = None

        return order

    def load_by_shopify_order_id(self, shopify_order_id):
        """Load order by shopify_order_id"""
        try:
            order = Order.objects.get(shopify_order_id=shopify_order_id)
        except Order.DoesNotExist:
            order = None

        return order

    def load_by_customer(self, order):
        """Load all order for order."""
        try:
            order = Order.objects.filter(order=order)
        except Order.DoesNotExist:
            order = None

        return order


    def create(self, **kwargs):
        """Create order."""
        return Order.objects.create(shopify_order_id=kwargs['shopify_order_id'],
                                        email=kwargs['email'],
                                        closed_at=kwargs['closed_at'],
                                        number=kwargs['number'],
                                        note=kwargs['note'],
                                        gateway=kwargs['gateway'],
                                        test=kwargs['test'],
                                        total_price=kwargs['total_price'],
                                        subtotal_price=kwargs['subtotal_price'],
                                        total_weight=kwargs['total_weight'],
                                        total_tax=kwargs['total_tax'],
                                        taxes_included=kwargs['taxes_included'],
                                        currency=kwargs['currency'],
                                        financial_status=kwargs['financial_status'],
                                        confirmed=kwargs['confirmed'],
                                        total_discounts=kwargs['total_discounts'],
                                        total_line_items_price=kwargs['total_line_items_price'],
                                        cart_token=kwargs['cart_token'],
                                        buyer_accepts_marketing=kwargs['buyer_accepts_marketing'],
                                        name=kwargs['name'],
                                        referring_site=kwargs['referring_site'],
                                        landing_site=kwargs['landing_site'],
                                        cancelled_at=kwargs['cancelled_at'],
                                        cancel_reason=kwargs['cancel_reason'],
                                        total_price_usd=kwargs['total_price_usd'],
                                        order_number=kwargs['order_number'],
                                        discount_applications=kwargs['discount_applications'],
                                        discount_codes=kwargs['discount_codes'],
                                        note_attributes=kwargs['note_attributes'],
                                        payment_gateway_names=kwargs['payment_gateway_names'],
                                        processing_method=kwargs['processing_method'],
                                        source_name=kwargs['source_name'],
                                        fulfillment_status=kwargs['fulfillment_status'],
                                        tax_lines=kwargs['tax_lines'],
                                        tags=kwargs['tags'],
                                        contact_email=kwargs['contact_email'],
                                        billing_address=kwargs['billing_address'],
                                        shipping_address=kwargs['shipping_address'],
                                        customer=kwargs['customer'])

    def update(self, pk, **kwargs):
        """Update order."""
        return Order.objects.filter(pk=pk).update(email=kwargs['email'],
                                        closed_at=kwargs['closed_at'],
                                        number=kwargs['number'],
                                        note=kwargs['note'],
                                        gateway=kwargs['gateway'],
                                        test=kwargs['test'],
                                        total_price=kwargs['total_price'],
                                        subtotal_price=kwargs['subtotal_price'],
                                        total_weight=kwargs['total_weight'],
                                        total_tax=kwargs['total_tax'],
                                        taxes_included=kwargs['taxes_included'],
                                        currency=kwargs['currency'],
                                        financial_status=kwargs['financial_status'],
                                        confirmed=kwargs['confirmed'],
                                        total_discounts=kwargs['total_discounts'],
                                        total_line_items_price=kwargs['total_line_items_price'],
                                        cart_token=kwargs['cart_token'],
                                        buyer_accepts_marketing=kwargs['buyer_accepts_marketing'],
                                        name=kwargs['name'],
                                        referring_site=kwargs['referring_site'],
                                        landing_site=kwargs['landing_site'],
                                        cancelled_at=kwargs['cancelled_at'],
                                        cancel_reason=kwargs['cancel_reason'],
                                        total_price_usd=kwargs['total_price_usd'],
                                        order_number=kwargs['order_number'],
                                        discount_applications=kwargs['discount_applications'],
                                        discount_codes=kwargs['discount_codes'],
                                        note_attributes=kwargs['note_attributes'],
                                        payment_gateway_names=kwargs['payment_gateway_names'],
                                        processing_method=kwargs['processing_method'],
                                        source_name=kwargs['source_name'],
                                        fulfillment_status=kwargs['fulfillment_status'],
                                        tax_lines=kwargs['tax_lines'],
                                        tags=kwargs['tags'],
                                        contact_email=kwargs['contact_email'],
                                        billing_address=kwargs['billing_address'],
                                        shipping_address=kwargs['shipping_address'],
                                        customer=kwargs['customer'])

    @transaction.atomic()
    def parse_and_create_order(self, json_data):
        """Parse and create order from shopify json data."""

        # Update or create customer
        customer_json = json_data['customer']
        customer_json['shopify_customer_id'] = customer_json['id']
        customer_object = self.customer_manager.load_by_shopify_customer_id(customer_json['id'])
        if not customer_object:
            customer_object = self.customer_manager.create(**customer_json)
        else:
            self.customer_manager.update(customer_object.id, **customer_json)

        # Update or Create Address
        address_json = customer_json['default_address']
        address_json['shopify_address_id'] = address_json['id']
        address_json['customer'] = customer_object
        address_object = self.address_manager.load_by_shopify_address_id(address_json['shopify_address_id'])

        if not address_object:
            address_object = self.address_manager.create(**address_json)
        else:
            self.address_manager.update(address_object.id, **address_json)

        # Update or create Order
        json_data['shopify_order_id'] = json_data['id']
        json_data['customer'] = customer_object
        order_object = self.load_by_shopify_order_id(shopify_order_id=json_data['shopify_order_id'])
        if not order_object:
            order_object = self.create(**json_data)
        else:
            self.update(order_object.id, **json_data)

        # Update Line Items
        line_items = json_data['line_items']
        for item in line_items:
            item['shopify_line_item_id'] = item['id']
            item['variant'] = self.variant_manager.load_by_shopify_variant_id(item['variant_id'])
            item['product'] = self.product_manager.load_by_shopify_product_id(item['product_id'])
            item['order'] = order_object
            
            item_object = self.line_item_manager.load_by_shopify_line_item_id(item['id'])
            if not item_object:
                item_object = self.line_item_manager.create(**item)
            else:
                self.line_item_manager.update(item_object.id, **item)
