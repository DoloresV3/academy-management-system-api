from django.urls import path
from .views import AssessmentCreateListView, AssessmentRetrieveUpdateDestroyView


urlpatterns = [
    path('assessment/', AssessmentCreateListView.as_view(), name='assessment-create-view'),
    path('assessment/<int:pk>/', AssessmentRetrieveUpdateDestroyView.as_view(), name='assessment-detail-view')
]
