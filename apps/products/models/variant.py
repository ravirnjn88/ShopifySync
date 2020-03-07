from django.db import models
from shopifysync.models import BaseModel
from .product import Product
from .images import Image
from .option_value import OptionValue

class Variant(BaseModel):
    """Model for Images."""

    WEIGHT = [('lb', 'lbs'), ('oz', 'oz'), ('kg', 'kilogram'), ('g', 'gram')]

    shopify_variant_id = models.BigIntegerField(unique=True)
    product = models.ForeignKey(Product, related_name='variant',
                                        on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sku = models.CharField(max_length=200, null=True)
    position = models.IntegerField(null=True, default=1)
    inventory_policy = models.CharField(max_length=40, null=True, default='deny')
    compare_at_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    fulfillment_service = models.CharField(max_length=40, default='manual')
    inventory_management = models.CharField(max_length=40, null=True, default='blank')
    option1 = models.ForeignKey(OptionValue, related_name='variant1', on_delete=models.SET_NULL, null=True)
    option2 = models.ForeignKey(OptionValue, related_name='variant2', on_delete=models.SET_NULL, null=True)
    option3 = models.ForeignKey(OptionValue, related_name='variant3', on_delete=models.SET_NULL, null=True)
    taxable = models.BooleanField(default=True)
    barcode = models.CharField(max_length=200, null=True)
    weight = models.IntegerField(null=True)
    weight_unit = models.CharField(max_length=20, null=True, choices=WEIGHT)
    image = models.ForeignKey(Image, related_name='variant', on_delete=models.SET_NULL, null=True)
    inventory_quantity = models.IntegerField()
    requires_shipping = models.BooleanField(default=True)



    class Meta:
        db_table = "variant"
        verbose_name = "Variant"
        verbose_name_plural = "Variants"

    def __unicode__(self):
        """Return name of entity."""
        return self.title

    def __str__(self):
        return self.title