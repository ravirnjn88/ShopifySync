from django.db import models
from shopifysync.models import BaseModel

class Product(BaseModel):
    """Model for Products."""

    shopify_product_id = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=500)
    body_html = models.TextField()
    vendor = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    handle = models.CharField(max_length=500)
    published_scope = models.CharField(max_length=200)
    admin_graphql_api_id = models.CharField(max_length=200)
    published_at = models.DateTimeField(null=True)


    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        """Return name of entity."""
        return self.title

    def __str__(self):
        return self.title