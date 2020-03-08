from django.db import models
from shopifysync.models import BaseModel

class Customer(BaseModel):

    shopify_cusomer_id = models.BigIntegerField(unique=True)
    email = models.EmailField(null=True)
    accepts_marketing = models.BooleanField(default=False)
    first_name = models.CharField(max_length=104, blank=True)
    last_name = models.CharField(max_length=104, blank=True)
    orders_count = models.IntegerField()
    state = models.CharField(max_length=64)
    total_spent = models.DecimalField(max_digits=8, decimal_places=2)
    last_order_id = models.IntegerField(null=True)
    note = models.TextField(null=True, blank=True)
    verified_email = models.BooleanField(default=False)
    multipass_identified = models.CharField(max_length=64, null=True)
    tax_exempt = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True)
    tags = models.TextField(null=True)
    last_order_name = models.CharField(max_length=64,null=True)
    currency = models.CharField(max_length=24)
    marketing_opt_in_level = models.CharField(max_length=24, null=True)

    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __unicode__(self):
        """Return name of entity."""
        return self.first_name

    def __str__(self):
        return self.first_name