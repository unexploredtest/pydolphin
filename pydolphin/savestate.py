from _cdolphin import savestate


def save_to_slot(slot):
    """
    Saves a savestate to the given slot.
    The slot number must be between 0 and 99.
    """
    return savestate.save_to_slot(slot)


def save_to_file(filename):
    """
    Saves a savestate to the given file.
    """
    savestate.save_to_file(filename)


def save_to_bytes():
    """
    Saves a savestate and returns it as bytes.
    """
    return savestate.save_to_bytes()


def load_from_slot(slot):
    """
    Loads a savestate from the given slot.
    The slot number must be between 0 and 99.
    """
    savestate.load_from_slot(slot)


def load_from_file(filename):
    """
    Loads a savestate from the given file.
    """
    savestate.load_from_file(filename)


def load_from_bytes(state_bytes):
    """
    Loads a savestate from the given bytes.
    """
    savestate.load_from_bytes(state_bytes)
