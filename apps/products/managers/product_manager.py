# if __name__ == "__main__":
#     import sys, os, django

#     sys.path.append("/home/raviranjan/Desktop/shopifysync")
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopifysync.settings")
#     django.setup()

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

    def update(self, pk, **kwargs):
        """Update a product instance given pk."""
        return Product.objects.filter(pk=pk).update(title=kwargs['title'],
                                                  body_html=kwargs['body_html'],
                                                  vendor=kwargs['vendor'],
                                                  product_type=kwargs['product_type'],
                                                  handle=kwargs['handle'],
                                                  published_scope=kwargs['published_scope'],
                                                  admin_graphql_api_id=kwargs['admin_graphql_api_id'],
                                                  published_at=kwargs['published_at'])


    @transaction.atomic()
    def parse_and_create_product(self, json_data):
        """Parse and create product from shopify json data."""
        json_data['shopify_product_id'] = json_data['id']
        product_object = self.load_by_shopify_product_id(json_data['shopify_product_id'])
        if not product_object:
            product_object = self.create(**json_data)
        else:
            self.update(product_object.id, **json_data)

        # Update or create tags
        tags = json_data['tags'].split(",")
        for tag in tags:
            tag_object = self.tag_manager.filter_by_name_product(tag, product_object).first()
            if not tag_object:
                tag_object = self.tag_manager.create(**{'product':product_object, 'name': tag})
            else:
                self.tag_manager.update(tag_object.id, **{'product':product_object, 'name': tag})

        # Update or create Images
        images = json_data['images']
        for image in images:
            image['shopify_image_id'] = image['id']
            image['product'] = product_object
            image_object = self.images_manager.load_by_shopify_image_id(image['id'])
            if not image_object:
                image_object = self.images_manager.create(**image)
            else:
                self.images_manager.update(image_object.id, **image)

        # Update or create Options and value.
        options = json_data['options']
        for option in options:
            option['shopify_option_id'] = option['id']
            option['product'] = product_object
            option['option_name'] = option['name']
            option_object = self.option_manager.load_by_shopify_option_id(option['id'])
            if not option_object:
                print("==== creating", product_object)
                option_object = self.option_manager.create(**option)
            else:
                self.option_manager.update(option_object.id, **option)
            values = option['values']
            for value in values:
                option_value = option_object.option_value.filter(name=value).first()
                if not option_value:
                    self.option_value_manager.create(**{'name': value, 'option': option_object})


        # Update or create variant
        variants = json_data['variants']
        for variant in variants:
            variant['shopify_variant_id'] = variant['id']
            variant['product'] = product_object
            variant['title'] = "{}|{}".format(product_object.title, variant['title'])

            option1_value_name = variant['option1']
            option1_object = product_object.options.filter(position=1)
            if option1_object:
                option1_value = option1_object[0].option_value.filter(name=variant['option1']).all()[0]
                variant['option1'] = option1_value
            else:
                variant['option1'] = None

            option2_value_name = variant['option2']
            option2_object = product_object.options.filter(position=2)
            if option2_object:
                option2_value = option2_object[0].option_value.filter(name=variant['option2']).all()[0]
                variant['option2'] = option2_value
            else:
                variant['option2'] = None

            option3_value_name = variant['option3']
            option3_object = product_object.options.filter(position=3)
            if option3_object:
                option3_value = option3_object[0].option_value.filter(name=variant['option3']).all()[0]
                variant['option3'] = option3_value
            else:
                variant['option3'] = None

            image = variant["image_id"]
            if image:
                image = self.images_manager.load_by_shopify_image_id(image)
                variant['image'] = image
            else:
                variant['image'] = None

            variant_object = self.variant_manager.load_by_shopify_variant_id(variant['id'])
            if not variant_object:
                variant_object = self.variant_manager.create(**variant)
            else:
                self.variant_manager.update(variant_object.id, **variant)



# from utils.shopify_utils import ShopifyProductFetch

# json = ShopifyProductFetch().fetch_single_product(4684578422917)
# a = json['product']
# print(a)
# ProductManager().parse_and_create_product(a)