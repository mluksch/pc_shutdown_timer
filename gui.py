from tkinter import *

import config


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(width=config.WIDTH, height=config.HEIGHT)

    def display(self):
        self.root.mainloop()
