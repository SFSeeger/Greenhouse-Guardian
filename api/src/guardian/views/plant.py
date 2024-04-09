from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from guardian.filters import PlantFilter
from guardian.models import Plant
from guardian.serializers.plant import PlantSerializer
from user_management.permissions import IsDevice, IsUser


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


class PlantMassCreateAPIView(GenericAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated, IsDevice]

    def post(self, request):
        print(request.data)
        request_data = [dict(data, device=request.device.id) for data in request.data]
        serializer = self.get_serializer(data=request_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
