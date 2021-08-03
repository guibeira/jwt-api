import uuid

from model_utils.fields import AutoCreatedField, AutoLastModifiedField, UUIDField
from django.db import models


class UUIDModel(models.Model):
    id = UUIDField(primary_key=True, version=4, editable=False)

    class Meta:
        abstract = True


class IndexedTimeStampedModel(models.Model):
    created = AutoCreatedField(("created"), db_index=True)
    modified = AutoLastModifiedField(("modified"), db_index=True)

    class Meta:
        abstract = True
