from django.db import models
from shopifysync.models import BaseModel
# Create your models here.

class Product(BaseModel):
    """Model for Products."""
    ### Due to time Limitation folowing assumptions are made ###
    # Only one image each product
    # Variable product not supported
    # Tags, collection not imlementing
    # Other variables like ISBN, weight, country of origin also not added.

    shopify_product_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    description = models.TextField()
    image = models.CharField(max_length=500)
    mrp = models.FloatField()
    sell_price = models.FloatField()
    sku = models.CharField(max_length=50, db_index=True)
    quantity = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        """Return name of entity."""
        return "{}-{}".format(self.title, self.sku)

    def __str__(self):
        return "{}-{}-Quan:{}".format(self.title, self.sku, self.quantity)