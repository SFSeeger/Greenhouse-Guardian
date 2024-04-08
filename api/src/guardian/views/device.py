from django.shortcuts import get_object_or_404
from knox.models import AuthToken
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from guardian.models import Device
from guardian.serializers import DeviceSerializer
from user_management.permissions import IsUser


class DeviceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)


class DeviceCreateAPIView(CreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance, token = AuthToken.objects.create(user=self.request.user, expiry=None)
        serializer.save(user=self.request.user, device_token=instance)

        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        data["token"] = token
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class DeviceListAPIView(ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)


class DeviceRegenerateTokenAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated, IsUser]

    def post(self, request, *args, **kwargs):
        device = get_object_or_404(Device, pk=kwargs.get("pk"), user=self.request.user)
        if device.device_token:
            device.device_token.delete()
        instance, token = AuthToken.objects.create(user=self.request.user, expiry=None)
        device.device_token = instance
        device.save()
        return Response({"token": token}, status=status.HTTP_200_OK)
