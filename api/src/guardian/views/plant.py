from rest_framework import status
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     ListAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from guardian.filters import PlantFilter
from guardian.models import Plant
from guardian.serializers.plant import PlantSerializer
from user_management.permissions import IsUser


class PlantRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Plant.objects.filter(device__user=self.request.user)

class PlantListAPIView(ListAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = PlantFilter

    def get_queryset(self):
        return Plant.objects.filter(device__user=self.request.user)

class PlantCreateAPIView(CreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated, IsUser]
