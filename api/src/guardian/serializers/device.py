from rest_framework import serializers

from guardian.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "device_token": {"write_only": True},
        }
