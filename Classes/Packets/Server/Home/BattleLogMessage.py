from Classes.ByteStream import ByteStream
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class BattleLogMessage(PiranhaMessage):

    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        

    def encode(self, fields, player):
        pass

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        
        self.writeBoolean(True)

        logs = player_data["BattleLogs"]["Logs"]
        
        self.writeVInt(0) # Count

        for x in range(0):
        	self.writeVInt(2) # Gamemode
        	self.writeVInt(0)
        	self.writeVInt(99999)    # Time When Battle Log Entry Was Created
        	self.writeVInt(1)    # Battle Log Type (1 = Normal, 2 = Crash, 3 = Survived for <time>, 
        	self.writeVInt(8)    # Trophies Result
        	self.writeVInt(120)  # Battle Time
        	self.writeInt8(0)   # Type
        	self.writeDataReference(15, 95) # Map SCID
        	self.writeVInt(1) # Victory/Defeat/Draw
        	self.writeVInt(0) # Mapmaker Map ID
        	
        	self.writeInt(0)
        	self.writeInt(0)
        	
        	self.writeVInt(1)
        	self.writeInt8(1)
        	
        	self.writeVInt(0)  # array
        	
        	self.writeVInt(0)
        	self.writeInt8(0)
        	self.writeVInt(0)
        	self.writeInt8(0)
        	self.writeVInt(0)

    def getMessageType(self):
        return 23458

    def getMessageVersion(self):
        return self.messageVersion