from django.urls import path
from .views import AttendanceListCreateView, AttendanceRetrieveUpdateDestroyView


urlpatterns = [
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-create-view'),
    path('attendance/<int:pk>/', AttendanceRetrieveUpdateDestroyView.as_view(), name='attendance-detail_view'),
]
