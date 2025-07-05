// #include "Scripting/Python/PyScriptingBackend.h"

#include <Python.h>
#include <string>
#include <thread>
#include <optional>


#include "Common/FileUtil.h"
#include "Common/Logging/Log.h"
#include "Common/StringUtil.h"

#include "Core/Config/MainSettings.h"

#include "Scripting/Python/Modules/controllermodule.h"
#include "Scripting/Python/Modules/doliomodule.h"
#include "Scripting/Python/Modules/dolphinmodule.h"
#include "Scripting/Python/Modules/eventmodule.h"
#include "Scripting/Python/Modules/emulationmodule.h"
#include "Scripting/Python/Modules/guimodule.h"
#include "Scripting/Python/Modules/memorymodule.h"
#include "Scripting/Python/Modules/registersmodule.h"
#include "Scripting/Python/Modules/savestatemodule.h"
// #include "Scripting/ScriptingEngine.h"
#include "include/dolphin.hpp"

#include "Scripting/Python/Modules/controllermodule.h"

#include "Core/API/Controller.h"
#include "Core/HW/WiimoteEmu/WiimoteEmu.h"
#include "Scripting/Python/PyScriptingBackend.h"
#include "Scripting/Python/Utils/module.h"

struct PyDolphinModuleState {
    std::optional<std::thread> dolphinThread;
};

void freeDolphin(void* self) {
    PyDolphinModuleState* state = Py::GetState<PyDolphinModuleState>(static_cast<PyObject*>(self));
    auto& dolphinThread = state->dolphinThread;

    if(dolphinThread.has_value() && dolphinThread.value().joinable()) {
        if(getDolphinState() != DS_FINISHED) {
            stopDolphin();
        }
        dolphinThread.value().join();
    }
}

// TODO: Find a better way of doing this
static bool checkBackendName(std::string backendName) {
    if(backendName == "OGL" || backendName == "Vulkan" || backendName == "default" ||
        backendName == "Software Rendering" || backendName == "Null" ||
        backendName == "Metal" || backendName == "D3D" || backendName == "D3D12") {
        
        return true;
    } else {
        return false;
    }
}

// Run dolphin, for other functions to work a little has to pass before 
// everything starts to function
static PyObject* run(PyObject* self, PyObject* args) {
    PyDolphinModuleState* state = Py::GetState<PyDolphinModuleState>(self);
    const char* gamePath;
    const char* saveStatePath;
    int headLess;
    u32 speedPercent;
    const char* backendName;
    int useDualCore;

    if (!PyArg_ParseTuple(args, "sspIsp", &gamePath, &saveStatePath, &headLess, &speedPercent, &backendName, &useDualCore)) {
        PyErr_SetString(PyExc_RuntimeError, "Wrong parameters!");
        return nullptr;
    }

    std::string gamePathS(gamePath);
    std::string saveStatePathS(saveStatePath);
    std::string backendNameS(backendName);

    if(!checkBackendName(backendNameS)) {
        PyErr_SetString(PyExc_RuntimeError, "Wrong backend name!");
        return nullptr;
    }

    if(state->dolphinThread != std::nullopt && state->dolphinThread.value().joinable()) {
        PyErr_SetString(PyExc_RuntimeError, "Dolphin already running!");
        return nullptr;
    }

    if(getDolphinState() == DS_FINISHED) {
        state->dolphinThread.value().join();
    }

    state->dolphinThread = std::thread(runDolphin, gamePathS, saveStatePathS, headLess, backendNameS, useDualCore);
    
    while(getDolphinState() == DS_INITING || getDolphinState() == DS_NONE) {
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    const float speed = float(speedPercent) / 100.0f;
    Config::SetCurrent(Config::MAIN_EMULATION_SPEED, speed);
  
    return Py_None;
}

static PyObject* stop(PyObject* self, PyObject* args) {
  PyDolphinModuleState* state = Py::GetState<PyDolphinModuleState>(self);
  auto& optionalThread = state->dolphinThread;

  if(getDolphinState() == DS_NONE) {
      PyErr_SetString(PyExc_RuntimeError, "Dolphin not running!");
      return nullptr;
  }
  
  if(getDolphinState() != DS_FINISHED) {
    stopDolphin();
  }

  // Wait until thread's work finishes
  optionalThread.value().join();
  optionalThread = std::nullopt;

  setDolphinState(DS_NONE);
  
  return Py_None;
}

// Check if dolphin is initilized, mustn't call right after the start
// as a crash would happen.
static PyObject* getIsRunningDolphin(PyObject* self, PyObject* args) {
    return PyBool_FromLong(getDolphinState() != DS_NONE);
}

static PyObject* changeSpeed(PyObject* self, PyObject* args) {
    u32 speedPercent;

    if (!PyArg_ParseTuple(args, "I", &speedPercent)) {
        PyErr_SetString(PyExc_RuntimeError, "Wrong parameters!");
    }

    const float speed = float(speedPercent) / 100.0f;
    Config::SetCurrent(Config::MAIN_EMULATION_SPEED, speed);
  
    return Py_None;
}


// Method table
static PyMethodDef DolphinMethods[] = {
    {"run", run, METH_VARARGS, "Run dolphin"},
    {"stop", stop, METH_NOARGS, "Stop dolphin"},
    {"check_init", getIsRunningDolphin, METH_NOARGS, "Check if dolphin is initialized"},
    {"change_speed", changeSpeed, METH_VARARGS, "Check if dolphin is initialized"},
    {nullptr, nullptr, 0, nullptr}  // Sentinel value
};

static struct PyModuleDef DolphinModule = {
    PyModuleDef_HEAD_INIT,
    "cdolphin",
    "A dolphin module for scripting",
    sizeof(PyDolphinModuleState*),
    DolphinMethods,
    nullptr,
    0,
    0,
    freeDolphin
};

PyMODINIT_FUNC PyInit__cdolphin(void) {
    PyObject* dolphinModule = PyModule_Create(&DolphinModule);
    if (!dolphinModule) {
        return nullptr;
    }

    PyDolphinModuleState** statePtr = static_cast<PyDolphinModuleState**>(PyModule_GetState(dolphinModule));
    *statePtr = new PyDolphinModuleState();

    PyObject* controllerModule = PyModule_Create(PyScripting::getControllerModule());
    if (!controllerModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "controller", controllerModule);

    PyObject* eventModule = PyModule_Create(PyScripting::getEventModule());
    if (!eventModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "event", eventModule);

    PyObject* emulationModule = PyModule_Create(PyScripting::getEmulationModule());
    if (!emulationModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "emulation", emulationModule);

    PyObject* GUIModule = PyModule_Create(PyScripting::getGUIModule());
    if (!GUIModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "gui", GUIModule);

    PyObject* memoryModule = PyModule_Create(PyScripting::getMemoryModule());
    if (!memoryModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "memory", memoryModule);

    PyObject* registersModule = PyModule_Create(PyScripting::getRegistersModule());
    if (!registersModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "registers", registersModule);

    PyObject* saveStateModule = PyModule_Create(PyScripting::getSaveStateModule());
    if (!saveStateModule) {
        Py_DECREF(dolphinModule);
        return nullptr;
    }
    PyModule_AddObject(dolphinModule, "savestate", saveStateModule);

    return dolphinModule;
}
