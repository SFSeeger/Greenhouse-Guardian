#ifndef CONFIG_H
#define CONFIG_H

struct PlantConfig
{
    int plantId;
    char plantName[64];
};

extern char authToken[64];
extern char apiUrl[64];
extern PlantConfig plants[NUM_PLANTS];

void loadConfig();
#endif