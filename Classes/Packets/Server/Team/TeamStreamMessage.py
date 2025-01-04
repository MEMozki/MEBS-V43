from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging


class TeamStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(1)
        for i in range(1):
        	self.writeVInt(8)
        	self.writeVInt(0)
        	self.writeVInt(1)
        	self.writeVInt(player.ID[0])
        	self.writeVInt(player.ID[1])
        	self.writeString(player.Name)
        	self.writeVInt(0)
        	self.writeVInt(0)
        	self.writeVInt(0)
        	self.writeDataReference(40, 0)
        	self.writeBoolean(True)
        	self.writeString(player.Name)
        	self.writeVInt(0)
        	self.writeVInt(52000000)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24124, fields, calling_instance.player)

    def getMessageType(self):
        return 24131

    def getMessageVersion(self):
        return self.messageVersion