from django.urls import path
from .views import WorkoutListCreateView, WorkoutRetrieveUpdateDestroyView


urlpatterns = [
    path('workout/', WorkoutListCreateView.as_view(), name='workout-create-view'),
    path('workout/<int:pk>/', WorkoutRetrieveUpdateDestroyView.as_view(), name='workout-detail-view'),
]
