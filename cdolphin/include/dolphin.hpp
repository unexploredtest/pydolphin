#pragma once

#include <string>

int run(std::string gamePath, std::string saveStatePath, bool headLess);
bool getHasPassed();
void setHasPassed(bool value);
bool getIsRunning();
void stop();