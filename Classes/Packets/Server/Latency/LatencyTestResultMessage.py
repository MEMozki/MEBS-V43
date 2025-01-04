from Classes.Packets.PiranhaMessage import PiranhaMessage


class LatencyTestResultMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0        
    def encode(self,fields):
        self.writeVInt(1000)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(True)
        self.writeString("FaliDev")

    def execute(message, calling_instance, fields):
        pass
        

    def getMessageType(self):
        return 19001

    def getMessageVersion(self):
        return self.messageVersion
