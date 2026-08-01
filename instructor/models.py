from django.db import models
from django.core.validators import RegexValidator
from specialty.models import Specialty


phone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-\(\)]+$',
    message="Digite um telefone válido.")


class Instructor(models.Model):
    name = models.CharField(max_length=200)
    cref = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name="instructors"
    )
    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.specialty.name}'
