## PyDolphin

Python bindings for dolphin, an emulator for GameCube and Wii, based on [Felk's fork](https://github.com/Felk/dolphin).

### Example
```py
import pydolphin
iso_path = "path/to/iso"
save_state_path = "path/to/savefile"

pydolphin.run(iso_path, save_state_path) # Runs Dolphin and the game
pydolphin.stop() # Stops and closes the emulator
```

### Prerequistes
Requires Python 3.12+

### Build
```sh
python setup.py install
```
