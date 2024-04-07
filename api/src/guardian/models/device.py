from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.utils import TimeStampModel

User = get_user_model()


class Device(TimeStampModel):
    name = models.CharField(_("Name"), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_token = models.ForeignKey(
        "knox.AuthToken", on_delete=models.SET_NULL, null=True, blank=True
    )

    temperature_limit_max = models.FloatField(
        _("Maximum Temperature"), null=True, blank=True
    )
    temperature_limit_min = models.FloatField(
        _("Minimum Temperature"), null=True, blank=True
    )
    humidity_limit_max = models.FloatField(_("Maximum Humidity"), null=True, blank=True)
    humidity_limit_min = models.FloatField(_("Minimum Humidity"), null=True, blank=True)

    def __str__(self):
        return self.name
