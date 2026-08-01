from django.urls import path
from .views import PlanListCreateView, PlanRetrieveUpdateDestroyView


urlpatterns = [
    path('plan/', PlanListCreateView.as_view(), name='plan-create-view'),
    path('plan/<int:pk>/', PlanRetrieveUpdateDestroyView.as_view(), name='plan-detail-view'),
]
