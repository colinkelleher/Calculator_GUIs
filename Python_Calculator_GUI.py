from tkinter import *

# Creating the Frame
class PythonCalculator:
    def __init__(self,frame):
        self.frame = frame
        frame.title("Colins Python Calculator")




root = Tk()
GUI = PythonCalculator(root)
root.mainloop()