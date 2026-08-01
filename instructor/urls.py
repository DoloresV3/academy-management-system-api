from django.urls import path
from .views import InstructorListCreateView, InstructorRetrieveUpdateDestroyView


urlpatterns = [
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-create-list'),
    path('instructors/<int:pk>/', InstructorRetrieveUpdateDestroyView.as_view(), name='instructor-detail-view'),
]
