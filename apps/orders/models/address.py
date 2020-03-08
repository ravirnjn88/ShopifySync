from django.db import models
from shopifysync.models import BaseModel
from .customer import Customer

class Address(BaseModel):

    shopify_address_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    company = models.CharField(max_length=64, null=True, blank=True)
    address1 = models.CharField(max_length=256, blank=True, null=True)
    address2 = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True)
    province = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=64, blank=True)
    zip = models.CharField(max_length=16, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    province_code = models.CharField(max_length=32, null=True, blank=True)
    country_code = models.CharField(max_length=32, blank=True, null=True)
    country_name = models.CharField(max_length=32, blank=True, null=True)
    default = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, related_name='address',
                                 on_delete=models.CASCADE)


    class Meta:
        db_table = "address"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __unicode__(self):
        """Return name of entity."""
        return "{}{}".format(self.first_name, self.address1)

    def __str__(self):
        return "{}{}".format(self.first_name, self.address1)