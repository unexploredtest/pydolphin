import _cdolphin

def run(game_path, save_state_path="", head_less=False, speed_percent=0, backend="default", use_dual_core=False):
    _cdolphin.run(game_path, save_state_path, head_less, speed_percent, backend, use_dual_core)

def stop():
    _cdolphin.stop()

def check_init():
    return _cdolphin.check_init()
