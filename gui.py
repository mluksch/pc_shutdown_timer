from tkinter import *

import config
import utils


class Gui:
    def __init__(self, timer):
        self.root = Tk()
        self.root.config(padx=10, pady=10)
        self.root.wm_title(u"\u23FC")
        self.root.attributes('-topmost', True)
        self.root.minsize(width=config.WIDTH, height=config.HEIGHT)
        self.root.resizable(False, False)

        self.timer = timer
        timer.listen(on_tick=self._update_timer)
        self._start_ticking()

        canvas_timer = Canvas()
        canvas_timer.config(bg=config.COLOR_TIMER_BG, width=80, height=25)
        canvas_timer.grid(column=0, row=0, columnspan=2)
        self.canvas_timer = canvas_timer
        self._update_timer()

        lbl_time_mins = Label()
        lbl_time_mins.config(text="Countdown (mins)")
        lbl_time_mins.grid(column=0, row=1)

        input_time_mins = Entry(width=9)
        input_time_mins.grid(column=1, row=1)
        self.input_time_mins = input_time_mins
        self._update_input_time()

        btn_cancel_shutdown = Button(text="Cancel", command=self._on_click_btn_cancel)
        btn_cancel_shutdown.grid(column=0, row=2)
        self.btn_cancel_shutdown = btn_cancel_shutdown

        btn_shutdown = Button(text="Start", command=self._on_click_btn_shutdown)
        btn_shutdown.grid(column=1, row=2)
        self.btn_shutdown = btn_shutdown

    def _start_ticking(self):
        self.root.after(1000, func=self._tick)

    def _tick(self):
        self.timer.tick()
        self.root.after(1000, func=self._tick)

    def display(self):
        self.root.mainloop()

    def _update_timer(self):
        formatted = utils.format_time_in_sec(self.timer.get_remaining_time_in_sec())
        self.canvas_timer.delete(ALL)
        self.canvas_timer.create_text(40, 14, fill=config.COLOR_TIMER, font="Courier 17 italic bold",
                                      text=formatted)

    def _update_input_time(self):
        self.input_time_mins.delete(0, END)
        self.input_time_mins.insert(0, self.timer.countdown_in_mins)

    # handlers:
    def _on_click_btn_shutdown(self):
        value = self.input_time_mins.get()
        self.timer.set_countdown(int(value.strip()))
        self.timer.start()

    def _on_click_btn_cancel(self):
        self.timer.cancel()
        self._update_timer()
