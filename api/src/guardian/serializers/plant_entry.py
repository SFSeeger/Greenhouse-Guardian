from rest_framework import serializers

from guardian.models.plant_entry import PlantEntry


class PlantEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantEntry
        fields = [
            "id",
            "plant",
            "humidity",
        ]
