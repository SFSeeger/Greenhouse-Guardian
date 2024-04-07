from django.urls import include, path

from guardian.views.device import (
    DeviceCreateAPIView,
    DeviceListAPIView,
    DeviceRegenerateTokenAPIView,
    DeviceRetrieveUpdateDestroyAPIView,
)
from guardian.views.entry import EntryCreateAPIView, EntryListAPIView
from guardian.views.plant import PlantCreateAPIView, PlantRetrieveUpdateDestroyAPIView
from guardian.views.webhook import (
    WebhookCreateAPIView,
    WebhookRetrieveUpdateDestroyAPIView,
)

device_urlpatterns = [
    path("<int:pk>/", DeviceRetrieveUpdateDestroyAPIView.as_view(), name="device"),
    path("", DeviceCreateAPIView.as_view(), name="device-create"),
    path("list/", DeviceListAPIView.as_view(), name="device-list"),
    path(
        "<int:pk>/regenerate-token/",
        DeviceRegenerateTokenAPIView.as_view(),
        name="device-regenerate-token",
    ),
]

entry_urlpatterns = [
    path("list/", EntryListAPIView.as_view(), name="entry-list"),
    path("", EntryCreateAPIView.as_view(), name="entry-create"),
]

plant_urlpatterns = [
    path("", PlantCreateAPIView.as_view(), name="plant-create"),
    path("<int:pk>/", PlantRetrieveUpdateDestroyAPIView.as_view(), name="plant"),
]

webhook_urlpatterns = [
    path("", WebhookCreateAPIView.as_view(), name="webhook-create"),
    path("<int:pk>/", WebhookRetrieveUpdateDestroyAPIView.as_view(), name="webhook"),
]

urlpatterns = [
    path("device/", include(device_urlpatterns)),
    path("entry/", include(entry_urlpatterns)),
    path("plant/", include(plant_urlpatterns)),
    path("webhook/", include(webhook_urlpatterns)),
]
