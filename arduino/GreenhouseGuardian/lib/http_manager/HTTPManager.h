#ifndef HTTPMANAGER_H
#define HTTPMANAGER_H
#include <Arduino.h>
#include <ArduinoJson.h>

void makePostRequest(const String url, const String payload, JsonDocument &json);

#endif