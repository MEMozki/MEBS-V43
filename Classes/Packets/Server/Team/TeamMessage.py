from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1) # Room Type
        self.writeBoolean(False)
        self.writeVInt(1)

        self.writeInt(0)
        self.writeInt(1)

        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeDataReference(15, 7)
        self.writeBoolean(False)
        
        self.writeVInt(1)  # Players Array

        self.writeBoolean(True)  # Owner
        self.writeLong(player.ID[0], player.ID[1]) # Player ID
        self.writeDataReference(16, 0) # Brawler
        self.writeDataReference(29, 0)  # Brawler Skin
        self.writeVInt(0) # Brawler Trophies
        self.writeVInt(0) # Brawler Trophies for Rank
        self.writeVInt(9) # Brawler Level
        self.writeVInt(3) # Player State
        self.writeBoolean(False) # Ready
        self.writeVInt(0) # Team
        self.writeVInt(52000000 + 69)
        self.writeVInt(52000000 + 69)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString(player.Name)
        self.writeVInt(100)
        self.writeVInt(28000000 + player.Thumbnail)
        self.writeVInt(43000000 + player.Namecolor)
        self.writeVInt(-1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) # pin
        
        self.writeVInt(0) # Invited Players
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Club War
        self.writeVInt(6)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion