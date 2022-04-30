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