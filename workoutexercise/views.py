from rest_framework import generics
from .models import WorkoutExercise
from .serializers import WorkoutExerciseSerielizer


class WorkoutExerciseCreateView(generics.CreateAPIView):
    queryset = WorkoutExercise
    serializer_class = WorkoutExerciseSerielizer


class WorkoutExerciseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutExercise
    serializer_class = WorkoutExerciseSerielizer
