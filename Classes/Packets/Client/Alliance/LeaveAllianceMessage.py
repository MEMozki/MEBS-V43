from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class LeaveAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        clubData = json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])
        MessageCount = len(clubData["ChatData"])
        Role = clubData["Members"][str(player_data["ID"][1])]["Role"]
        message = {
        'StreamType': 4,
        'StreamID': [0, MessageCount + 1],
        'PlayerID': calling_instance.player.ID,
        'PlayerName': calling_instance.player.Name,
        'PlayerRole': Role,
        'EventType': 4,
        'Target': {'ID': calling_instance.player.ID, 'Name': calling_instance.player.Name}
        }
        clubData["ChatData"].append(message)
        clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(24311, fields, calling_instance.player)
        del clubData["Members"][str(calling_instance.player.ID[1])]
        if len(clubData["Members"]) == 0:
        	clubdb_instance.deleteClub(calling_instance.player.AllianceID[1])
        clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        
        player_data["AllianceID"] = [0, 0]
        db_instance.updatePlayerData(player_data, calling_instance)
        
        fields["Socket"] = calling_instance.client
        fields["ResponseID"] = 80
        Messaging.sendMessage(24333, fields)
        fields["HasClub"] = False
        Messaging.sendMessage(24399, fields, calling_instance.player)

    def getMessageType(self):
        return 14308

    def getMessageVersion(self):
        return self.messageVersion