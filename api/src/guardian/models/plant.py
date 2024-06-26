from django.db import models
from django.utils.translation import gettext_lazy as _

from api.utils import TimeStampModel


class Plant(TimeStampModel):
    name = models.CharField(_("Name"), max_length=255)
    device = models.ForeignKey("guardian.Device", on_delete=models.CASCADE)

    humidity_limit_max = models.FloatField(_("Maximum Humidity"), null=True, blank=True)
    humidity_limit_min = models.FloatField(_("Minimum Humidity"), null=True, blank=True)

    def __str__(self):
        return self.name
