if __name__ == "__main__":
    import sys, os, django

    sys.path.append("/home/raviranjan/Desktop/shopifysync")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopifysync.settings")
    django.setup()

"""Contains all manager functions for Product."""
from django.db import transaction
from apps.products.models.product import Product
from apps.products.managers.tags_manager import TagManager
from apps.products.managers.images_manager import ImageManager
from apps.products.managers.option_manager import OptionManager
from apps.products.managers.option_value_manager import OptionValueManager
from apps.products.managers.variant_manager import VariantManager

class ProductManager(object):
    """Manager for all product related functions.."""
    
    def __init__(self):
        self.tag_manager = TagManager()
        self.images_manager = ImageManager()
        self.option_manager = OptionManager()
        self.option_value_manager = OptionValueManager()
        self.variant_manager = VariantManager()

    def load_by_id(self, pk):
        """Load product by pk"""
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            product = None

        return product

    def load_by_shopify_product_id(self, shopify_product_id):
        """Load product by shopify_product_id"""
        try:
            product = Product.objects.get(shopify_product_id=shopify_product_id)
        except Product.DoesNotExist:
            product = None

        return product

    def create(self, **kwargs):
        """Create product corresponding to a product."""
        return Product.objects.create(shopify_product_id=kwargs['shopify_product_id'],
                                      title=kwargs['title'],
                                      body_html=kwargs['body_html'],
                                      vendor=kwargs['vendor'],
                                      product_type=kwargs['product_type'],
                                      handle=kwargs['handle'],
                                      published_scope=kwargs['published_scope'],
                                      admin_graphql_api_id=kwargs['admin_graphql_api_id'],
                                      published_at=kwargs['published_at'])

    @transaction.atomic()
    def parse_and_create_product(self, json_data):
        """Parse and create order from shopify json data."""
        json_data['shopify_product_id'] = json_data['id']
        product_object = self.create(**json_data)

        tags = json_data['tags'].split(",")
        for tag in tags:
            self.tag_manager.create(**{'product':product_object, 'name': tag})

        # images = json_data['images']
        








from utils.shopify_utils import ShopifyProductFetch

json = ShopifyProductFetch().fetch_single_product(4679803076741)
a = json['product']
ProductManager().parse_and_create_product(a)