from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import random
import json


class AlliancePremadeChatMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        pass
        
    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        fields["MessageDataID"] = self.readVInt()
        fields["EmoteID"] = self.readVInt()
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
        'StreamType': 8,
        'StreamID': [0, MessageCount + 1],
        'PlayerID': calling_instance.player.ID,
        'PlayerName': calling_instance.player.Name,
        'PlayerRole': Role,
        'MessageDataID': fields["MessageDataID"],
        'PremadeID': fields["EmoteID"]
        }
        clubData["ChatData"].append(message)
        clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        Messaging.sendMessage(24311, fields, calling_instance.player)
        

    def getMessageType(self):
        return 14469

    def getMessageVersion(self):
        return self.messageVersion
