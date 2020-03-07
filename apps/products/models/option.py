from django.db import models
from shopifysync.models import BaseModel
from .product import Product

class Option(BaseModel):
    """Model for Shopify Product Option."""

    shopify_option_id = models.BigIntegerField(db_index=True, null=True)
    product_id = models.ForeignKey(Product, related_name='options',
                                           on_delete='CASCADE')
    option_name = models.CharField(max_length=100, unique=True)
    position = models.IntegerField(null=True, default=1)

    class Meta:
        db_table = "option"
        verbose_name = "Option"
        verbose_name_plural = "Options"
        unique_together = [['product_id', 'option_name'], ['product_id', 'position']]

    def __unicode__(self):
        """Return name of entity."""
        return self.title

    def __str__(self):
        return self.title