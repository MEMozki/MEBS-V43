from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
from Classes.Commands.LogicCommand import LogicCommand

class RequestLatencyTestStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0        
    def encode(self,fields):
    	self.writeVInt(10)
    def decode(self):
        self.readVInt()

    def execute(message, calling_instance, fields):
        Messaging.sendMessage(19001, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
       

    def getMessageType(self):
        return 19004

    def getMessageVersion(self):
        return self.messageVersion