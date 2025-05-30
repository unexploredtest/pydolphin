import asyncio
from _cdolphin import event

# def create_frameadvance():
#     def frameadvance_callback():
#         return

#     async def frameadvance():
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(None, event.on_single_frameadvance, frameadvance_callback)
#         return

#     return frameadvance
def create_frameadvance():
    state = {
        'result': False
    }

    def frameadvance_callback():
        state['result'] = True
    
    async def wait_for_callback():
        event.on_single_frameadvance(frameadvance_callback)
        while(not state['result']):
            await asyncio.sleep(0)

    async def frameadvance():
        state['result'] = False
        await wait_for_callback()
        return state['frame_drawn_result']

    return frameadvance

def create_framedrawn():
    state = {
        'frame_drawn_result': (None, None, None),
        'result': False
    }

    def framedrawn_callback(width, height, data):
        state['frame_drawn_result'] = (width, height, data)
        state['result'] = True
    
    async def wait_for_callback():
        event.on_single_framedrawn(framedrawn_callback)
        while(not state['result']):
            await asyncio.sleep(0)

    async def framedrawn():
        state['result'] = False
        await wait_for_callback()
        return state['frame_drawn_result']

    return framedrawn

def create_memorybreakpoint():
    state = {
        'memory_break_point_result': (None, None, None),
        'result': False
    }

    def memorybreakpoint_callback(is_write, addr, value):
        state['memory_break_point_result'] = (is_write, addr, value)
        state['result'] = True
    
    async def wait_for_callback():
        event.on_single_memorybreakpoint(memorybreakpoint_callback)
        while(not state['result']):
            await asyncio.sleep(0)

    async def memorybreakpoint():
        state['result'] = False
        await wait_for_callback()
        return state['frame_drawn_result']

    return memorybreakpoint


# def create_memorybreakpoint():
#     state = {
#         'memory_break_point_result': (None, None, None),
#         'result': False
#     }

#     def memorybreakpoint_callback(is_write, addr, value):
#         state['memory_break_point_result'] = (is_write, addr, value)
#         state['result'] = True

#     async def memorybreakpoint():
#         state['result'] = False
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(None, event.on_single_memorybreakpoint, memorybreakpoint_callback)
#         return state['memory_break_point_result']

#     return memorybreakpoint

def create_codebreakpoint():
    state = {
        'code_break_point_result': None,
        'result': False
    }

    def codebreakpoint_callback(addr):
        state['code_break_point_result'] = addr
        state['result'] = True
    
    async def wait_for_callback():
        event.on_single_codebreakpoint(codebreakpoint_callback)
        while(not state['result']):
            await asyncio.sleep(0)

    async def codebreakpoint():
        state['result'] = False
        await wait_for_callback()
        return state['frame_drawn_result']

    return codebreakpoint


# def create_codebreakpoint():
#     state = {
#         'code_break_point_result': None,
#         'result': False
#     }

#     def codebreakpoint_callback(addr):
#         state['code_break_point_result'] = addr
#         state['result'] = True

#     async def codebreakpoint():
#         state['result'] = False
#         loop = asyncio.get_event_loop()
#         await loop.run_in_executor(None, event.on_single_codebreakpoint, codebreakpoint_callback)
#         return state['code_break_point_result']

#     return codebreakpoint