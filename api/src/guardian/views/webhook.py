from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from guardian.models import Webhook
from guardian.serializers.webhook import WebhookSerializer
from user_management.permissions import IsUser


class WebhookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WebhookSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        return Webhook.objects.filter(user=self.request.user)


class WebhookCreateAPIView(CreateAPIView):
    serializer_class = WebhookSerializer
    permission_classes = [IsAuthenticated, IsUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
