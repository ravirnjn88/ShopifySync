"""Contains all manager functions for Address."""
from apps.orders.models.address import Address


class AddressManager(object):
    """Manager for all address related functions.."""

    def load_by_id(self, pk):
        """Load address by pk"""
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            address = None

        return address

    def load_by_shopify_address_id(self, shopify_address_id):
        """Load address by shopify_address_id"""
        try:
            address = Address.objects.get(shopify_address_id=shopify_address_id)
        except Address.DoesNotExist:
            address = None

        return address


    def load_by_customer(self, customer):
        """Load all addresss for customer."""
        try:
            address = Address.objects.filter(customer=customer)
        except Address.DoesNotExist:
            address = None

        return address

    def create(self, **kwargs):
        """Create address corresponding to a Customer."""
        return Address.objects.create(shopify_address_id=kwargs['shopify_address_id'],
                                        first_name=kwargs['first_name'],
                                        last_name=kwargs['last_name'],
                                        company=kwargs['company'],
                                        address1=kwargs['address1'],
                                        address2=kwargs['address2'],
                                        city=kwargs['city'],
                                        province=kwargs['province'],
                                        country=kwargs['country'],
                                        zip=kwargs['zip'],
                                        phone=kwargs['phone'],
                                        province_code=kwargs['province_code'],
                                        country_code=kwargs['country_code'],
                                        country_name=kwargs['country_name'],
                                        default=kwargs['default'],
                                        customer=kwargs['customer'])

    def update(self, pk, **kwargs):
        """Update address corresponding to a Customer."""
        return Address.objects.filter(pk=pk).update(first_name=kwargs['first_name'],
                                        last_name=kwargs['last_name'],
                                        company=kwargs['company'],
                                        address1=kwargs['address1'],
                                        address2=kwargs['address2'],
                                        city=kwargs['city'],
                                        province=kwargs['province'],
                                        country=kwargs['country'],
                                        zip=kwargs['zip'],
                                        phone=kwargs['phone'],
                                        province_code=kwargs['province_code'],
                                        country_code=kwargs['country_code'],
                                        country_name=kwargs['country_name'],
                                        default=kwargs['default'],
                                        customer=kwargs['customer'])
