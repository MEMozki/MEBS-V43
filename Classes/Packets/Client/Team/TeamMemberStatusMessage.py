from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler
from Classes.Messaging import Messaging


class TeamMemberStatusMessage(PiranhaMessage):


    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0


    def encode(self, fields, player):
        pass


    def decode(self):
        fields = {}
        fields["PlayerState"] = self.readVInt()
        super().decode(fields)
        return fields


    def execute(message, calling_instance, fields):
        pass


    def getMessageType(self):
        return 14361


    def getMessageVersion(self):
        return self.messageVersion
