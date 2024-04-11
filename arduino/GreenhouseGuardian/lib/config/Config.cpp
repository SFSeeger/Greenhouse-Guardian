#include <FS.h>

#ifdef ESP32
#include <SPIFFS.h>
#endif

#include <ArduinoJson.h>

#include "Config.h"
#include <Error.h>

char authToken[64];
char apiUrl[64];
PlantConfig plants[NUM_PLANTS];

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
