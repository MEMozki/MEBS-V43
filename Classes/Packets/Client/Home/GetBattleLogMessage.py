from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Packets.Server.Home.BattleLogMessage import BattleLogMessage
from Classes.Messaging import Messaging

from Classes.ByteStream import ByteStream


class GetBattleLogMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def decode(self):
        fields = {}
        return fields

    def encode(self):
    	pass
    
    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(23458, fields, calling_instance.player)

    def getMessageType(self):
        return 14114

    def getMessageVersion(self):
        return self.messageVersion