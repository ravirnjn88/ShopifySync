from django.db import models
from shopifysync.models import BaseModel
from jsonfield import JSONField
from apps.orders.models.customer import Customer
from apps.orders.helpers import empty_dict, empty_list

class Order(BaseModel):

    shopify_order_id = models.BigIntegerField(unique=True)
    email = models.EmailField()
    closed_at = models.DateTimeField(null=True, blank=True)
    number = models.IntegerField()
    note = models.TextField(null=True)
    gateway = models.CharField(max_length=32, null=True)
    test = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    subtotal_price = models.DecimalField(max_digits=9, decimal_places=2)
    total_weight = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    total_tax = models.DecimalField(max_digits=9, decimal_places=2)
    taxes_included = models.BooleanField(default=False)
    currency = models.CharField(max_length=8)
    financial_status = models.CharField(max_length=32)
    confirmed = models.BooleanField(default=False)
    total_discounts = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    total_line_items_price = models.DecimalField(max_digits=9, decimal_places=2)
    cart_token = models.CharField(max_length=32, null=True)
    buyer_accepts_marketing = models.BooleanField(default=True)
    name = models.CharField(max_length=32)
    referring_site = models.URLField(max_length=2048, null=True)
    landing_site = models.URLField(max_length=2048, null=True)
    cancelled_at = models.DateTimeField(null=True)
    cancel_reason = models.CharField(max_length=32, null=True, blank=True)
    total_price_usd = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    order_number = models.IntegerField()
    discount_applications = JSONField(default=empty_list)
    discount_codes = JSONField(default=empty_list)
    note_attributes = JSONField(default=empty_list)
    payment_gateway_names = JSONField(default=empty_list)
    processing_method = models.CharField(max_length=32, null=True, blank=True)
    source_name = models.CharField(max_length=32, null=True, blank=True)
    fulfillment_status = models.CharField(max_length=32, null=True, blank=True)
    tax_lines = JSONField(default=empty_list)
    tags = models.CharField(max_length=104, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    billing_address = JSONField(default=empty_dict)
    shipping_address = JSONField(default=empty_dict)
    customer = models.ForeignKey(Customer, related_name='order', on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __unicode__(self):
        """Return name of entity."""
        return self.order_number

    def __str__(self):
        return str(self.order_number)