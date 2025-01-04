from io import BytesIO

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
import Configuration

OwnedBrawlersLatest = {
    0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    1: {'CardID': 4, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    2: {'CardID': 8, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    3: {'CardID': 12, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    4: {'CardID': 16, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    5: {'CardID': 20, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    6: {'CardID': 24, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    7: {'CardID': 28, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    8: {'CardID': 32, 'Skins': [435], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    9: {'CardID': 36, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    10: {'CardID': 40, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    11: {'CardID': 44, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    12: {'CardID': 48, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    13: {'CardID': 52, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    14: {'CardID': 56, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    15: {'CardID': 60, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    16: {'CardID': 64, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    17: {'CardID': 68, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    18: {'CardID': 72, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    19: {'CardID': 95, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    20: {'CardID': 100, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    21: {'CardID': 105, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    22: {'CardID': 110, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    23: {'CardID': 115, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    24: {'CardID': 120, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    25: {'CardID': 125, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    26: {'CardID': 130, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    27: {'CardID': 177, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    28: {'CardID': 182, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    29: {'CardID': 188, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    30: {'CardID': 194, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    31: {'CardID': 200, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    32: {'CardID': 206, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    34: {'CardID': 218, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    35: {'CardID': 224, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    36: {'CardID': 230, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    37: {'CardID': 236, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    38: {'CardID': 279, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    39: {'CardID': 296, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    40: {'CardID': 303, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    41: {'CardID': 320, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    42: {'CardID': 327, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    43: {'CardID': 334, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    44: {'CardID': 341, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    45: {'CardID': 358, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    46: {'CardID': 365, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    47: {'CardID': 372, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    48: {'CardID': 379, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    49: {'CardID': 386, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    50: {'CardID': 393, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    51: {'CardID': 410, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    52: {'CardID': 417, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    53: {'CardID': 427, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    54: {'CardID': 434, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    56: {'CardID': 448, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
}


class BattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeLong(0, 1)
        self.writeLong(0, 1)
        PlayersTeams = []
        for heroEntry in fields["Heroes"]:
        	PlayersTeams.append(heroEntry["Team"])
        Bot1Team = PlayersTeams[1]
        if fields["HeroesCount"] == 10:
        	self.writeVInt(2) # Battle End Game Mode
        elif fields["HeroesCount"] == 10 and Bot1Team == 0:
        	self.writeVInt(5) # Battle End Game Mode
        elif fields["HeroesCount"] == 3 and fields["MapID"][1] in [27, 29, 39, 68]:
        	self.writeVInt(3) # Battle End Game Mode
        elif fields["HeroesCount"] == 3 and fields["MapID"][1] in [57, 67, 133]:
        	self.writeVInt(6) # Battle End Game Mode
        elif fields["HeroesCount"] == 6 and fields["MapID"][1] in [21, 30, 65, 66, 119, 120]:
        	self.writeVInt(4) # Battle End Game Mode
        else:
        	self.writeVInt(1) # Battle End Game Mode
        self.writeVInt(fields["Rank"]) # Result (Victory/Defeat/Draw/Rank Score)
        if fields["Result"] == 0:
        	self.writeVInt(150) # Tokens Gained
        	self.writeVInt(8) # Trophies Result
        if fields["Result"] == 1:
        	self.writeVInt(10) # Tokens Gained
        	self.writeVInt(-5) # Trophies Result
        if fields["Result"] == 2:
        	self.writeVInt(15) # Tokens Gained
        	self.writeVInt(0) # Trophies Result
        self.writeVInt(0) # Power Play Points Gained
        self.writeVInt(0) # Doubled Tokens
        if fields["Result"] == 0:
        	if Configuration.settings["DoubleTokenEvent"] == True: 
        	    self.writeVInt(20) # Double Token Event
        	else:
        		self.writeVInt(0) # Double Token Event
        if fields["Result"] == 1:
        	if Configuration.settings["DoubleTokenEvent"] == True: 
        	    self.writeVInt(10) # Double Token Event
        	else:
        		self.writeVInt(0) # Double Token Event
        if fields["Result"] == 2:
        	if Configuration.settings["DoubleTokenEvent"] == True: 
        	    self.writeVInt(15) # Double Token Event
        	else:
        		self.writeVInt(0) # Double Token Event
        self.writeVInt(0) # Token Doubler Remaining
        self.writeVInt(0) # Special Events Level Passed
        self.writeVInt(0) # Epic Win Power Play Points Gained
        self.writeVInt(0) # Championship Level Passed
        self.writeBoolean(False) # Challenge Reward Array
        self.writeVInt(0) # Challenge Reward Amount
        self.writeVInt(0) # Championship Losses Left
        self.writeBoolean(False)  # Championship Array
        if fields["Result"] == 0:
        	if Configuration.settings["GoldRushEvent"] == True: 
        	    self.writeVInt(20) # Coin Shower Event
        	else:
        		self.writeVInt(0) # Coin Shower Event
        if fields["Result"] == 1:
        	if Configuration.settings["GoldRushEvent"] == True: 
        	    self.writeVInt(10) # Coin Shower Event
        	else:
        		self.writeVInt(0) # Coin Shower Event
        if fields["Result"] == 2:
        	if Configuration.settings["GoldRushEvent"] == True: 
        	    self.writeVInt(15) # Coin Shower Event
        	else:
        		self.writeVInt(0) # Coin Shower Event
        self.writeVInt(0) # Underdog Trophies
        self.writeVInt(0) # SD+ Win Trophies
        self.writeVInt(0) # SD+ Lose Trophies
        self.writeVInt(16) # Battle Result Type
        self.writeBoolean(False)
        self.writeBoolean(False) # Experience is Over
        self.writeBoolean(False) # Battle Tokens is Over
        self.writeBoolean(False) # Battle End State Off
        self.writeBoolean(True) # Trophies is  nit Off
        self.writeBoolean(False) # Battle End State is Over
        self.writeBoolean(False) # Power Play Battle End
        self.writeVInt(-1) # Challenge Type
        self.writeBoolean(False) # ChampionShip Cleared and Beta Quests

        self.writeVInt(fields["HeroesCount"]) # Players In Battle End
        for heroEntry in fields["Heroes"]:
            self.writeBoolean(heroEntry["IsPlayer"])
            if fields["HeroesCount"] == 10 and Bot1Team != 0:
            	self.writeBoolean(0)
            	self.writeBoolean(bool(heroEntry["Team"]))
            elif fields["HeroesCount"] == 10 and Bot1Team == 0:
            	self.writeBoolean(0)
            	self.writeBoolean(bool(heroEntry["Team"]))
            else:
            	self.writeBoolean(bool(heroEntry["Team"]))
            self.writeBoolean(bool(heroEntry["Team"]))
            self.writeVInt(1)
            for i in range(1):
                self.writeDataReference(heroEntry["Brawler"]["ID"][0], heroEntry["Brawler"]["ID"][1])
            self.writeVInt(1)
            for i in range(1):
                if heroEntry["Brawler"]["SkinID"] != None:
                    self.writeDataReference(heroEntry["Brawler"]["SkinID"][0], heroEntry["Brawler"]["SkinID"][1])
                else:
                    self.writeDataReference(0)
            self.writeVInt(1)
            for i in range(1):
        	       	if heroEntry["IsPlayer"]:
        	       		self.writeVInt(fields["Trophies"]) # Brawler Trophies
        	       	else:
        	       		self.writeVInt(0)
            self.writeVInt(1)
            for i in range(1):
        	       	if heroEntry["IsPlayer"]:
        	       		for i,v in player.OwnedBrawlers.items():
        	       			if v["CardID"] == OwnedBrawlersLatest[heroEntry["Brawler"]["ID"][1]]["CardID"]:
        	       				self.writeVInt(v["PowerLevel"]) # Brawler Power LVL
        	       	else:
        	       		self.writeVInt(1)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(heroEntry["IsPlayer"])
            if heroEntry["IsPlayer"]:
                self.writeLong(player.ID[0], player.ID[1])
            self.writeString(heroEntry["PlayerName"])
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeVInt(46000000)
            if heroEntry["IsPlayer"]:
                self.writeBoolean(True)
                self.writeVLong(5, 4181497)
                self.writeString('Orange eSPORT')
                self.writeDataReference(8, 16)

        
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(2)

        self.writeVInt(1)
        self.writeVInt(fields["Trophies"]) # Brawler Trophies
        self.writeVInt(fields["HighestTrophies"]) # Brawler Trophies

        self.writeVInt(5)
        self.writeVInt(player.Experience)
        self.writeVInt(player.Experience)

        self.writeDataReference(28, 0)
        self.writeBoolean(False) # Play Again
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Power League
        self.writeVInt(-1)
        self.writeBoolean(False)
        
        if fields["Result"] == 0:
        	player.TrophiesGained += 8
        	if Configuration.settings["GoldRushEvent"] == True:
        		player.TokensGained += 20
        		player.CoinsGained += 20
        	elif Configuration.settings["DoubleTokenEvent"] == True: 
        	    player.TokensGained += 40
        	else:
        		player.TokensGained += 20
        if fields["Result"] == 1:
        	player.TrophiesGained -= 5
        	if Configuration.settings["GoldRushEvent"] == True:
        		player.TokensGained += 10
        		player.CoinsGained += 10
        	elif Configuration.settings["DoubleTokenEvent"] == True: 
        	    player.TokensGained += 20
        	else:
        		player.TokensGained += 10
        if fields["Result"] == 2:
        	player.TrophiesGained = 0
        	if Configuration.settings["GoldRushEvent"] == True:
        		player.TokensGained += 15
        		player.CoinsGained += 15
        	elif Configuration.settings["DoubleTokenEvent"] == True: 
        	    player.TokensGained += 30
        	else:
        		player.TokensGained += 15
        

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23456

    def getMessageVersion(self):
        return self.messageVersion
