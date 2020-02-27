"""Sync Orders"""
from django.core.management import BaseCommand
from utils.shopify_functions import get_allshopify_orders
from apps.orders.sync_orders import create_order

class Command(BaseCommand):
    """Command to populate lab data."""

    def __init__(self, *args, **kwargs):
        """init method where all the managers are initialized for the command."""
        super(Command, self).__init__(*args, **kwargs)
        

    def handle(self, *args, **options):
        """handling the command begins here."""
        all_orders = get_allshopify_orders()
        orders = all_orders['orders']
        for order in orders:
        	# print(product)
            create_order(order)
       
