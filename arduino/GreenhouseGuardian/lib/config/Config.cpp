#include <FS.h>

#ifdef ESP32
#include <SPIFFS.h>
#endif

#include <ArduinoJson.h>

#include "BoardSettings.h"
#include "Config.h"
#include <Error.h>

#define FORMAT_SPIFFS_IF_FAILED true

char authToken[64];
char apiUrl[64];
PlantConfig plants[NUM_PLANTS] = {{1, PLANT_PIN_1}, {2, PLANT_PIN_2}, {3, PLANT_PIN_3}}; // Change this based on board config

void loadConfig()
{
    // SPIFFS.format();
    if (!SPIFFS.begin(FORMAT_SPIFFS_IF_FAILED))
    {
        Serial.println("failed to mount FS");
        displayError(FsError);
        return;
    }

    Serial.println("mounted file system");

    if (!SPIFFS.exists("/config.json"))
    {
        Serial.println("failed to load json config");
        displayError(FsError);
        return;
    }
    // file exists, reading and loading

    Serial.println("reading config file");
    File configFile = SPIFFS.open("/config.json", "r");
    if (configFile)
    {
        Serial.println("opened config file");
        size_t size = configFile.size();
        // Allocate a buffer to store contents of the file.
        std::unique_ptr<char[]> buf(new char[size]);
        Serial.println("Creating buffer");

        configFile.readBytes(buf.get(), size);
        Serial.println("reading file");

        JsonDocument json;
        auto deserializeError = deserializeJson(json, buf.get());
        serializeJson(json, Serial);
        if (!deserializeError)
        {
            Serial.println("\nparsed json");

            // ADD ALL CONFIG VARS HERE
            strcpy(authToken, json["authToken"]);
            strcpy(apiUrl, json["apiUrl"]);
            int i = 0;
            for (JsonObject plant : json["plants"].as<JsonArray>())
            {
                plants[i].plantId = plant["plantId"];
                plants[i].plantPin = plants[i].plantPin;
                i++;
            }
        }
        else
        {
            Serial.println("failed to load json config");
            displayError(FsError);
        }
    }
    configFile.close();
}
