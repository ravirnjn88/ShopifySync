"""Containing the base models"""
from __future__ import absolute_import, unicode_literals

from django.db import models



class BaseModel(models.Model):
    """Custom model to be inherited as base while making other models."""

    created_at = models.DateTimeField(
        auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True