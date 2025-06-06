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
    return controller.get_wiimote_pointer(controller_id)

def set_wiimote_pointer(controller_id, x, y):
    controller.set_wiimote_pointer(controller_id, x, y)

def get_wiimote_acceleration(controller_id):
    return controller.get_wiimote_acceleration(controller_id)

def set_wiimote_acceleration(controller_id, x, y, z):
    controller.set_wiimote_acceleration(controller_id, x, y, z)

def get_wiimote_angular_velocity(controller_id):
    return controller.get_wiimote_angular_velocity(controller_id)

def set_wiimote_angular_velocity(controller_id, x, y, z):
    controller.set_wiimote_angular_velocity(controller_id, x, y, z)

def get_wii_classic_buttons(controller_id):
    return controller.get_wii_classic_buttons(controller_id)

def set_wii_classic_buttons(controller_id, inputs):
    controller.set_wii_classic_buttons(controller_id, inputs)

def get_wiimote_swing(controller_id):
    return controller.get_wiimote_swing(controller_id)

def set_wiimote_swing(controller_id, x, y, z, distance, speed, return_speed, angle):
    controller.set_wii_classic_buttons(controller_id, x, y, z, distance, speed, return_speed, angle)

def get_wiimote_shake(controller_id):
    return controller.get_wiimote_swing(controller_id)

def set_wiimote_shake(controller_id, x, y, z, intensity, frequency):
    controller.set_wiimote_shake(controller_id, x, y, z, intensity, frequency)

def get_wiimote_tilt(controller_id):
    return controller.get_wiimote_tilt(controller_id)

def set_wiimote_tilt(controller_id, x, y, angle, velocity):
    controller.set_wiimote_tilt(controller_id, x, y, angle, velocity)

def get_wii_nunchuk_buttons(controller_id):
    return controller.get_wii_nunchuk_buttons(controller_id)

def set_wii_nunchuk_buttons(controller_id, inputs):
    controller.set_wii_nunchuk_buttons(controller_id, inputs)

def get_wii_nunchuk_acceleration(controller_id):
    return controller.get_wii_nunchuk_acceleration(controller_id)

def set_wii_nunchuk_acceleration(controller_id, x, y, z):
    controller.set_wii_nunchuk_buttons(controller_id, x, y, z)

def get_wii_nunchuk_swing(controller_id):
    return controller.get_wii_nunchuk_swing(controller_id)

def set_wii_nunchuk_swing(controller_id, x, y, z, distance, speed, return_speed, angle):
    controller.set_wii_nunchuk_swing(controller_id, x, y, z, distance, speed, return_speed, angle)

def get_wii_nunchuk_shake(controller_id):
    return controller.get_wii_nunchuk_shake(controller_id)

def set_wii_nunchuk_shake(controller_id, x, y, z, intensity, frequency):
    controller.set_wii_nunchuk_shake(controller_id, x, y, z, intensity, frequency)

def get_wii_nunchuk_tilt(controller_id):
    return controller.get_wii_nunchuk_tilt(controller_id)

def set_wii_nunchuk_tilt(controller_id, x, y, angle, velocity):
    controller.set_wii_nunchuk_tilt(controller_id, x, y, angle, velocity)

def get_gba_buttons(controller_id):
    return controller.get_gba_buttons(controller_id)

def set_gba_buttons(controller_id, inputs):
    controller.set_gba_buttons(controller_id, x, y, angle, velocity)
