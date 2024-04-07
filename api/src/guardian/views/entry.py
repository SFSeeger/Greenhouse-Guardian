from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from guardian.filters import EntryFilter
from guardian.models import Entry
from guardian.serializers.entry import EntrySerializer
from user_management.permissions import IsDevice


class EntryListAPIView(ListAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]
    filterset_class = EntryFilter

    def get_queryset(self):
        return Entry.objects.filter(device__user=self.request.user)


class EntryCreateAPIView(CreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated, IsDevice]

    def perform_create(self, serializer):
        serializer.save(device=self.request.device)
