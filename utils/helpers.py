import hashlib, base64, hmac

def get_hmac(body, secret):
    """
    Calculate the HMAC value of the given request body and secret as per Shopify's documentation for Webhook requests.
    """
    hash = hmac.new(secret.encode('utf-8'), body, hashlib.sha256)
    return base64.b64encode(hash.digest()).decode()


def hmac_is_valid(body, secret, hmac_to_verify):
    """
    Return True if the given hmac_to_verify matches that calculated from the given body and secret.
    """
    return get_hmac(body, secret) == hmac_to_verify