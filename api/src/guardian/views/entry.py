from django.conf import settings
from django.db.models import F, Q
from django.utils import timezone
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from guardian.filters import EntryFilter
from guardian.models import Device, Entry, Webhook
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
        entry: Entry = serializer.save(device=self.request.device)
        device: Device = self.request.device
        user = self.request.user
        try:
            webhook: Webhook = user.webhook
        except Webhook.DoesNotExist:
            return

        if webhook.last_notification:
            if timezone.now() - webhook.last_notification < timezone.timedelta(
                minutes=settings.NOTIFICATION_TIMEDELTA
            ):
                return

        webhook.last_notification = timezone.now()
        webhook.save()

        message = [f"# Warning on {device.name}"]

        if entry.temperature > device.temperature_limit_max:
            message.append(f"Temperature is too high: **{entry.temperature}°C**")
        elif entry.temperature < device.temperature_limit_min:
            message.append(f"Temperature is too low: **{entry.temperature}°C**")
        if entry.humidity > device.humidity_limit_max:
            message.append(f"Humidity is too high: **{entry.humidity}%**")
        elif entry.humidity < device.humidity_limit_min:
            message.append(f"Humidity is too low: **{entry.humidity}%**")

        high_water_plant = entry.plantentry_set.filter(
            humidity__gt=F("plant__humidity_limit_max")
        )
        low_water_plant = entry.plantentry_set.filter(
            humidity__lt=F("plant__humidity_limit_min")
        )

        if high_water_plant.exists():
            message.append(
                f"Following plants are drowning: **{', '.join(str(plant_entry.plant) for plant_entry in high_water_plant)}**"
            )
        if low_water_plant.exists():
            message.append(
                f"Following plants are thirsty: **{', '.join(str(plant_entry.plant) for plant_entry in low_water_plant)}**",
            )
        if len(message) > 1:
            webhook.handle_notification("\n".join(message), color=0xFF0000)
