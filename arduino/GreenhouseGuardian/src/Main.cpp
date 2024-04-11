#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

#include <WifiHandler.h>
#include <Error.h>
#include <Config.h>
#include <BoardSettings.h>

void setup()
{
    Serial.begin(9600);
    Serial.println("Setup methods");
    setupError();
    loadConfig();
    setupUserPins();

    Serial.println("Starting WiFi");
    handleWiFi();
}

void loop()
{
}