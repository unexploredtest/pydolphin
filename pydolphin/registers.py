from _cdolphin import registers


def read_gpr(index):
    """
    Returns the value contained in general purpose register at index.
    
    :param index: index of the gpr to read from (0-31)
    :return: value as integer
    """
    return registers.read_gpr(index)


def read_fpr(index):
    """
    Returns the value contained in floating point register at index.
    
    :param index: index of the fpr to read from (0-31)
    :return: value as float
    """
    return registers.read_fpr(index)


def write_gpr(index, value):
    """
    Writes value to general purpose register at index.
    
    :param index: index of the gpr to write to (0-31)
    :param value: the value to write
    """
    registers.write_gpr(index, value)


def write_fpr(index, value):
    """
    Writes value to floating point register at index.
    
    :param index: index of the fpr to write to (0-31)
    :param value: the value to write
    """
    registers.write_fpr(index, value)