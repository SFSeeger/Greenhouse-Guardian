# Generated by Django 5.0.4 on 2024-04-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guardian", "0002_device_device_token"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="device",
            name="humidity_limit",
        ),
        migrations.RemoveField(
            model_name="device",
            name="temperature_limit",
        ),
        migrations.RemoveField(
            model_name="plant",
            name="humidity_limit",
        ),
        migrations.RemoveField(
            model_name="plantentry",
            name="temperature",
        ),
        migrations.AddField(
            model_name="device",
            name="humidity_limit_max",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Maximum Humidity"
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="humidity_limit_min",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Minimum Humidity"
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="temperature_limit_max",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Maximum Temperature"
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="temperature_limit_min",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Minimum Temperature"
            ),
        ),
        migrations.AddField(
            model_name="plant",
            name="humidity_limit_max",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Maximum Humidity"
            ),
        ),
        migrations.AddField(
            model_name="plant",
            name="humidity_limit_min",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Minimum Humidity"
            ),
        ),
    ]
