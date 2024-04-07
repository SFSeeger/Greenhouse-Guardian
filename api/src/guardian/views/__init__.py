from .device import (
    DeviceCreateAPIView,
    DeviceListAPIView,
    DeviceRegenerateTokenAPIView,
    DeviceRetrieveUpdateDestroyAPIView,
)
from .entry import EntryListAPIView

__all__ = [
    DeviceCreateAPIView.__name__,
    DeviceListAPIView.__name__,
    DeviceRetrieveUpdateDestroyAPIView.__name__,
    DeviceRegenerateTokenAPIView.__name__,
    EntryListAPIView.__name__,
]
