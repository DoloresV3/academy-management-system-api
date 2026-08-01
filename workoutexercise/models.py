from django.db import models
from workout.models import Workout
from exercise.models import Exercise


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name='workout_exercises'
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.PROTECT,
        related_name='workout_exercises'
    )
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField()
    order = models.PositiveIntegerField()
    observation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.workout.name} - {self.exercise.name}'
