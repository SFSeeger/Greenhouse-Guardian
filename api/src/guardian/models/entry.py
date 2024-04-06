from django.db import models
from django.utils.translation import gettext_lazy as _

from api.utils import TimeStampModel


class Entry(TimeStampModel):
    device = models.ForeignKey("guardian.Device", on_delete=models.CASCADE)
    temperature = models.FloatField(_("Temperature"))
    humidity = models.FloatField(_("Humidity"))

    def __str__(self):
        return f"{self.device} - {self.created_at}"
