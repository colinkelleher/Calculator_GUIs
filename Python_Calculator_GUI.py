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

        # \u232B - Unicode 'ERASE TO THE LEFT
        # \u00F7 - Unicode ' Division Sign)
        b1 = self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u232B", None)
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00F7")
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('*')
        b13 = self.createButton('.')
        b14 = self.createButton(0)
        b15 = self.createButton('+')
        b16 = self.createButton('-')
        b17 = self.createButton('=', None, 40)

        # buttons stored in list
        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

    def createButton():
            return

root = Tk()
my_gui = Calculator(root)
root.mainloop()