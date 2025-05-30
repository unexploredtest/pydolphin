from _cdolphin import controller

def get_gc_buttons(controller_id):
    return controller.get_gc_buttons(controller_id)

def set_gc_buttons(controller_id, inputs):
    controller.set_gc_buttons(controller_id, inputs)


def get_wiimote_buttons(controller_id):
    return controller.get_wiimote_buttons(controller_id)


def set_wiimote_buttons(controller_id, inputs):
    controller.set_wiimote_buttons(controller_id, inputs)


def get_wiimote_pointer(controller_id):
    """
    Returns the current wii pointer position, in screen coordinates.
    For x, -1 and 1 represent the left and right edge of the screen.
    For y, -1 and 1 represent the bottom and top edge of the screen.
    The x and y values are allowed to exceed the [-1, 1] range.
    :param controller_id: 0-based index of the controller
    :return: The screen coordinates as a tuple (x, y)
    """
    return controller.get_wiimote_pointer(controller_id)


def set_wiimote_pointer(controller_id, x, y):
    """
    Sets the current wii pointer position, in screen coordinates.

    | For x, -1 and 1 represent the left and right edge of the screen.
    | For y, -1 and 1 represent the bottom and top edge of the screen.
    The x and y values are allowed to exceed the [-1, 1] range.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: horizontal screen coordinate, where positive means right
    :param y: vertical screen coordinate, where positive means up
    """
    controller.set_wiimote_pointer(controller_id, x, y)


def get_wiimote_acceleration(controller_id):
    """
    Returns the current wii remote acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    :param controller_id: 0-based index of the controller
    :return: The current acceleration as a tuple (x, y, z)
    """
    return controller.get_wiimote_acceleration(controller_id)


def set_wiimote_acceleration(controller_id: int, x, y, z):
    """
    Sets the current wii remote acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    This function overrides set_wiimote_shake and set_wiimote_swing.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the acceleration vector
    :param y: y-component of the acceleration vector
    :param z: z-component of the acceleration vector
    """
    controller.set_wiimote_acceleration(controller_id, x, y, z)


def get_wiimote_angular_velocity(controller_id):
    """
    Returns the current wii remote angular velocity, as a vector (x, y, z).
    The angular velocity is measured in radians/s.
    :param controller_id: 0-based index of the controller
    :return: The current angular velocity as a tuple (x, y, z)
    """
    return controller.get_wiimote_angular_velocity(controller_id)


def set_wiimote_angular_velocity(controller_id, x, y, z) -> None:
    """
    Sets the current wii remote angular velocity, as a vector (x, y, z).
    The angular velocity is measured in radians/s.
    This function overrides set_wiimote_tilt and set_wiimote_swing.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the angular velocity vector
    :param y: y-component of the angular velocity vector
    :param z: z-component of the angular velocity vector
    """
    controller.set_wiimote_angular_velocity(controller_id, x, y, z)


def get_wii_classic_buttons(controller_id):
    """
    Retrieves the current input map for the given Wii Classic controller.
    All keys of :class:`WiiClassicInputs` will be present in the returned
    dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """
    return controller.get_wii_classic_buttons(controller_id)


def set_wii_classic_buttons(controller_id, inputs):
    """
    Sets the current input map for the given Wii Classic controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the A button like this::

        controller.set_wii_classic_buttons(0, {"A": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """
    controller.set_wii_classic_buttons(controller_id, inputs)


def get_wiimote_swing(controller_id):
    """
    Returns the current wii remote swing state, as a vector (x, y, z, distance, speed, return_speed, angle).
    The angle is measured in radians. The distances are in meters.
    :param controller_id: 0-based index of the controller
    :return: The current swing state as a tuple (x, y, z, distance, speed, return_speed, angle)
    """
    return controller.get_wiimote_swing(controller_id)


def set_wiimote_swing(controller_id, x, y, z, distance, speed, return_speed, angle):
    """
    Sets the wii remote swing motion.
    This function is overridden by set_wiimote_acceleration and set_wiimote_angular_velocity.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the swing
    :param y: y-component of the swing
    :param z: z-component of the swing
    :param distance: distance of the swing (m)
    :param speed: speed of the swing (m/s)
    :param return_speed: return speed of the swing (m/s)
    :param angle: angle of the swing (rad)
    """
    controller.set_wii_classic_buttons(controller_id, x, y, z, distance, speed, return_speed, angle)


def get_wiimote_shake(controller_id):
    """
    Returns the current wii remote shake state, as a vector (x, y, z, intensity, frequency).
    The intensity is in meters, and the frequency in Hertz.
    :param controller_id: 0-based index of the controller
    :return: The current swing state as a tuple (x, y, z, intensity, frequency)
    """
    return controller.get_wiimote_swing(controller_id)


def set_wiimote_shake(controller_id, x, y, z, intensity, frequency):
    """
    Sets the wii remote shake motion.
    This function is overridden by set_wiimote_acceleration.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the shake
    :param y: y-component of the shake
    :param z: z-component of the shake
    :param intensity: intensity of the shake (m)
    :param frequency: frequency of the shake (Hz)
    """
    controller.set_wiimote_shake(controller_id, x, y, z, intensity, frequency)


def get_wiimote_tilt(controller_id):
    """
    Returns the current wii remote tilt motion state, as a vector (x, y, angle, velocity).
    The angle is in rad, and the velocity in rad/s
    :param controller_id: 0-based index of the controller
    :return: The current swing state as a tuple (x, y, angle, velocity)
    """
    return controller.get_wiimote_tilt(controller_id)


