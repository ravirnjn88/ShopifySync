from django.db import models
from shopifysync.models import BaseModel
from .option import Option


class OptionValue(BaseModel):
    """Model for storing options value."""

    name = models.CharField(max_length=100)
    option = models.ForeignKey(Option, related_name='option',
                               on_delete='CASCADE')

    class Meta:
        db_table = "option_value"
        verbose_name = "Option Value"
        verbose_name_plural = "Option Values"

    def __unicode__(self):
        """Return name of entity."""
        return self.name
