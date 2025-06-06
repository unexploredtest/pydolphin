from _cdolphin import memory

def read_u8(addr):
    return memory.read_u8(addr)

def read_u16(addr):
    return memory.read_u16(addr)

def read_u32(addr):
    return memory.read_u32(addr)

def read_u64(addr):
    return memory.read_u64(addr)

def read_s8(addr):
    return memory.read_s8(addr)

def read_s16(addr):
    return memory.read_s16(addr)

def read_s32(addr):
    return memory.read_s32(addr)

def read_s64(addr):
    return memory.read_s64(addr)

def read_f32(addr):
    return memory.read_f32(addr)


def read_f64(addr):
    return memory.read_f64(addr)


def write_u8(addr, value):
    memory.write_u8(addr, value)


def write_u16(addr, value):
    memory.write_u16(addr, value)

def write_u32(addr, value):
    memory.write_u32(addr, value)

def write_u64(addr, value):
    memory.write_u64(addr, value)

def write_s8(addr, value):
    memory.write_s8(addr, value)


def write_s16(addr, value):
    memory.write_s16(addr, value)

def write_s32(addr, value):
    memory.write_s32(addr, value)

def write_s64(addr, value):
    memory.write_s64(addr, value)


def write_f32(addr, value):

    memory.write_f32(addr, value)


def write_f64(addr, value):
    memory.write_f64(addr, value)
