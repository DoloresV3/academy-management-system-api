from rest_framework import serializers
from .models import WorkoutExercise


class WorkoutExerciseSerielizer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = '__all__'
