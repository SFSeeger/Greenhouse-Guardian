#include <FS.h>

#ifdef ESP32
#include <SPIFFS.h>
#endif

#include <ArduinoJson.h>

#include "BoardSettings.h"
#include "Config.h"
#include <Error.h>

char authToken[64];
char apiUrl[64];
PlantConfig plants[NUM_PLANTS] = {{0, PLANT_PIN_1}, {0, PLANT_PIN_2}, {0, PLANT_PIN_3}}; // Change this based on board config

void loadPlants(PlantConfig *plants, JsonDocument &json)
{
    for (int i = 0; i < NUM_PLANTS; i++)
    {
        plants[i].plantId = json["plants"][i]["plantId"];
        plants[i].plantPin = json["plants"][i]["plantPin"];
    }
}

void loadConfig()
{
    // SPIFFS.format();
    if (SPIFFS.begin())
    {
        Serial.println("mounted file system");
        if (SPIFFS.exists("/config.json"))
        {
            // file exists, reading and loading
            Serial.println("reading config file");
            File configFile = SPIFFS.open("/config.json", "r");
            if (configFile)
            {
                Serial.println("opened config file");
                size_t size = configFile.size();
                // Allocate a buffer to store contents of the file.
                std::unique_ptr<char[]> buf(new char[size]);

                configFile.readBytes(buf.get(), size);

                JsonDocument json;
                auto deserializeError = deserializeJson(json, buf.get());
                serializeJson(json, Serial);
                if (!deserializeError)
                    Serial.println("\nparsed json");

                // ADD ALL CONFIG VARS HERE
                strcpy(authToken, json["authToken"]);
                strcpy(apiUrl, json["apiUrl"]);
                loadPlants(plants, json);
            }
            else
            {
                Serial.println("failed to load json config");
                displayError(FsError);
            }
            configFile.close();
        }
    }
    else
    {
        Serial.println("failed to mount FS");
        displayError(FsError);
    }
}
