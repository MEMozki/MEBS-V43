from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler, DatabaseHandler
from Classes.ClientsManager import ClientsManager
import json

class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        clubdb_instance = ClubDatabaseHandler()
        db_instance = DatabaseHandler()
        clubData = json.loads(clubdb_instance.getClubWithLowID(fields["AllianceID"][1])[0][1])
        db_instance.loadAccount(player, player.ID)
        allSockets = ClientsManager.GetAll()

        self.writeBoolean(False)
        
        AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

        self.writeString(clubData["Description"])

        self.writeVInt(len(clubData["Members"]))

        for i in clubdb_instance.getMembersSorted(clubData):
            memberData = i[1]
            playerData = json.loads(db_instance.getPlayerEntry([memberData['HighID'], memberData['LowID']])[2])
            self.writeLong(memberData['HighID'], memberData['LowID'])
            self.writeVInt(memberData['Role']) # Role
            self.writeVInt(playerData['Trophies']) # Trophies
            if playerData["ID"][1] in allSockets:
                self.writeVInt(2) # Player State TODO: Members state
            else:
                self.writeVInt(0)
            self.writeVInt(6974) # State Timer

            self.writeVInt(1)
            self.writeVInt(1) # idk
            self.writeVInt(19) # Power League Rank

            self.writeBoolean(False) # DoNotDisturb TODO: Do not disturb sync

            self.writeString(playerData['Name']) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000 + playerData['Thumbnail']) # Player Thumbnail
            self.writeVInt(43000000 + playerData['Namecolor']) # Player Name Color
            self.writeVInt(46000000) # Color Gradients

            self.writeVInt(-1)
            self.writeBoolean(False)

            self.writeVInt(1) # Club League
            self.writeVInt(0) # Idk
            self.writeVInt(317) # Season Club Trophies
            self.writeVInt(317) # Day Club Trophies
            self.writeVInt(14) # Season Tickets Used
            self.writeVInt(6) # Day Tickets Used
            self.writeVInt(6) # Day Tickets Usex Max
            self.writeVInt(0) # Idk
            self.writeBoolean(True)
            
            self.writeVInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion
