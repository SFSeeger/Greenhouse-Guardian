from django.db import transaction
from django.db.models import Q
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
        data = request.data

        if not isinstance(data, list):
            return Response({"detail": "Expected a list of items but got type 'dict'."}, status=status.HTTP_400_BAD_REQUEST)

        data = [dict(d, device=request.device.id) for d in data]
        serializer = self.get_serializer(data=data, many=True)

        serializer.is_valid(raise_exception=True)

        request_ids = [d.get('id') for d in data]

        existing_ids = list(Plant.objects.filter(id__in=request_ids).values_list('id', flat=True))
        objects_to_create = []
        for obj_id, obj in zip(request_ids, serializer.validated_data):
            if not obj_id in existing_ids:
                objects_to_create.append(obj)

        with transaction.atomic():
            plants = Plant.objects.bulk_create([Plant(**data) for data in objects_to_create])

        request_plants = Plant.objects.filter(Q(id__in=[plant.id for plant in plants]) | Q(id__in=existing_ids))

        return Response({"ids": request_plants.values_list("id", flat=True)}, status=status.HTTP_201_CREATED)