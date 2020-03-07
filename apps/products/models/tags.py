from django.db import models
from shopifysync.models import BaseModel
from .product import Product


class Tag(BaseModel):
    """Model for storing Product tag."""

    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name='tags',
                                on_delete=models.CASCADE)

    class Meta:
        db_table = "tag"
        verbose_name = "Product Tag"
        verbose_name_plural = "Products Tag"

    def __unicode__(self):
        """Return name of entity."""
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)
