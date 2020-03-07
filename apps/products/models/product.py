from django.db import models
from shopifysync.models import BaseModel

class Product(BaseModel):
    """Model for Products."""
    STATUS = [('draft', 'Draft'), ('published', 'Published')]

    shopify_product_id = models.BigIntegerField(db_index=True, null=True)
    title = models.CharField(max_length=500)
    body_html = models.TextField()
    vendor = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    handle = models.CharField(max_length=500)
    published_scope = models.CharField(max_length=200)
    admin_graphql_api_id = models.CharField(max_length=200)
    variable_product = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)


    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        """Return name of entity."""
        return self.title

    def __str__(self):
        return self.title