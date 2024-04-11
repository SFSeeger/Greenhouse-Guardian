#ifndef ERROR_H
#define ERROR_H

enum ERROR
{
    FsError = 1,
    DHT_Error = 2,
};

void setupError();
void displayError(ERROR error);

#endif