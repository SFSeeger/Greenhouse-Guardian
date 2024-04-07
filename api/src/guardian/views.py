from knox.models import AuthToken
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Device, Entry
from .serializers import DeviceSerializer, EntrySerializer


class EntryList(APIView):
    def get(self, request):
        snippets = Entry.objects.all()
        serializer = EntrySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)


class DeviceCreateAPIView(CreateAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance, token = AuthToken.objects.create(user=self.request.user)
        serializer.save(user=self.request.user, device_token=instance)

        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        data["token"] = token
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class DeviceListAPIView(ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)
