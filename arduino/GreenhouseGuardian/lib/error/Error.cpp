#include <Arduino.h>
#include "Error.h"
#include <BoardSettings.h>

#ifndef LED_BUILTIN
#define LED_BUILTIN 2
#endif

void setupError()
{
    pinMode(LED_BUILTIN, OUTPUT);
}

void displayError(ERROR error)
{
    for (int i = 0; i < error; i++)
    {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(500);
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
    }
    delay(1000);
}