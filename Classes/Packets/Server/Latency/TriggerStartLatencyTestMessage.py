from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
from Classes.Commands.LogicCommand import LogicCommand

class TriggerStartLatencyTestMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0        
    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
    def encode(self,fields):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

    def execute(message, calling_instance, fields):
        Messaging.sendMessage(19004, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})
        

    def getMessageType(self):
        return 19003

    def getMessageVersion(self):
        return self.messageVersion