#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

#include <WifiHandler.h>
#include <Error.h>
#include <Config.h>
#include <BoardSettings.h>
#include <Guardian.h>

void setup()
{
    Serial.begin(9600);
    Serial.println("Setup methods");
    setupError();

    setupDHT();
    setupPlants();

    pinMode(RESET_PIN, INPUT);

    Serial.println("Starting WiFi");
    handleWiFi();

    Serial.println(authToken);
    Serial.println(apiUrl);
}

void loop()
{
    if (digitalRead(RESET_PIN) == HIGH)
    {
        Serial.println("Resetting device");
        wifiManager.resetSettings();
        ESP.restart();
    }
    sendDataToServer();
    delay(1000 * 5);
}