from rest_framework import serializers

from guardian.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "id",
            "name",
            "user",
            "temperature_limit_max",
            "temperature_limit_min",
            "humidity_limit_max",
            "humidity_limit_min",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "created_at", "updated_at"]
