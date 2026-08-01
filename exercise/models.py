from django.db import models


class MuscleGroup(models.TextChoices):
    CHEST = "CHEST", "Peitoral"
    BACK = "BACK", "Costas"
    SHOULDERS = "SHOULDERS", "Ombros"
    BICEPS = "BICEPS", "Bíceps"
    TRICEPS = "TRICEPS", "Tríceps"
    LEGS = "LEGS", "Pernas"
    GLUTES = "GLUTES", "Glúteos"
    ABS = "ABS", "Abdômen"
    CARDIO = "CARDIO", "Cardio"


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    muscle_group = models.TextField(
        choices=MuscleGroup.choices,
        max_length=20
    )
    equipment = models.CharField(max_length=100)
    description = models.TextField(
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='exercise_images/',
        blank=True,
        null=True
    )
    video_url = models.URLField(
        blank=True,
        null=True
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
