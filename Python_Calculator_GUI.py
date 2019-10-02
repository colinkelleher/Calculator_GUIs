from tkinter import *

# Creating the Frame
class PythonCalculator:
    def __init__(self,frame):
        self.frame = frame
        frame.title("Colins Python Calculator")

        self.screen = Text(frame, state='disabled', width=30, height=3,background='yellow', foreground='blue')




root = Tk()
GUI = PythonCalculator(root)
root.mainloop()