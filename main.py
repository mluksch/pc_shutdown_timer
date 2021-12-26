from filelock import FileLock

import config
from gui import Gui
from timer import Timer

lock = FileLock(config.APP_NAME_LOCK, timeout=1)
try:
    with lock:
        timer = Timer()
        gui = Gui(timer=timer)
        gui.display()
except:
    pass
