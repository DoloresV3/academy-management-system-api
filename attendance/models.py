from django.db import models
from students.models import Student


class Attendance(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendances'
    )
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student.name} - {self.check_in:%d/%m/%Y %H:%M}'
