#include <ArduinoJson.h>
#include <HTTPClient.h>

#include <WifiHandler.h>

JsonDocument sendPostRequest(const String *url, const String payload)
{
    JsonDocument json;

    HTTPClient http;
    http.begin(String(apiUrl) + *url);
    http.addHeader("Content-Type", "application/json");
    http.addHeader("Authorization", authToken);

    int httpResponseCode = http.POST(payload);

    if (httpResponseCode > 0)
    {
        String response = http.getString();
        Serial.println(httpResponseCode);
        Serial.println(response);
        if (httpResponseCode == 200)
        {
            Serial.println("Success on sending POST");
            auto deserializeError = deserializeJson(json, response);
            if (deserializeError)
            {
                Serial.println("Failed to parse JSON");
            }
        }
    }
    else
    {
        Serial.print("Error on sending POST: ");
        Serial.println(httpResponseCode);
    }

    http.end();
    return json;
}
