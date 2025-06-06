from _cdolphin import registers


def read_gpr(index):
    return registers.read_gpr(index)


def read_fpr(index):
    return registers.read_fpr(index)


def write_gpr(index, value):
    registers.write_gpr(index, value)


def write_fpr(index, value):
    registers.write_fpr(index, value)