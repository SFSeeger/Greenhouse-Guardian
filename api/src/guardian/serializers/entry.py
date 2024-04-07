from rest_framework import serializers

from guardian.models import Entry
from guardian.serializers.plant_entry import PlantEntrySerializer


class EntrySerializer(serializers.ModelSerializer):
    plantentry_set = PlantEntrySerializer(many=True)

    class Meta:
        model = Entry
        fields = [
            "id",
            "plantentry_set",
            "humidity",
            "temperature",
            "created_at",
            "updated_at",
        ]
        depth = 2
