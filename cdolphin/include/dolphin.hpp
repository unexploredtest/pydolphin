#pragma once

#include <string>

enum DolphinState {
    DS_NONE,
    DS_INITING,
    DS_RUNNING,
    DS_FINISHED
};

DolphinState getDolphinState();
void setDolphinState(DolphinState state);

int runDolphin(std::string gamePath, std::string saveStatePath, bool headLess);
void stopDolphin();