def set_wiimote_tilt(controller_id, x, y, angle, velocity):
    """
    Sets the wii remote tilt motion.
    This function is overridden by set_wiimote_angular_velocity.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the tilt
    :param y: y-component of the tilt
    :param angle: max tilt angle (rad)
    :param velocity: rotational velocity of the tilt (rad/s)
    """
    controller.set_wiimote_tilt(controller_id, x, y, angle, velocity)


def get_wii_nunchuk_buttons(controller_id):
    """
    Retrieves the current input map for the given Wii Nunchuk controller.
    All keys of :class:`WiiNunchukInputs` will be present in the returned
    dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """
    return controller.get_wii_nunchuk_buttons(controller_id)


def set_wii_nunchuk_buttons(controller_id, inputs):
    """
    Sets the current input map for the given Wii Nunchuk controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the C button like this::

        controller.set_wii_nunchuk_buttons(0, {"C": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """
    controller.set_wii_nunchuk_buttons(controller_id, inputs)


def get_wii_nunchuk_acceleration(controller_id):
    """
    Returns the current wii nunchuk acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    :param controller_id: 0-based index of the controller
    :return: The current acceleration as a tuple (x, y, z)
    """
    return controller.get_wii_nunchuk_acceleration(controller_id)


def set_wii_nunchuk_acceleration(controller_id, x, y, z):
    """
    Sets the current wii nunchuk acceleration, as a vector (x, y, z).
    The acceleration is measured in m/s².
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the acceleration vector
    :param y: y-component of the acceleration vector
    :param z: z-component of the acceleration vector
    """
    controller.set_wii_nunchuk_buttons(controller_id, x, y, z)


def get_wii_nunchuk_swing(controller_id):
    """
    Returns the current wii nunchuk swing state, as a vector (x, y, z, distance, speed, return_speed, angle).
    The angle is measured in radians. The distances are in meters.
    :param controller_id: 0-based index of the controller
    :return: The current swing state as a tuple (x, y, z, distance, speed, return_speed, angle)
    """
    return controller.get_wii_nunchuk_swing(controller_id)


def set_wii_nunchuk_swing(controller_id, x, y, z, distance, speed, return_speed, angle):
    """
    Sets the wii nunchuk swing motion.
    This function is overridden by set_wii_nunchuk_acceleration and set_wii_nunchuk_angular_velocity.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the swing
    :param y: y-component of the swing
    :param z: z-component of the swing
    :param distance: distance of the swing (m)
    :param speed: speed of the swing (m/s)
    :param return_speed: return speed of the swing (m/s)
    :param angle: angle of the swing (rad)
    """
    controller.set_wii_nunchuk_swing(controller_id, x, y, z, distance, speed, return_speed, angle)


def get_wii_nunchuk_shake(controller_id):
    """
    Returns the current wii nunchuk shake state, as a vector (x, y, z, intensity, frequency).
    The intensity is in meters, and the frequency in Hertz.
    :param controller_id: 0-based index of the controller
    :return: The current swing state as a tuple (x, y, z, intensity, frequency)
    """
    return controller.get_wii_nunchuk_shake(controller_id)


def set_wii_nunchuk_shake(controller_id, x, y, z, intensity, frequency):
    """
    Sets the wii nunchuk shake motion.
    This function is overridden by set_wii_nunchuk_acceleration.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the shake
    :param y: y-component of the shake
    :param z: z-component of the shake
    :param intensity: intensity of the shake (m)
    :param frequency: frequency of the shake (Hz)
    """
    controller.set_wii_nunchuk_shake(controller_id, x, y, z, intensity, frequency)


def get_wii_nunchuk_tilt(controller_id):
    """
    Returns the current wii nunchuk tilt motion state, as a vector (x, y, angle, velocity).
    The angle is in rad, and the velocity in rad/s
    :param controller_id: 0-based index of the controller
    :return: The current swing state as a tuple (x, y, angle, velocity)
    """
    return controller.get_wii_nunchuk_tilt(controller_id)


def set_wii_nunchuk_tilt(controller_id, x, y, angle, velocity):
    """
    Sets the wii nunchuk tilt motion.
    This function is overridden by set_wii_nunchuk_angular_velocity.
    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param x: x-component of the tilt
    :param y: y-component of the tilt
    :param angle: max tilt angle (rad)
    :param velocity: rotational velocity of the tilt (rad/s)
    """
    controller.set_wii_nunchuk_tilt(controller_id, x, y, angle, velocity)


def get_gba_buttons(controller_id):
    """
    Retrieves the current input map for the given GameBoy Advance controller.
    All keys of :class:`GBAInputs` will be present in the returned dictionary.
    :param controller_id: 0-based index of the controller
    :return: dictionary describing the current input map
    """
    return controller.get_gba_buttons(controller_id)


def set_gba_buttons(controller_id, inputs):
    """
    Sets the current input map for the given GameBoy Advance controller.

    All input keys omitted from the input map will not be applied
    and therefore stay in their current state.
    For example, you may only set the A button like this::

        controller.set_gba_buttons(0, {"A": True})

    The override will hold for the current frame.
    :param controller_id: 0-based index of the controller
    :param inputs: dictionary describing the input map
    """
    controller.set_gba_buttons(controller_id, x, y, angle, velocity)