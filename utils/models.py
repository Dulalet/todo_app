import uuid
from django.db import models


class BaseModel(models.Model):
    """Абстрактный класс, который создает новый PK, на основе UUID"""
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='UUID',
    )

    class Meta:
        abstract = True
        ordering = ('-uuid', )

    def __str__(self) -> str:
        return str(self.uuid)


class DateModel(models.Model):
    """Абстрактный класс, который создает автоматические поля создания и обновления"""
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date created',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date updated',
    )

    class Meta:
        abstract = True
        ordering = ('-created_at', )

    def __str__(self):
        return str(self.created_at)
