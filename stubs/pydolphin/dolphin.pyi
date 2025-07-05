"""
Functions related to running Dolphin
"""


def run(game_path: str, save_state_path: str = "", head_less: bool = False, speed_percent: int = 0, backend: str = "default", use_dual_core: bool = False) -> None:
    """
    Runs Dolphin

    :param game_path: Path to the game ROM
    :param save_state_path: Path to the savestate (optional)
    :param head_less: Whether to run as head_less (with no gui) or with gui
    :param speed_percent: Speed in percent. 0 Means unlimited speed
    :param backend: Rendering backend name to be used.
    """

def stop() -> None:
    """
    Stops Dolphin
    """


def check_init() -> bool:
    """
    Checks if Dolphin is initialized

    :return: value as boolean
    """