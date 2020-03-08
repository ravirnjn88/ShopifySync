"""Sync Orders"""
from django.core.management import BaseCommand
from utils.shopify_utils import ShopifyProductFetch
from apps.products.managers.product_manager import ProductManager

class Command(BaseCommand):
    """Command to fetch shopify products one time."""

    def __init__(self, *args, **kwargs):
        """init method where all the managers are initialized for the command."""
        super(Command, self).__init__(*args, **kwargs)
        self.product_manager = ProductManager()
        

    def handle(self, *args, **options):
        """handling the command begins here."""
        all_products = ShopifyProductFetch().fetch_all_products()
        products = all_products['products']
        for product in products:
            self.product_manager.parse_and_create_product(product)
