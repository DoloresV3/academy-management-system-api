from django.urls import path
from .views import SpecialtyCreateView, SpecialtyRetrieveUpdateDestroyView


urlpatterns = [
    path('specialty/', SpecialtyCreateView.as_view(), name='specialty-create-view'),
    path('specialty/<int:pk>/', SpecialtyRetrieveUpdateDestroyView.as_view(), name='specialty-detail-view'),
]
