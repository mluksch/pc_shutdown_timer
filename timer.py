import os
import time

import config


class Timer:
    def __init__(self):
        self.on_tick = None
        self.start_time = None
        self.countdown_in_mins = config.COUNTDOWN_DEFAULT_MINS
        self.stopped = True

    def listen(self, on_tick, on_alarm):
        self.on_tick = on_tick
        self.on_alarm = on_alarm

    def start(self):
        self.stopped = False
        self.start_time = time.time()

    def get_remaining_time_in_sec(self):
        if not self.stopped:
            elapsed = time.time() - self.start_time if self.start_time else 0
            return max(round(self.countdown_in_mins * 60 - elapsed), 0)
        elif self.stopped:
            return self.countdown_in_mins * 60

    def tick(self):
        if not self.stopped and self.start_time:
            if self.on_tick:
                self.on_tick()
            elapsed_in_sec = self.get_remaining_time_in_sec()
            finished = elapsed_in_sec == 0
            if (elapsed_in_sec == 10 * 60 or elapsed_in_sec == 5 * 60 or elapsed_in_sec == 60) and self.on_alarm:
                self.on_alarm()
            if finished:
                # shutdown pc
                os.system(f"shutdown /s")

    def set_countdown(self, countdown_in_mins):
        self.countdown_in_mins = countdown_in_mins

    def cancel(self):
        self.start_time = None
        self.countdown_in_mins = config.COUNTDOWN_DEFAULT_MINS
        self.stopped = True
