from django.urls import include, path

from guardian.views import (
    DeviceCreateAPIView,
    DeviceListAPIView,
    DeviceRetrieveUpdateDestroyAPIView,
    EntryList,
)

urlpatterns = [
    path("entry/", EntryList.as_view(), name="entry-list"),
    path(
        "device/<int:pk>/", DeviceRetrieveUpdateDestroyAPIView.as_view(), name="device"
    ),
    path("device/", DeviceCreateAPIView.as_view(), name="device-create"),
    path("device/list/", DeviceListAPIView.as_view(), name="device-list"),
]
