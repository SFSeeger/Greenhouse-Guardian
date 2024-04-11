#ifndef BOARD_SETTINGS_H
#define BOARD_SETTINGS_H

#ifdef BOARD_ESP32
#include "Settings_esp32.h"
#endif

#ifdef BOARD_ESP8266
#include "Settings_esp_8266.h"
#endif

#define NUM_PLANTS 3 // TODO: Change this based on flash

void setupUserPins();

#endif