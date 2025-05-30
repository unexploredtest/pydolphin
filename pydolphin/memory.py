from _cdolphin import memory

def read_u8(addr):
    """
    Reads 1 byte as an unsigned integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_u8(addr)

def read_u16(addr):
    """
    Reads 2 byte as an unsigned integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_u16(addr)

def read_u32(addr):
    """
    Reads 4 byte as an unsigned integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_u32(addr)

def read_u64(addr):
    """
    Reads 8 byte as an unsigned integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_u64(addr)

def read_s8(addr):
    """
    Reads 1 byte as an signed integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_s8(addr)

def read_s16(addr):
    """
    Reads 2 byte as an signed integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_s16(addr)

def read_s32(addr):
    """
    Reads 4 byte as an signed integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_s32(addr)

def read_s64(addr):
    """
    Reads 8 byte as an signed integer.

    :param addr: memory address to read from
    :return: value as integer
    """
    return memory.read_s64(addr)

def read_f32(addr):
    """
    Reads 4 bytes as a floating point number.

    :param addr: memory address to read from
    :return: value as floating point number
    """
    return memory.read_f32(addr)


def read_f64(addr):
    """
    Reads 8 bytes as a floating point number.

    :param addr: memory address to read from
    :return: value as floating point number
    """
    return memory.read_f64(addr)


def write_u8(addr, value):
    """
    Writes an unsigned integer to 1 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_u8(addr, value)


def write_u16(addr, value):
    """
    Writes an unsigned integer to 2 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_u16(addr, value)

def write_u32(addr, value):
    """
    Writes an unsigned integer to 4 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_u32(addr, value)

def write_u64(addr, value):
    """
    Writes an unsigned integer to 8 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_u64(addr, value)

def write_s8(addr, value):
    """
    Writes an signed integer to 1 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_s8(addr, value)


def write_s16(addr, value):
    """
    Writes an signed integer to 2 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_s16(addr, value)

def write_s32(addr, value):
    """
    Writes an signed integer to 4 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_s32(addr, value)

def write_s64(addr, value):
    """
    Writes an signed integer to 8 byte.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as integer
    """
    memory.write_s64(addr, value)


def write_f32(addr, value):
    """
    Writes a floating point number to 4 bytes.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as floating point number
    """
    memory.write_f32(addr, value)


def write_f64(addr, value):
    """
    Writes a floating point number to 8 bytes.
    Overflowing values are truncated.

    :param addr: memory address to read from
    :param value: value as floating point number
    """
    memory.write_f64(addr, value)
