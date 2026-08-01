from django.db import models
from students.models import Student


class Assessment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='assessment'
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    height = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    body_fat = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    muscle_mass = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    chest = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    abdomen = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    hip = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    right_arm = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    left_arm = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    right_thigh = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    left_thigh = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    right_calf = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    left_calf = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    observation = models.TextField(
        max_length=200,
        blank=True,
        null=True
    )
    assessment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.name} - {self.assessment_date}'
