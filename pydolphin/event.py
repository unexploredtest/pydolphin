from _cdolphin import event
import pydolphin.event_async_creator as event_async_creator

import asyncio

    # Py::MakeMethodDef<PyFrameAdvanceEvent::AddCallback>("on_frameadvance"),
    # Py::MakeMethodDef<PyFrameAdvanceEvent::AddSingleUseCallback>("on_single_frameadvance"),
    # Py::MakeMethodDef<PyMemoryBreakpointEvent::AddCallback>("on_memorybreakpoint"),
    # Py::MakeMethodDef<PyMemoryBreakpointEvent::AddSingleUseCallback>("on_single_memorybreakpoint"),
    # Py::MakeMethodDef<PyCodeBreakpointEvent::AddCallback>("on_codebreakpoint"),
    # Py::MakeMethodDef<PyCodeBreakpointEvent::AddSingleUseCallback>("on_single_codebreakpoint"),
    # Py::MakeMethodDef<PyFrameDrawnEvent::AddCallback>("on_framedrawn"),
    # Py::MakeMethodDef<PyFrameDrawnEvent::AddSingleUseCallback>("on_single_framedrawn"),

def on_frameadvance(callback):
    event.on_frameadvance(callback)

def on_single_frameadvance(callback):
    event.on_single_frameadvance(callback)

def on_memorybreakpoint(callback):
    event.on_memorybreakpoint(callback)

def on_single_memorybreakpoint(callback):
    event.on_single_memorybreakpoint(callback)

def on_codebreakpoint(callback):
    event.on_codebreakpoint(callback)

def on_single_codebreakpoint(callback):
    event.on_single_codebreakpoint(callback)

def on_framedrawn(callback):
    event.on_framedrawn(callback)

def on_single_framedrawn(callback):
    event.on_single_framedrawn(callback)

def reset():
    event._dolphin_reset()


frameadvance = event_async_creator.create_frameadvance()
framedrawn = event_async_creator.create_framedrawn()
memorybreakpoint = event_async_creator.create_memorybreakpoint()
codebreakpoint = event_async_creator.create_codebreakpoint()