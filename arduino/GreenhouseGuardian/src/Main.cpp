#include <Arduino.h>
#include <WiFiManager.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

WiFiManager wifiManager;

void setup()
{
    wifiManager.autoConnect("Greenhouse Guardian Device");
}

void loop()
{
}