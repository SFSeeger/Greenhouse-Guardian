from rest_framework import serializers

from guardian.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = ["device_token"]
        extra_kwargs = {
            "user": {"read_only": True},
        }
