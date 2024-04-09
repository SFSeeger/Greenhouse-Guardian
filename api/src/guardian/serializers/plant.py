from rest_framework import serializers

from guardian.models import Plant


class PlantSerializer(serializers.ModelSerializer):
    def validate_device(self, value):
        if value.user != self.context["request"].user:
            raise serializers.ValidationError("Device does not belong to the user.")
        return value

    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "device",
            "humidity_limit_max",
            "humidity_limit_min",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
