import _cdolphin

def run(game_path, save_state_path="", head_less=False, speed_percent=0, backend="default"):
    _cdolphin.run(game_path, save_state_path, head_less, speed_percent, backend)

def stop():
    _cdolphin.stop()

def check_init():
    return _cdolphin.check_init()
