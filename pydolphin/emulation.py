import _cdolphin
from _cdolphin import event

def resume():
    emulation.resume()

def pause():
    emulation.pause()

# TODO: change_speed should come from emulation not _cdolphin
def change_speed(speed_percent):
    _cdolphin.change_speed(speed_percent)

def reset():
    emulation.reset()
