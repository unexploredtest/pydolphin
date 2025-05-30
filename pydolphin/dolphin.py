import _cdolphin
from _cdolphin import emulation

def run(game_path, save_state_path="", head_less=False):
    _cdolphin.run(game_path, save_state_path, head_less)

def stop():
    _cdolphin.stop()

def check_init():
    return _cdolphin.check_init()

def reset():
    emulation.reset()