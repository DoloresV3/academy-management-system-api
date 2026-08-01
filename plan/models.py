from django.db import models


class Plan(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField(blank=True)
    duration_days = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
