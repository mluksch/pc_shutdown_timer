from tkinter import *

import config


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.config(padx=5, pady=5)
        self.root.wm_title("PC-Shutdown-Timer")
        self.root.attributes('-topmost', True)
        self.root.minsize(width=config.WIDTH, height=config.HEIGHT)

        canvas_timer = Canvas()
        canvas_timer.config(bg="red", width=200, height=50)
        canvas_timer.grid(column=0, row=0, columnspan=2)
        self.canvas_timer = canvas_timer

        lbl_time_mins = Label()
        lbl_time_mins.config(text="Shutdown in mins")
        lbl_time_mins.grid(column=0, row=1)

        input_time_mins = Entry()
        input_time_mins.grid(column=1, row=1)
        self.input_time_mins = input_time_mins

        btn_cancel_shutdown = Button(text="Cancel")
        btn_cancel_shutdown.grid(column=0, row=2)
        self.btn_cancel_shutdown = btn_cancel_shutdown

        btn_shutdown = Button(text="Shutdown")
        btn_shutdown.grid(column=1, row=2)
        self.btn_shutdown = btn_shutdown

    def display(self):
        self.root.mainloop()
