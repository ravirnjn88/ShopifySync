"""Contains all manager functions for customer."""
from apps.orders.models.customer import Customer


class CustomerManager(object):
    """Manager for all customer related functions.."""

    def load_by_id(self, pk):
        """Load customer by pk"""
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            customer = None

        return customer

    def load_by_shopify_customer_id(self, shopify_customer_id):
        """Load customer by shopify_customer_id"""
        try:
            customer = Customer.objects.get(shopify_customer_id=shopify_customer_id)
        except Customer.DoesNotExist:
            customer = None

        return customer

    def create(self, **kwargs):
        """Create Customer."""
        return Customer.objects.create(shopify_customer_id=kwargs['shopify_customer_id'],
                                        email=kwargs['email'],
                                        accepts_marketing=kwargs['accepts_marketing'],
                                        first_name=kwargs['first_name'],
                                        last_name=kwargs['last_name'],
                                        orders_count=kwargs['orders_count'],
                                        state=kwargs['state'],
                                        total_spent=kwargs['total_spent'],
                                        last_order_id=kwargs['last_order_id'],
                                        note=kwargs['note'],
                                        verified_email=kwargs['verified_email'],
                                        multipass_identifier=kwargs['multipass_identifier'],
                                        tax_exempt=kwargs['tax_exempt'],
                                        phone=kwargs['phone'],
                                        tags=kwargs['tags'],
                                        last_order_name=kwargs['last_order_name'],
                                        currency=kwargs['currency'],
                                        marketing_opt_in_level=kwargs['marketing_opt_in_level'])

    def update(self, pk, **kwargs):
        """Update customer."""
        return Customer.objects.filter(pk=pk).update(email=kwargs['email'],
                                        accepts_marketing=kwargs['accepts_marketing'],
                                        first_name=kwargs['first_name'],
                                        last_name=kwargs['last_name'],
                                        orders_count=kwargs['orders_count'],
                                        state=kwargs['state'],
                                        total_spent=kwargs['total_spent'],
                                        last_order_id=kwargs['last_order_id'],
                                        note=kwargs['note'],
                                        verified_email=kwargs['verified_email'],
                                        multipass_identifier=kwargs['multipass_identifier'],
                                        tax_exempt=kwargs['tax_exempt'],
                                        phone=kwargs['phone'],
                                        tags=kwargs['tags'],
                                        last_order_name=kwargs['last_order_name'],
                                        currency=kwargs['currency'],
                                        marketing_opt_in_level=kwargs['marketing_opt_in_level'])
