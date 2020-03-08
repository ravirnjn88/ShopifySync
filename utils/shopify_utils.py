# if __name__ == "__main__":
#     import sys, os, django

#     sys.path.append("/home/raviranjan/Desktop/shopifysync")
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopifysync.settings")
#     django.setup()

import requests
from utils import config
from utils.constants import SHOPIFY_BASE_URL, SHOPIFY_ALL_PRODUCTS_DATA_SUFFIX, SHOPIFY_SINGLE_PRODUCT_DATA_SUFFIX
from utils.constants import SHOPIFY_SINGLE_PRODUCT_ALL_VARIANT_SUFFIX, SHOPIFY_SINGLE_VARIANT_SUFFIX
from utils.constants import SHOPIFY_ALL_CUSTOMER_SUFFIX, SHOPIFY_SINGLE_CUSTOMER_SUFFIX
from utils.constants import SHOPIFY_ALL_ORDERS_SUFFIX, SHOPIFY_SINGLE_order_SUFFIX


class ShopifyBaseRequest:

    def __init__(self):
        self.headers = {'X-Shopify-Access-Token': config.get('shopify', 'api_password')}


    def make_request(self, request_type, url, headers={}, payload={}):
        """Wrapper for makig GET and POST authnticated request to Shopify."""

        assert request_type in ['GET', 'POST'], "Only GET and POST request Supported"
        headers.update(self.headers)
        if request_type == "GET":
            response = requests.get(url, headers=headers, params=payload)
        if request_type == "POST":
            response = requests.post(url, headers=headers, data=payload)

        return response


class ShopifyProductFetch(ShopifyBaseRequest):
    """Fetch Product Details."""

    def __init__(self, base_url=SHOPIFY_BASE_URL):
        super(ShopifyProductFetch, self).__init__()
        self.base_url = SHOPIFY_BASE_URL


    def fetch_all_products(self):
        url = "{}{}".format(self.base_url, SHOPIFY_ALL_PRODUCTS_DATA_SUFFIX)

        response = self.make_request("GET", url)

        return response.json()

    def fetch_single_product(self, shopify_product_id):
        url = "{}{}".format(self.base_url, SHOPIFY_SINGLE_PRODUCT_DATA_SUFFIX)
        url = url.format(product_id=shopify_product_id)
        
        response = self.make_request("GET", url)

        return response.json()

    def fetch_single_variant(self, shopify_variant_id):
        url = "{}{}".format(self.base_url, SHOPIFY_SINGLE_VARIANT_SUFFIX)
        url = url.format(variant_id=shopify_variant_id)
        
        response = self.make_request("GET", url)

        return response.json()


class ShopifyOrderFetch(ShopifyBaseRequest):
    """Fetch order details"""

    def __init__(self, base_url=SHOPIFY_BASE_URL):
        super(ShopifyOrderFetch, self).__init__()
        self.base_url = SHOPIFY_BASE_URL

    def fetch_all_customers(self):
        url = "{}{}".format(self.base_url, SHOPIFY_ALL_CUSTOMER_SUFFIX)

        response = self.make_request("GET", url)

        return response.json()

    def fetch_single_customer(self, shopify_customer_id):
        url = "{}{}".format(self.base_url, SHOPIFY_SINGLE_CUSTOMER_SUFFIX)
        url = url.format(customer_id=shopify_customer_id)
        
        response = self.make_request("GET", url)

        return response.json()

    def fetch_all_orders(self):
        url = "{}{}".format(self.base_url, SHOPIFY_ALL_ORDERS_SUFFIX)

        response = self.make_request("GET", url)

        return response.json()

    def fetch_single_order(self, shopify_order_id):
        url = "{}{}".format(self.base_url, SHOPIFY_SINGLE_order_SUFFIX)
        url = url.format(order_id=shopify_order_id)
        
        response = self.make_request("GET", url)

        return response.json()


# print(ShopifyOrderFetch().fetch_single_order(2053784240261))


# def get_shopify_headers():

#     headers = {'X-Shopify-Access-Token': config.get('shopify', 'api_password')}
#     return headers


# def get_allshopify_products():
#     url = "{}{}".format(SHOPIFY_BASE_URL, SHOPIFY_ALL_PRODUCS_SUFFIX)
#     headers = get_shopify_headers()

#     r = requests.get(url, headers=headers)
#     return r.json()

# def get_allshopify_orders():
#     url = "{}{}".format(SHOPIFY_BASE_URL, SHOPIFY_ALL_ORDERS_SUFFIX)
#     headers = get_shopify_headers()

#     r = requests.get(url, headers=headers)
#     return r.json()
