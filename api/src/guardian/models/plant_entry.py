from django.db import models
from django.utils.translation import gettext_lazy as _

from api.utils import TimeStampModel


class PlantEntry(models.Model):
    plant = models.ForeignKey("guardian.Plant", on_delete=models.CASCADE)
    entry = models.ForeignKey("guardian.Entry", on_delete=models.CASCADE)
    temperature = models.FloatField(_("Temperature"))
    humidity = models.FloatField(_("Humidity"))

    def __str__(self):
        return f"{self.plant} - {self.entry.created_at}"
