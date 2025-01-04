from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class JoinAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AllianceID"] = self.readLong()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])
        player_data["AllianceID"] = fields["AllianceID"]
        clubData["Members"][str(calling_instance.player.ID[1])] = {'HighID': calling_instance.player.ID[0], 'LowID': calling_instance.player.ID[1], 'Name': calling_instance.player.Name, 'Role': 1, 'Trophies': calling_instance.player.Trophies, 'NameColor': calling_instance.player.Namecolor, 'Thumbnail': calling_instance.player.Thumbnail}
        db_instance.updatePlayerData(player_data, calling_instance)
        clubdb_instance.updateClubData(clubData, fields["AllianceID"][1])
        
        MessageCount = len(clubData["ChatData"])
        Role = clubData["Members"][str(player_data["ID"][1])]["Role"]
        message = {
        'StreamType': 4,
        'StreamID': [0, MessageCount + 1],
        'PlayerID': calling_instance.player.ID,
        'PlayerName': calling_instance.player.Name,
        'PlayerRole': Role,
        'EventType': 3,
        'Target': {'ID': calling_instance.player.ID, 'Name': calling_instance.player.Name}
        }
        clubData["ChatData"].append(message)
        clubdb_instance.updateClubData(clubData, calling_instance.player.AllianceID[1])
        Messaging.sendMessage(24311, fields, calling_instance.player)
        
        fields["Socket"] = calling_instance.client
        fields["ResponseID"] = 40
        Messaging.sendMessage(24333, fields)
        fields["HasClub"] = True
        Messaging.sendMessage(24399, fields, calling_instance.player)
        Messaging.sendMessage(24311, fields, calling_instance.player)
        Messaging.sendMessage(22161, fields, calling_instance.player)

    def getMessageType(self):
        return 14305

    def getMessageVersion(self):
        return self.messageVersion