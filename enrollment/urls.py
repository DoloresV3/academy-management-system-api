from django.urls import path
from .views import EnrollmentListCreateView, EnrollmentRetrieveUpdateDestroyView


urlpatterns = [
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-create-view'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-detail-view'),
]
