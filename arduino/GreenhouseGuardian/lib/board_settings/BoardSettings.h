#ifndef BOARD_SETTINGS_H
#define BOARD_SETTINGS_H

#ifdef BOARD_ESP_WROOM_32
#include "Settings_espwroom32.h"
#endif

#ifdef BOARD_ESP32
#include "Settings_esp32.h"
#endif

#ifdef BOARD_ESP8266
#include "Settings_esp8266.h"
#endif

void setupUserPins();

#endif