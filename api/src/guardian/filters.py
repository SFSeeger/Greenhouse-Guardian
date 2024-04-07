from django_filters import rest_framework as filters

from guardian.models import Entry, Plant


class EntryFilter(filters.FilterSet):
    created_at = filters.IsoDateTimeFromToRangeFilter()

    class Meta:
        model = Entry
        fields = ["device", "created_at"]


class PlantFilter(filters.FilterSet):
    class Meta:
        model = Plant
        fields = ["device", "name"]
