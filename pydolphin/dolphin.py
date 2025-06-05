import _cdolphin
from _cdolphin import emulation

def run(game_path, save_state_path="", head_less=False, speed_percent=100, backend="default"):
    _cdolphin.run(game_path, save_state_path, head_less, speed_percent, backend)

def stop():
    _cdolphin.stop()

def resume():
    emulation.resume()

def pause():
    emulation.pause()

def check_init():
    return _cdolphin.check_init()

def change_speed(speed_percent):
    _cdolphin.change_speed(speed_percent)

def reset():
    emulation.reset()