from tkinter import *


class Calculator:
    def __init__(self, frame):
        self.frame = frame
        frame.title("Python Calculator")

        # create screen widget
        self.screen = Text(frame, state='disabled', width=30, height=3, background="yellow", foreground="blue")

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''


root = Tk()
my_gui = Calculator(root)
root.mainloop()