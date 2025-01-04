from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import random
import json


class ChatToAllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Message"] = self.readString()
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        clubdb_instance = ClubDatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])
        
        MessageCount = len(clubData["ChatData"])
        Role = clubData["Members"][str(playerData["ID"][1])]["Role"]
        message = {
        'StreamType': 2,
        'StreamID': [0, MessageCount + 1],
        'PlayerID': calling_instance.player.ID,
        'PlayerName': calling_instance.player.Name,
        'PlayerRole': Role,
        'Message': fields["Message"]
        }
        clubData["ChatData"].append(message)
        clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        Messaging.sendMessage(24311, fields, calling_instance.player)


    def getMessageType(self):
        return 14315

    def getMessageVersion(self):
        return self.messageVersion