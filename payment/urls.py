from django.urls import path
from .views import PaymentListCreateView, PaymentRetrieveUpdateDestroyView


urlpatterns = [
    path('payment/', PaymentListCreateView.as_view(), name='payment-create-view'),
    path('payment/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail-view'),
]
