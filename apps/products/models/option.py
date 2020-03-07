from django.db import models
from shopifysync.models import BaseModel
from .product import Product

class Option(BaseModel):
    """Model for Shopify Product Option."""

    shopify_option_id = models.BigIntegerField(unique=True)
    product = models.ForeignKey(Product, related_name='options',
                                           on_delete=models.CASCADE)
    option_name = models.CharField(max_length=100, unique=True)
    position = models.IntegerField(null=True, default=1)

    class Meta:
        db_table = "option"
        verbose_name = "Option"
        verbose_name_plural = "Options"
        unique_together = [['product', 'option_name'], ['product', 'position']]

    def __unicode__(self):
        """Return name of entity."""
        return self.option_name

    def __str__(self):
        return self.option_name