from django.urls import path
from .views import WorkoutExerciseCreateView, WorkoutExerciseRetrieveUpdateDestroyView


urlpatterns = [
    path('workoutexercise/', WorkoutExerciseCreateView.as_view(), name='workoutexercise-create-view'),
    path('workoutexercise/<int:pk>/', WorkoutExerciseRetrieveUpdateDestroyView.as_view(), name='workoutexercise-detail-view'),
]
