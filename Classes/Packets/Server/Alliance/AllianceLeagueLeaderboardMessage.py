from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler



class AllianceLeagueLeaderboardMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        
    def encode(self, fields, player):
        self.writeVInt(1)
        self.writeVLong(0, 1)
        self.writeVInt(1)
        self.writeVInt(1)

        self.writeVInt(1)

        self.writeVLong(0, 1)
        self.writeLong(0, 1)
        self.writeDataReference(8, 18)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(1)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22160

    def getMessageVersion(self):
        return self.messageVersion