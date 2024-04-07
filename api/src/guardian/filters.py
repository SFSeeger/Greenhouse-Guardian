from django_filters import rest_framework as filters

from guardian.models.entry import Entry


class EntryFilter(filters.FilterSet):
    created_at = filters.IsoDateTimeFromToRangeFilter()

    class Meta:
        model = Entry
        fields = ["device", "created_at"]
