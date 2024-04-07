# Generated by Django 5.0.4 on 2024-04-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guardian", "0004_webhook"),
    ]

    operations = [
        migrations.AddField(
            model_name="webhook",
            name="last_notification",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Last Notification"
            ),
        ),
    ]