#include <Config.h>
#include <HTTPManager.h>
#include <Error.h>
#include <BoardSettings.h>
#include <ArduinoJson.h>
#include <DHT.h>

DHT dht1(DHT_1_PIN, DHTTYPE);
DHT dht2(DHT_2_PIN, DHTTYPE);

void setupDHT()
{
    dht1.begin();
    dht2.begin();
}

void setupPlants()
{
    for (unsigned i = 0; i < NUM_PLANTS; i++)
    {
        pinMode(plants[i].plantPin, INPUT);
    }
}

float readTemperature()
{
    float t1 = dht1.readTemperature();
    float t2 = dht2.readTemperature();

    if (isnan(t1) || isnan(t2))
    {
        displayError(DHT_Error);
        return -1;
    }
    return (t1 + t2) / 2;
}
float readHumidity()
{
    float h1 = dht1.readHumidity();
    float h2 = dht2.readHumidity();

    if (isnan(h1) || isnan(h2))
    {
        displayError(DHT_Error);
        return -1;
    }
    return (h1 + h2) / 2;
}

long readPlantData(const unsigned plant_idx)
{
    unsigned soil_moisture = analogRead(plants[plant_idx].plantPin);
    return map(soil_moisture, SENSOR_WET, SENSOR_DRY, 100, 0);
}

void sendDataToServer()
{
    JsonDocument response;
    JsonDocument body;
    String bodyStr;
    body["temperature"] = readTemperature();
    body["humidity"] = readHumidity();
    JsonArray plantentry_set = body["plantenry_set"].to<JsonArray>();
    for (unsigned plant_idx = 0; plant_idx < NUM_PLANTS; plant_idx++)
    {
        JsonObject plantentry;
        plantentry["plant"] = plants[plant_idx].plantId;
        plantentry["humidity"] = readPlantData(plant_idx);
        plantentry_set.add(plantentry);
    }
    serializeJson(body, bodyStr);
    makePostRequest("/entry/", bodyStr, response);
}