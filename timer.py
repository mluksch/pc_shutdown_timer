import os
import time


class Timer:
    def __init__(self):
        self.on_tick = None
        self.start_time = None
        self.countdown_in_mins = None

    def listen(self, on_tick):
        self.on_tick = on_tick

    def start(self):
        self.start_time = time.time()

    def tick(self):
        if self.start_time and self.countdown_in_mins:
            now = time.time()
            elapsed_in_sec = round(now - self.start_time)
            if self.on_tick:
                self.on_tick(elapsed_in_sec)
            finished = elapsed_in_sec >= 60 * self.countdown_in_mins
            if finished:
                # shutdown pc
                os.system(f"shutdown /s")

    def set_countdown(self, countdown_in_mins):
        self.countdown_in_mins = countdown_in_mins

    def cancel(self):
        self.start_time = None
        self.countdown_in_mins = None
