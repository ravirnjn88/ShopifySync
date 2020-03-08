from django.db import models
from shopifysync.models import BaseModel
from jsonfield import JSONField
from apps.products.models.variant import Variant
from apps.products.models.product import Product
from apps.orders.models.order import Order
from apps.orders.helpers import empty_dict, empty_list

class LineItem(BaseModel):

    shopify_line_item_id = models.BigIntegerField(unique=True)
    variant =product = models.ForeignKey(Variant, related_name='line_items', null=True,
                                         on_delete=models.SET_NULL)
    product = product = models.ForeignKey(Product, related_name='line_items', null=True,
                                          on_delete=models.SET_NULL)
    title = models.CharField(max_length=500, blank=True, null=True)
    quantity = models.IntegerField()
    sku = models.CharField(max_length=48, blank=True, null=True)
    variant_title = models.CharField(max_length=500, blank=True, null=True)
    vendor = models.CharField(max_length=64, blank=True, null=True)
    fulfillment_service = models.CharField(max_length=64, blank=True, null=True)
    requires_shipping = models.BooleanField(default=True)
    taxable = models.BooleanField(default=False)
    gift_card = models.BooleanField(default=False)
    name = models.CharField(max_length=256, blank=True, null=True)
    variant_inventory_management = models.CharField(max_length=256)
    properties = JSONField(default=empty_list)
    product_exists = models.BooleanField(default=True)
    fulfillable_quantity = models.IntegerField()
    grams = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    total_discount = models.DecimalField(max_digits=9, decimal_places=2)
    fulfillment_status = models.CharField(max_length=32, null=True, blank=True)
    price_set = JSONField(default=empty_dict)
    total_discount_set = JSONField(default=empty_dict)
    discount_allocations = JSONField(default=empty_list)
    tax_lines = JSONField(default=empty_list)
    order = models.ForeignKey(Order, related_name='line_items', on_delete=models.CASCADE)


    class Meta:
        db_table = "line_item"
        verbose_name = "LineItem"
        verbose_name_plural = "LineItems"

    def __unicode__(self):
        """Return name of entity."""
        return self.title

    def __str__(self):
        return self.title