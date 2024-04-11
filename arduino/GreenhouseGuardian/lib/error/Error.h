#ifndef ERROR_H
#define ERROR_H

enum ERROR
{
    FsError = 1,
};

void setupError();
void displayError(ERROR error);

#endif