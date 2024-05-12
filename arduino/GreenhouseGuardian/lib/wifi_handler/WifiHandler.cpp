#include <FS.h>          //this needs to be first, or it all crashes and burns...
#include <WiFiManager.h> //https://github.com/tzapu/WiFiManager

#ifdef ESP32
#include <SPIFFS.h>
#endif

#include <ArduinoJson.h> //https://github.com/bblanchon/ArduinoJson

#include "Error.h"
#include <Config.h>
#include <HTTPManager.h>

WiFiManager wifiManager;

bool shouldSaveConfig = false;

void handleWiFi()
{
    loadConfig();

    // wifiManager.resetSettings();
    wifiManager.setAPStaticIPConfig(IPAddress(10, 0, 1, 1), IPAddress(10, 0, 1, 1), IPAddress(255, 255, 255, 0));

    Serial.println(authToken);
    Serial.println(apiUrl);

    WiFiManagerParameter authTokenParameter("authToken", "API auth token", authToken, sizeof(authToken) / sizeof(char), "required");
    WiFiManagerParameter apiUrlParameter("apiURL", "API Url", apiUrl, sizeof(apiUrl) / sizeof(char), "required");

    wifiManager.addParameter(&authTokenParameter);
    wifiManager.addParameter(&apiUrlParameter);

    if (!wifiManager.autoConnect("Greenhouse Guardian Device"))
    {
        Serial.println("failed to connect and hit timeout");
        delay(3000);
        ESP.restart();
        delay(5000);
    }

    const char *newApiToken = authTokenParameter.getValue();
    const char *newApiUrl = apiUrlParameter.getValue();

    if ((*newApiToken > 0 || *newApiUrl > 0) && (strcmp(authToken, newApiToken) != 0 || strcmp(apiUrl, newApiUrl) != 0))
    {
        Serial.println("New Config Detected");
        shouldSaveConfig = true;
    }

    Serial.println("Should save config: " + String(shouldSaveConfig));
    if (shouldSaveConfig)
    {
        Serial.println("Got AuthToken: " + String(authToken));

        strcpy(authToken, newApiToken);
        strcpy(apiUrl, newApiUrl);

        Serial.println("getting plant ids");
        // Create Plants on server. Send ids to prevent duplicates
        JsonDocument response;
        String body = "[";
        for (int i = 0; i < NUM_PLANTS; i++)
        {
            body += "{\"id\":" + String(plants[i].plantId) + ",";
            body += "\"name\":\"Plant " + String(i) + "\"}";
            if (i != NUM_PLANTS - 1)
            {
                body += ",";
            }
        }
        body += "]";

        makePostRequest("/plant/mass-create/", body, response);
        JsonArray ids = response["ids"].as<JsonArray>();
        for (unsigned i = 0; i < NUM_PLANTS; i++)
        {
            plants[i].plantId = ids[i];
        }

        Serial.println("Saving Config");
        JsonDocument json;
        json["authToken"] = authToken;
        json["apiUrl"] = apiUrl;
        JsonArray plantsArray = json["plants"].to<JsonArray>();
        for (int i = 0; i < NUM_PLANTS; i++)
        {
            JsonObject plant = plantsArray.add<JsonObject>();
            plant["plantId"] = plants[i].plantId;
            plant["plantPin"] = plants[i].plantPin;
        }
        if (SPIFFS.begin())
        {
            File configFile = SPIFFS.open("/config.json", "w");
            if (!configFile)
            {
                Serial.println("failed to open config file for writing");
                displayError(FsError);
            }
            serializeJson(json, Serial);
            serializeJson(json, configFile);
            configFile.flush();
            configFile.close();
        }
    }
}
