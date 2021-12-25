from tkinter import *

import config
import utils
from timer import Timer


class Gui:
    def __init__(self, timer: Timer):
        self.root = Tk()
        self.root.config(padx=10, pady=10)
        self.root.wm_title(u"\u23FC")
        self.root.attributes('-topmost', True)
        self.root.minsize(width=config.WIDTH, height=config.HEIGHT)
        self.root.resizable(False, False)

        self.timer = timer

        canvas_timer = Canvas()
        canvas_timer.config(bg=config.COLOR_TIMER_BG, width=80, height=25)
        canvas_timer.grid(column=0, row=0, columnspan=2)
        self.canvas_timer = canvas_timer
        self._display_text("--:--")

        lbl_time_mins = Label()
        lbl_time_mins.config(text="Countdown (mins)")
        lbl_time_mins.grid(column=0, row=1)

        input_time_mins = Entry(width=9)
        input_time_mins.grid(column=1, row=1)
        self.input_time_mins = input_time_mins
        self._set_default_timer()

        btn_cancel_shutdown = Button(text="Cancel")
        btn_cancel_shutdown.grid(column=0, row=2)
        self.btn_cancel_shutdown = btn_cancel_shutdown

        btn_shutdown = Button(text="Shutdown")
        btn_shutdown.grid(column=1, row=2)
        self.btn_shutdown = btn_shutdown

    def _start_ticking(self):
        self.root.after(1000, func=self._tick)

    def _tick(self):
        elapsed_in_sec = self.timer.on_tick()
        formatted = utils.format_time_in_sec(elapsed_in_sec)
        self._display_text(formatted)

    def display(self):
        self.root.mainloop()

    def _display_text(self, text):
        self.canvas_timer.create_text(40, 14, fill=config.COLOR_TIMER, font="Courier 17 italic bold",
                                      text=text)

    def _set_default_timer(self):
        self.input_time_mins.delete(0, END)
        self.input_time_mins.insert(0, config.COUNTDOWN_DEFAULT_MINS)

    # handlers:
    def _on_click_btn_shutdown(self):
        pass

    def _on_click_btn_cancel(self):
        pass

