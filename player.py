"""
FelipedelosH
"""
from tkinter import PhotoImage

class Player:
    def __init__(self) -> None:
        self.sprite = None # Containt a code Sprite
        self.tempSprite = PhotoImage(file="resources/images/player/example.png")
        self.posX = 0
        self.posY = 0
        self.age = 0
        self.health = 100
        self.attack = 1
        self.defend = 1
        self.inteligence = 1
        self.stanmina = 10