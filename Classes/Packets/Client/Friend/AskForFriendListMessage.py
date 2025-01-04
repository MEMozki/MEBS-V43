from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Packets.Server.Home.BattleLogMessage import BattleLogMessage
from Classes.Messaging import Messaging

from Classes.ByteStream import ByteStream


class AskForFriendListMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        fields["Unk2"] = self.readVInt()
        return fields

    def encode(self):
    	pass
    
    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(20105, fields, calling_instance.player)

    def getMessageType(self):
        return 10504

    def getMessageVersion(self):
        return self.messageVersion
