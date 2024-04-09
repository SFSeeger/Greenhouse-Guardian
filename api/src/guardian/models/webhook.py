import json

import requests
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Webhook(models.Model):
    class WebhookType(models.IntegerChoices):
        DISCORD = 1, _("Discord")

    webhook_type = models.IntegerField(
        _("Webhook Type"), choices=WebhookType.choices, default=WebhookType.DISCORD
    )
    url = models.URLField(_("Webhook URL"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message_prefix = models.CharField(
        _("Message Prefix"),
        help_text=_(
            "Prefix to add to messages. Useful for adding @everyone or similar"
        ),
        max_length=255,
        blank=True,
        null=True,
    )
    last_notification = models.DateTimeField(
        _("Last Notification"), null=True, blank=True
    )

    WEBHOOK_METHODS = {
        WebhookType.DISCORD: "send_discord_notification",
    }

    def send_discord_notification(self, message, **kwargs):
        data = {
            "content": f"{self.message_prefix}",
            "embeds": [
                {
                    "description": message,
                    "color": kwargs.get("color", 0x00FF00),
                    "url": kwargs.get("url"),
                }
            ],
        }
        requests.post(
            self.url,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )

    def handle_notification(self, message, **kwargs):
        getattr(self, self.WEBHOOK_METHODS[self.webhook_type])(message, **kwargs)

    class Meta:
        verbose_name = _("Webhook")
        verbose_name_plural = _("Webhooks")

    def __str__(self):
        return f"{self.user} - {self.get_webhook_type_display()}"
