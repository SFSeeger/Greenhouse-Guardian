#include <FS.h>          //this needs to be first, or it all crashes and burns...
#include <WiFiManager.h> //https://github.com/tzapu/WiFiManager

#ifdef ESP32
#include <SPIFFS.h>
#endif

#include <ArduinoJson.h> //https://github.com/bblanchon/ArduinoJson

#include "Error.h"
#include <Config.h>

bool shouldSaveConfig = false;

void saveConfigCallback()
{
    Serial.println("Should save config");
    shouldSaveConfig = true;
}

void handleWiFi()
{
    WiFiManager wifiManager;

    wifiManager.resetSettings();
    wifiManager.setAPStaticIPConfig(IPAddress(10, 0, 1, 1), IPAddress(10, 0, 1, 1), IPAddress(255, 255, 255, 0));
    wifiManager.setSaveConfigCallback(saveConfigCallback);

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

    strcpy(authToken, authTokenParameter.getValue());
    strcpy(apiUrl, apiUrlParameter.getValue());

    Serial.println("Got AuthToken: " + String(authToken));
    if (shouldSaveConfig)
    {
        Serial.println("Saving Config");
        JsonDocument json;
        json["authToken"] = authToken;
        json["apiUrl"] = apiUrl;

        File configFile = SPIFFS.open("/config.json", "w");
        if (!configFile)
        {
            Serial.println("failed to open config file for writing");
            displayError(FsError);
        }
        serializeJson(json, Serial);
        serializeJson(json, configFile);
        configFile.close();
    }
}
