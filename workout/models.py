from django.db import models
from students.models import Student
from instructor.models import Instructor


class Workout(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='workouts'
    )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.PROTECT,
        related_name='workouts'
    )
    objective = models.TextField(
        blank=True,
        null=True
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.student.name}'
