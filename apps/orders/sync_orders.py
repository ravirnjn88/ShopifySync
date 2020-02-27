from apps.orders.models import Order, OrderProduct
from apps.products.models import Product
from django.db import transaction

@transaction.atomic()
def create_order(shopify_order_details):
    import pdb
    # pdb.set_trace()
    # order = Order.objects.get(shopify_order_id=shopify_order_details['id'])
    try:
        order = Order.objects.get(shopify_order_id=shopify_order_details['id'])
    except:
        order = None
    if order is None:
        print("Creating Product {}".format(shopify_order_details['name']))
        order_object = Order()
        order_object.shopify_order_id = shopify_order_details['id']
        order_object.order_number = shopify_order_details['name']
        order_object.customer_name = shopify_order_details['billing_address']['first_name']
        order_object.save()

        for item in shopify_order_details['line_items']:
            product_id = item['product_id']
            product = Product.objects.get(shopify_product_id=product_id)
            op = OrderProduct()
            op.order = order_object
            op.product = product
            op.save()

    else:
        print("Order Already Exist {}".format(shopify_order_details['id']))
