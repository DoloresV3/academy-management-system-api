from django.db import models
from students.models import Student
from plan.models import Plan


class Enrollment(models.Model):

    STATUS_CHOICES = (
        ("ACTIVE", "Ativa"),
        ("SUSPENDED", "Suspensa"),
        ("CANCELLED", "Cancelada"),
        ("FINISHED", "Finalizada"),
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name="enrollments"
    )
    enrollment_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )
    observation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.name} - {self.plan.name}'
