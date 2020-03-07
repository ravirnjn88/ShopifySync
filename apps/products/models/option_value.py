from django.db import models
from shopifysync.models import BaseModel
from .option import Option


class OptionValue(BaseModel):
    """Model for storing options value."""

    name = models.CharField(max_length=100)
    option = models.ForeignKey(Option, related_name='option_value',
                               on_delete=models.CASCADE)

    class Meta:
        db_table = "option_value"
        verbose_name = "Option Value"
        verbose_name_plural = "Option Values"
        unique_together = ['name', 'option']

    def __unicode__(self):
        """Return name of entity."""
        return self.name

    def __str__(self):
        return self.name