from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class FriendListMessage(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
        self.writeVInt(1)
        self.writeVInt(1)
        
        self.writeLong(0, 1)
        
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        
        self.writeVInt(0)
        self.writeInt(4)
        self.writeInt(1)
        self.writeInt(1)
        self.writeInt(1)
        
        self.writeBoolean(False)
        
        self.writeString()
        self.writeInt(0)
        
        self.writeBoolean(True)
        
        self.writeString("FriendlyBot")
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(-1)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20105

    def getMessageVersion(self):
        return self.messageVersion
