"""
FelipedelosH
This is the main controller to my videogame

"""
from tkinter import *
from control import Control
from player import *
from stateMachine import *

class Controller:
    def __init__(self) -> None:
        self.configuration = {} # game configuration
        self.loadConfiguration()
        self.control = Control(
            self.configuration["key_UP"],
            self.configuration["key_RIGTH"],
            self.configuration["key_DOWN"],
            self.configuration["key_LEFT"],
            self.configuration["key_SELECT"],
            self.configuration["key_START"],
            self.configuration["key_B"],
            self.configuration["key_A"],
            self.configuration["key_Y"],
            self.configuration["key_X"],
            self.configuration["key_L"],
            self.configuration["key_R"])
        self.language = {} # Containt a language
        self.loadLanguage()
        self.SMgame = StateMachine()
        self._initStateMachineGame()
        self.player = Player()

    def _initStateMachineGame(self):
        self.SMgame.addNode("gameStart")
        self.SMgame.addNode("gamePause")
        self.SMgame.addNode("gameOptions")
        # To game Running
        for i in self.control.direction_buttons:
            self.SMgame.addConection("gameStart", "gameStart", i)
        for i in self.control.action_buttons:
            self.SMgame.addConection("gameStart", "gameStart", i)
        self.SMgame.addConection("gameStart", "gamePause", self.control.key_START)
        self.SMgame.addConection("gamePause", "gameStart", self.control.key_START)
        self.SMgame.addConection("gameStart", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "gameStart", self.control.key_SELECT)
        self.SMgame.addConection("gamePause", "gameOptions", self.control.key_SELECT)
        self.SMgame.addConection("gameOptions", "gamePause", self.control.key_START)        

    def paintPlayer(self, canvas):
        
        pass


    def loadLanguage(self, language="ESP"):
        try:
            f = open('resources/LAN/'+language+"/game.txt", 'r')
            for i in f.read().split("\n"):
                if str(i).strip() != "":
                    info = i.split("=")
                    self.language[str(info[0])]=str(info[1])
        except:
            self.setLanguageDefault()

    def loadConfiguration(self):
        try:
            f = open('resources/config.txt', 'r')
            for i in f.read().split("\n"):
                if str(i).strip() != "":
                    info = i.split("=")
                    self.configuration[str(info[0])]=str(info[1])
        except:
            self.setConfigDefaultOptions()

    def getFPS(self):
        return int(1000/int(self.configuration["FPS"]))

    def setConfigDefaultOptions(self):
        self.configuration["displayW"]="1280"
        self.configuration["displayH"]="720"
        self.configuration["playerName"]="Human"
        self.configuration["playerAge"]="0"
        self.configuration["FPS"]="30"
        self._setConfigDefaultOptionsController()
    
    def _setConfigDefaultOptionsController(self):
        self.configuration["key_U"]="38"
        self.configuration["key_RIGTH"]="39"
        self.configuration["key_DOWN"]="40"
        self.configuration["key_LEFT"]="37"
        self.configuration["key_SELECT"]="32"
        self.configuration["key_START"]="13"
        self.configuration["key_B"]="90"
        self.configuration["key_A"]="88"
        self.configuration["key_Y"]="67"
        self.configuration["key_X"]="86"
        self.configuration["key_L"]="65"
        self.configuration["key_R"]="83"


    def setLanguageDefault(self):
        self.language["gameTitle"]="LokoGame"

    def _setPlayer(self):
        # Load all player images
        
        self.player.posX = 100
        self.player.posY = 100