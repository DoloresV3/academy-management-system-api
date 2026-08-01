from django.db import models
from localflavor.br.models import BRCPFField
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-\(\)]+$',
    message="Digite um telefone válido.")


class Student(models.Model):
    name = models.CharField(max_length=200)
    cpf = BRCPFField(unique=True)
    birth_date = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino')
        ]
    )
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )
    photo = models.ImageField(
        upload_to='student_photos/',
        blank=True,
        null=True
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
