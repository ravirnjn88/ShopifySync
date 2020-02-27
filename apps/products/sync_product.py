from apps.products.models import Product

def create_or_update_product(shopify_product_details):
    import pdb
    # pdb.set_trace()
    try:
        product = Product.objects.get(shopify_product_id=shopify_product_details['id'])
    except Product.DoesNotExist:
        product = None
    if product is None:
        if len(shopify_product_details['variants']) > 1:
            raise Exception("variants products not supported")
        print("Creating Product {}".format(shopify_product_details['title']))
        p = Product()
        p.shopify_product_id = shopify_product_details['id']
        p.title = shopify_product_details['title']
        p.slug = shopify_product_details['handle']
        p.description =  shopify_product_details['body_html']
        p.image =  shopify_product_details['image']['src']
        p.mrp =  shopify_product_details['variants'][0]['compare_at_price']
        p.sell_price = shopify_product_details['variants'][0]['price']
        p.sku = shopify_product_details['variants'][0]['sku']
        p.quantity = shopify_product_details['variants'][0]['inventory_quantity']

        p.save()
    else:
        print("Updating Quantity {}".format(shopify_product_details['variants'][0]['inventory_quantity']))
        product.quantity = shopify_product_details['variants'][0]['inventory_quantity']
        product.save()

    return product
