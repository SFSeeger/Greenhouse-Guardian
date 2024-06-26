from rest_framework import serializers

from guardian.models import Entry, PlantEntry
from guardian.serializers.plant_entry import PlantEntrySerializer


class EntrySerializer(serializers.ModelSerializer):
    plantentry_set = PlantEntrySerializer(many=True)

    def create(self, validated_data):
        plant_entries = validated_data.pop("plantentry_set")
        entry = Entry.objects.create(**validated_data)
        for plant_entry in plant_entries:
            PlantEntry.objects.create(entry=entry, **plant_entry)
        return entry

    class Meta:
        model = Entry
        fields = [
            "id",
            "device",
            "plantentry_set",
            "humidity",
            "temperature",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at",
            "device",
        ]
