#include <Arduino.h>
#include "BoardSettings.h"

void setupUserPins()
{
    // Register Plants here:
    pinMode(PLANT_PIN_1, INPUT);
    pinMode(PLANT_PIN_2, INPUT);
    pinMode(PLANT_PIN_3, INPUT);
}