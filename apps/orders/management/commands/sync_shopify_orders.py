"""Sync Orders"""
from django.core.management import BaseCommand
from utils.shopify_utils import ShopifyOrderFetch
from apps.orders.managers.order_manager import OrderManager

class Command(BaseCommand):
    """Command to fetch shopify Orders one time."""

    def __init__(self, *args, **kwargs):
        """init method where all the managers are initialized for the command."""
        super(Command, self).__init__(*args, **kwargs)
        self.order_manager = OrderManager()
        

    def handle(self, *args, **options):
        """handling the command begins here."""
        all_orders = ShopifyOrderFetch().fetch_all_orders()
        orders = all_orders['orders']
        for order in orders:
        	self.order_manager.parse_and_create_order(order)
       
