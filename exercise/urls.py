from django.urls import path
from .views import ExerciseListCreateView, ExerciseRetrieveUpdateDestroyView

urlpatterns = [
    path('exercise/', ExerciseListCreateView.as_view(), name='exercise-create-view'),
    path('exercise/<int:pk>/', ExerciseRetrieveUpdateDestroyView.as_view(), name='exercise-detail-view'),
]
