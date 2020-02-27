import requests
from utils import config
from utils.constants import SHOPIFY_BASE_URL, SHOPIFY_ALL_PRODUCS_SUFFIX, SHOPIFY_ALL_ORDERS_SUFFIX

def get_shopify_headers():

    headers = {'X-Shopify-Access-Token': config.get('shopify', 'api_password')}
    return headers


def get_allshopify_products():
    url = "{}{}".format(SHOPIFY_BASE_URL, SHOPIFY_ALL_PRODUCS_SUFFIX)
    headers = get_shopify_headers()

    r = requests.get(url, headers=headers)
    return r.json()

def get_allshopify_orders():
    url = "{}{}".format(SHOPIFY_BASE_URL, SHOPIFY_ALL_ORDERS_SUFFIX)
    headers = get_shopify_headers()

    r = requests.get(url, headers=headers)
    return r.json()
