"""Sync products"""
from django.core.management import BaseCommand
from utils.shopify_functions import get_allshopify_products
from apps.products.sync_product import create_or_update_product
import json

class Command(BaseCommand):
    """Command to populate lab data."""

    def __init__(self, *args, **kwargs):
        """init method where all the managers are initialized for the command."""
        super(Command, self).__init__(*args, **kwargs)
        

    def handle(self, *args, **options):
        """handling the command begins here."""
        all_products = get_allshopify_products()
        products = all_products['products']
        for product in products:
        	# print(product)
            create_or_update_product(product)
       
