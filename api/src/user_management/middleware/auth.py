from django.core.cache import cache
from django.http import HttpRequest
from django.utils.deprecation import MiddlewareMixin
from knox.crypto import hash_token
from knox.settings import CONSTANTS

from guardian.models.device import Device


class DeviceMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        token = request.headers.get("Authorization", None)
        if not token:
            request.device = None
            return
        token = token[6:]
        device = cache.get(token)
        if device:
            request.device = device
            return
        try:
            request.device = Device.objects.get(
                device_token__digest=hash_token(token),
                device_token__token_key=token[: CONSTANTS.TOKEN_KEY_LENGTH],
            )
        except Device.DoesNotExist:
            request.device = None
        cache.set(token, request.device, 60 * 60)
        return
