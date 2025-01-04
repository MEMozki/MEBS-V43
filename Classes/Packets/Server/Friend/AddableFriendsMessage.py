from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class AddableFriendsMessage(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
        self.writeVInt(1)



        self.writeVInt(0)

        self.writeVInt(1)



        self.writeVInt(1)

        self.writeVInt(0) #trophies



        self.writeVInt(1)

        self.writeString("Club Friends")



        self.writeString("Test")

        self.writeVInt(0)

        self.writeVInt(28000069)

        self.writeVInt(43000005)

        self.writeVInt(46000005)

        self.writeVInt(0) #UNK

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20107

    def getMessageVersion(self):
        return self.messageVersion
