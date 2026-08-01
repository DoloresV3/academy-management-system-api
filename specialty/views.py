from rest_framework import generics
from .models import Specialty
from . serializers import SpecialtySerializer


class SpecialtyCreateView(generics.CreateAPIView):
    queryset = Specialty
    serializer_class = SpecialtySerializer


class SpecialtyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialty
    serializer_class = SpecialtySerializer
