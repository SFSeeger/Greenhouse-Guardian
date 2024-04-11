#ifndef CONFIG_H
#define CONFIG_H
#define DHTTYPE DHT11

struct PlantConfig
{
    int plantId;
    int plantPin;
};

extern char authToken[64];
extern char apiUrl[64];

#define NUM_PLANTS 3   // TODO: Change this based on flash
#define SENSOR_DRY 400 // TODO: Determine value
#define SENSOR_WET 273 // TODO: Determine value

extern PlantConfig plants[NUM_PLANTS];

void loadConfig();
#endif