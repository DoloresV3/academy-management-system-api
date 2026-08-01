from rest_framework import generics
from .models import Assessment
from .serializers import AssessmentSerializer


class AssessmentCreateListView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class AssessmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
