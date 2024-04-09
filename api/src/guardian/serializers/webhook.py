from rest_framework import serializers

from guardian.models import Webhook


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = ["id", "webhook_type", "url", "user", "message_prefix"]
        read_only_fields = ["id", "user"]
