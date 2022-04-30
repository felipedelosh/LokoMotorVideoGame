"""
FelipedelosH
This is the main controller to my videogame

"""
from control import Control

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

    def setConfigDefaultOptions(self):
        self.configuration["displayW"]="1280"
        self.configuration["displayH"]="720"
        self.configuration["playerName"]="Human"
        self.configuration["playerAge"]="0"
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