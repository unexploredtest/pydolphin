// #include "Scripting/Python/PyScriptingBackend.h"

#include <Python.h>
#include <string>
#include <thread>
#include <optional>


#include "Common/FileUtil.h"
#include "Common/Logging/Log.h"
#include "Common/StringUtil.h"

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
        stop();
        dolphinThread.value().join();
    }
}

// static int dolphinClear(PyObject *self) {
//     std::cout << "xd?\n";
//     PyDolphinModuleState* state = Py::GetState<PyDolphinModuleState>(self);
//     state->~PyDolphinModuleState();
//     return 0;
// }

// std::thread dolphinThread;

// Run dolphin, for other functions to work a little has to pass before 
// everything starts to function
static PyObject* runDolphin(PyObject* self, PyObject* args) {
    PyDolphinModuleState* state = Py::GetState<PyDolphinModuleState>(self);
    const char* gamePath;
    const char* saveStatePath;
    int headLess;

    if(state->dolphinThread != std::nullopt && state->dolphinThread.value().joinable()) {
        PyErr_SetString(PyExc_RuntimeError, "Dolphin already running!");
        return nullptr;
    }

    if (!PyArg_ParseTuple(args, "ssp", &gamePath, &saveStatePath, &headLess)) {
        PyErr_SetString(PyExc_RuntimeError, "Wrong parameters!");
    }

    std::string gamePathS(gamePath);
    std::string saveStatePathS(saveStatePath);

    setHasPassed(false);
    state->dolphinThread = std::thread(run, gamePathS, saveStatePathS, headLess);
    while(!getHasPassed()) {
        if(!state->dolphinThread.value().joinable()) {
            break;
        }
        std::this_thread::sleep_for(std::chrono::seconds(10));
    }
    // std::this_thread::sleep_for(std::chrono::seconds(10));
    // run(gamePathS, saveStatePathS);
  
    return Py_None;
}

static PyObject* stopDolphin(PyObject* self, PyObject* args) {
  PyDolphinModuleState* state = Py::GetState<PyDolphinModuleState>(self);
  // Check if dolphin's thread is running at all.
  auto& optionalThread = state->dolphinThread;
  bool isThereAThread = false;
  if(optionalThread.has_value()) {
    isThereAThread = true;
  }

  if (!isThereAThread ||  (isThereAThread && !optionalThread.value().joinable())) {
      PyErr_SetString(PyExc_RuntimeError, "Dolphin not running!");
      return nullptr;
  }
  
  if(getIsRunning()) {
    stop();
  }

  // Wait until thread's work finishes
  optionalThread.value().join();
  optionalThread = std::nullopt;
  
  return Py_None;
}

// Check if dolphin is initilized, mustn't call right after the start
// as a crash would happen.
static PyObject* getIsRunningDolphin(PyObject* self, PyObject* args) {
    return PyBool_FromLong(getIsRunning());
}


// Method table
static PyMethodDef DolphinMethods[] = {
    {"run", runDolphin, METH_VARARGS, "Run dolphin"},
    {"stop", stopDolphin, METH_NOARGS, "Stop dolphin"},
    {"check_init", getIsRunningDolphin, METH_NOARGS, "Check if dolphin is initialized"},
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

// static auto lol = PyScripting::getEventModule();
// PyObject* child_module = PyModuleDef_Init(&lol);
// if (!child_module) {
//     Py_DECREF(dolphinModule);
//     return nullptr;
// }

// PyObject* child_module = PyScripting::PyInit_event();

// PyModule_AddObject(dolphinModule, "child", child_module);