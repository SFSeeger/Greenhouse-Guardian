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

    Serial.println("Starting WiFi");
    handleWiFi();

    Serial.println(authToken);
    Serial.println(apiUrl);
}

void loop()
{
    sendDataToServer();
    delay(1000 * 10);
}