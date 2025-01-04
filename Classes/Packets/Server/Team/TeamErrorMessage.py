from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamErrorMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(10)
        self.writeVInt(10)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24129

    def getMessageVersion(self):
        return self.messageVersion