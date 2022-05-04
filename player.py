"""
FelipedelosH
"""
from tkinter import PhotoImage

class Player:
    def __init__(self) -> None:
        self.sprite = None # Containt a code Sprite
        self.tempSprite = PhotoImage(file="resources/images/player/example.png")
        self.posX = 500
        self.posY = 200
        self.age = 0
        self.health = 100
        self.attack = 1
        self.defend = 1
        self.inteligence = 1
        self.stanmina = 10
        self.velocity = 3

    def player_mouve_up(self):
        if (self.posY-self.velocity>0):
            self.posY = self.posY - self.velocity

    def player_mouve_down(self):
        self.posY = self.posY + self.velocity

    def player_mouve_rigth(self):
        self.posX = self.posX + self.velocity

    def player_mouve_left(self):
        self.posX = self.posX - self.velocity

    