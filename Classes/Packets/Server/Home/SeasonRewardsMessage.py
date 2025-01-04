from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class SeasonRewardsMessage(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
    	self.writeVInt(1)
    	self.writeVInt(1)
    	self.writeVInt(1)
    	self.writeVInt(1)
    	self.writeVInt(1)
    	self.writeVInt(1)
    	

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24123

    def getMessageVersion(self):
        return self.messageVersion
