from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging

from Classes.ByteStream import ByteStream


class ChronosEventSeenMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        return fields

    def encode(self):
    	pass
    
    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 14166

    def getMessageVersion(self):
        return self.messageVersion
