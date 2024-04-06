from django.db import models
from django.utils.translation import gettext_lazy as _

from api.utils import TimeStampModel


class Device(TimeStampModel):
    name = models.CharField(_("Name"), max_length=255)
    user = models.ForeignKey(_("User"), "auth.User", on_delete=models.CASCADE)

    temperature_limit = models.FloatField(_("Temperature Limit"), null=True, blank=True)
    humidity_limit = models.FloatField(_("Humidity Limit"), null=True, blank=True)

    def __str__(self):
        return self.name
