"""
FelipedelosH
This is my first MotorVideoGame
"""
from tkinter import *
from controller import *

class Software:
    def __init__(self) -> None:
        self.display = Tk()
        self.canvas = Canvas(self.display, bg="snow")
        self.canvas.bind_all("<Key>", self.keyPressed)


        self.controller = Controller()


        self.VizualizedAndRun()


    def VizualizedAndRun(self):
        self.display.title(self.controller.language["gameTitle"])
        self.display.geometry(self.controller.configuration["displayW"]+"x"+self.controller.configuration["displayH"])
        self.canvas['height']=int(self.controller.configuration["displayH"])
        self.canvas['width']=int(self.controller.configuration["displayW"])
        self.canvas.place(x=0, y=0)
        
        self.display.resizable(0,0)
        self.display.after(0, self.refreshGame)
        self.display.mainloop()

    def refreshGame(self):
        self.display.after(30, self.refreshGame)


    def keyPressed(self, Event):
        if str(Event.keycode) in self.controller.control.keyResult:
            if str(Event.keycode) == self.controller.control.key_UP:
                print("Arriba")
            if str(Event.keycode) == self.controller.control.key_RIGTH:
                print("Derecha")
            if str(Event.keycode) == self.controller.control.key_DOWN:
                print("Abajo")
            if str(Event.keycode) == self.controller.control.key_LEFT:
                print("Izquierda")    
            if str(Event.keycode) == self.controller.control.key_B:
                print("B")
            if str(Event.keycode) == self.controller.control.key_A:
                print("A")
            if str(Event.keycode) == self.controller.control.key_Y:
                print("Y")
            if str(Event.keycode) == self.controller.control.key_X:
                print("X")
            if str(Event.keycode) == self.controller.control.key_SELECT:
                print("Select")
            if str(Event.keycode) == self.controller.control.key_START:
                print("Start")
            if str(Event.keycode) == self.controller.control.key_L:
                print("L")
            if str(Event.keycode) == self.controller.control.key_R:
                print("R")

s = Software()