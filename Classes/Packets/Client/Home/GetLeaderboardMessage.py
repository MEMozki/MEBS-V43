from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class GetLeaderboardMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["IsLocal"] = self.readVInt()
        fields["Type"] = self.readVInt()
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        # def by_trophy(plr):
        #     return plr['Trophies']
        #db = DatabaseHandler()
        #players = db.load_all()
        #calling_instance.sort(key = by_trophy, reverse=True)
        Messaging.sendMessage(24403, fields, calling_instance.player)

    def getMessageType(self):
        return 14403

    def getMessageVersion(self):
        return self.messageVersion