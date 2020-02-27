from django.db import models
from shopifysync.models import BaseModel
from apps.products.models import Product
# Create your models here.

class Order(BaseModel):
    """Model for Orders."""
    ### Due to time Limitation folowing assumptions are made ###
    # Only syncing order no and product
    # We can create seperate table for address, payment and 
    # LInk to those

    shopify_order_id = models.BigIntegerField(unique=True)
    order_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __unicode__(self):
        """Return name of entity."""
        return "{}-{}".format(self.order_number, self.customer_name)

    def __str__(self):
        return "{}-{}".format(self.order_number, self.customer_name)


class OrderProduct(BaseModel):
    """Model for storing Products for an order."""

    order = models.ForeignKey('Order', related_name='order',
                                on_delete='CASCADE', default=1)
    product = models.ForeignKey(Product, related_name='order_product',
                                on_delete='CASCADE')

    class Meta:
        db_table = "order_product"
        verbose_name = "Order Product"
        verbose_name_plural = "Order Products"

    def __unicode__(self):
        """Return name of entity."""
        return self.product.title