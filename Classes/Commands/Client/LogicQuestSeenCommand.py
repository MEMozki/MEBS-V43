import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicQuestSeenCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        pass

    def decode(self, calling_instance):
        pass

    def execute(self, calling_instance, fields):
        self.writeVInt(1) # Quests Count
        
        self.writeVInt(1)     # Unknown
        self.writeVInt(11)     # Unknown
        self.writeVInt(0)     # Mission Type
        self.writeVInt(0)     # Achieved Goal
        self.writeVInt(3)     # Quest Goal
        self.writeVInt(200)    # Tokens Reward
        self.writeVInt(11)     # Unknown
        self.writeVInt(0)     # Current level
        self.writeVInt(0)     # Max level
        self.writeVInt(999999)     # Timer
        self.writeBoolean(False)    # Brawl Pass Quest
        self.writeDataReference(16, 54) # Brawler(16, <BrawlerID>)
        self.writeVInt(-1)     # GameMode
        self.writeVInt(11)     # Unknown
        self.writeVInt(11)     # Unknown
        self.writeVInt(11)     # Unknown

    def getCommandType(self):
        return 533