from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler
from Classes.Messaging import Messaging


class GetSeasonRewardsMessage(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
    	pass

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24123, fields, calling_instance.player)

    def getMessageType(self):
        return 14277

    def getMessageVersion(self):
        return self.messageVersion
