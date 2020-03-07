from django.db import models
from shopifysync.models import BaseModel


class Option(BaseModel):
    """Model for storing options."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "option"
        verbose_name = "Product option"
        verbose_name_plural = "Products options"

    def __unicode__(self):
        """Return name of entity."""
        return self.name
