from rest_framework import serializers

from guardian.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = "__all__"
