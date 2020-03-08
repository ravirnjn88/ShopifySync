from django.db import models
from shopifysync.models import BaseModel
from .product import Product

class Image(BaseModel):
    """Model for Images."""

    shopify_image_id = models.BigIntegerField(unique=True)
    product = models.ForeignKey(Product, related_name='images',
                                   on_delete=models.CASCADE)
    position =  models.IntegerField(null=True, default=1)
    src = models.URLField()
    admin_graphql_api_id = models.CharField(max_length=500, null=True)
    width =  models.IntegerField(null=True)
    height =  models.IntegerField(null=True)
    alt = models.CharField(max_length=100, null=True)



    class Meta:
        db_table = "image"
        verbose_name = "Image"
        verbose_name_plural = "Images"
        unique_together = ['product', 'position']

    def __unicode__(self):
        """Return name of entity."""
        return self.src

    def __str__(self):
        return self.src
