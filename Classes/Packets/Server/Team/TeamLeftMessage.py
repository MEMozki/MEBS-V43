from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamLeftMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24125

    def getMessageVersion(self):
        return self.messageVersion
