from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.ByteStreamHelper import ByteStreamHelper
from Static.StaticData import StaticData


class LogicDayChangedCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeVInt(25) # Count

        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        EventsData = StaticData.EventsData
        
        self.writeVInt(len(EventsData) + 7) # Coming Events Count(7 it a ChampionShip(3 Stages) and ClubLeague(PowerMatch and Default Game Mode)) and PowerLeague(Solo and Team Mode)
        for i in EventsData:
              # Default Slots Start Array #
              self.writeVInt(0)
              self.writeVInt(EventsData.index(i) + 1)  # EventType
              self.writeVInt(i['CountdownTimer'])  # EventsBeginCountdown
              self.writeVInt(i['Timer'])  # Timer
              self.writeVInt(i['TokensReward'])  # tokens reward for new event
              self.writeDataReference(15, i['ID'])  # MapID
              self.writeVInt(-64)  # GameModeVariation
              self.writeVInt(i['Status'])  # Status
              self.writeString()
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeVInt(0)
              if i['Modifier'] > 0:
                 self.writeBoolean(True)
                 self.writeVInt(i['Modifier']) #Modifer ID
              else:
                 self.writeBoolean(False)
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # Map Maker Map Structure Array
              self.writeVInt(0)
              self.writeBoolean(False)  # Power League Data Array
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # ChronosTextEntry
              self.writeBoolean(False)
              self.writeBoolean(False)
              self.writeVInt(-1)
              self.writeBoolean(False)
              self.writeBoolean(False)
              # Default Slots End Array #

        # Championship Challenge Slot Start Array #
        # Championship Challenge Stage 1 #
        self.writeVInt(0)
        self.writeVInt(20)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 10)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(7) #Challenge Variation
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(True)  # ChronosTextEntry
        self.writeInt(0)
        self.writeString("Grom Challenge")
        self.writeBoolean(True)# Stage Name
        self.writeInt(0)
        self.writeString("Stage 1")
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeVInt(0) # Count
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        
        # Championship Challenge Stage 2 #   
        self.writeVInt(0)
        self.writeVInt(21)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 53)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(7) #Challenge Variation
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(2) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(True)  # ChronosTextEntry
        self.writeInt(0)
        self.writeString("Grom Challenge")
        self.writeBoolean(True)# Stage Name
        self.writeInt(0)
        self.writeString("Stage 2")
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeVInt(0) # Count
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        
        # Championship Challenge Stage 3 #   
        self.writeVInt(0)
        self.writeVInt(22)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 293)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(7) # Challenge Varuation
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(True)  # ChronosTextEntry
        self.writeInt(0)
        self.writeString("Grom Challenge")
        self.writeBoolean(True) # Stage Name
        self.writeInt(0)
        self.writeString("Stage 3")
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeVInt(0) # Count
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        # Championship Slots End Array #
        
        # Club League Slots Start Array #
        # Club League Default Map Array #
        self.writeVInt(0)
        self.writeVInt(16)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 7)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Club League Power Match Array #
        self.writeVInt(0)
        self.writeVInt(17)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 25)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString() 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        # Club League Slots End Array #
        
        # Power League Solo Mode #
        self.writeVInt(0)
        self.writeVInt(14)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(0, 0)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_10") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(30) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(83) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(84) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(467) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Power League Team Mode #
        self.writeVInt(0)
        self.writeVInt(15)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(0, 0)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_10") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(30) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(83) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(84) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(467) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)


        EventsData = StaticData.EventsData
        
        self.writeVInt(len(EventsData) + 7) # Events Count(7 it a ChampionShip(3 Stages) and ClubLeague(PowerMatch and Default Game Mode)) and PowerLeague(Solo and Team Mode)
        for i in EventsData:
              # Default Slots Start Array #
              self.writeVInt(0)
              self.writeVInt(EventsData.index(i) + 1)  # EventType
              self.writeVInt(i['CountdownTimer'])  # EventsBeginCountdown
              self.writeVInt(i['Timer'])  # Timer
              self.writeVInt(i['TokensReward'])  # tokens reward for new event
              self.writeDataReference(15, i['ID'])  # MapID
              self.writeVInt(-64)  # GameModeVariation
              self.writeVInt(i['Status'])  # Status
              self.writeString()
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeVInt(0)
              if i['Modifier'] > 0:
                 self.writeBoolean(True)
                 self.writeVInt(i['Modifier']) #Modifer ID
              else:
                 self.writeBoolean(False)
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # Map Maker Map Structure Array
              self.writeVInt(0)
              self.writeBoolean(False)  # Power League Data Array
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # ChronosTextEntry
              self.writeBoolean(False)
              self.writeBoolean(False)
              self.writeVInt(-1)
              self.writeBoolean(False)
              self.writeBoolean(False)
              # Default Slots End Array #

        # Championship Challenge Slot Start Array #
        # Championship Challenge Stage 1 #
        self.writeVInt(0)
        self.writeVInt(20)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 10)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(7) #Challenge Variation
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(True)  # ChronosTextEntry
        self.writeInt(0)
        self.writeString("Grom Challenge")
        self.writeBoolean(True)# Stage Name
        self.writeInt(0)
        self.writeString("Stage 1")
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeVInt(0) # Count
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        
        # Championship Challenge Stage 2 #   
        self.writeVInt(0)
        self.writeVInt(21)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 53)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(7) #Challenge Variation
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(2) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(True)  # ChronosTextEntry
        self.writeInt(0)
        self.writeString("Grom Challenge")
        self.writeBoolean(True)# Stage Name
        self.writeInt(0)
        self.writeString("Stage 2")
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeVInt(0) # Count
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        
        # Championship Challenge Stage 3 #   
        self.writeVInt(0)
        self.writeVInt(22)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 293)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(7) # Challenge Varuation
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(True)  # ChronosTextEntry
        self.writeInt(0)
        self.writeString("Grom Challenge")
        self.writeBoolean(True) # Stage Name
        self.writeInt(0)
        self.writeString("Stage 3")
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeVInt(0) # Count
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        self.writeBoolean(True) # Array
        self.writeInt(0) # ?
        # Championship Slots End Array #
        
        # Club League Slots Start Array #
        # Club League Default Map Array #
        self.writeVInt(0)
        self.writeVInt(16)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 7)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Club League Power Match Array #
        self.writeVInt(0)
        self.writeVInt(17)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 25)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString() 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        # Club League Slots End Array #
        
        # Power League Solo Mode #
        self.writeVInt(0)
        self.writeVInt(14)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(0, 0)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_10") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(30) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(83) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(84) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(467) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Power League Team Mode #
        self.writeVInt(0)
        self.writeVInt(15)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(0, 0)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeString("TID_BRAWL_PASS_SEASON_10") # Name Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3) # Quests Count
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(30) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(83) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(84) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(467) # SkinID
        
        self.writeVInt(19) # Road Count
        
        self.writeVInt(1) # Rank
        self.writeVInt(500) # Starpoints
        self.writeVInt(2) # Rank
        self.writeVInt(1000) # Starpoints
        self.writeVInt(3)  # Rank
        self.writeVInt(2000) # Starpoints
        self.writeVInt(4)  # Rank
        self.writeVInt(2500) # Starpoints
        self.writeVInt(5)  # Rank
        self.writeVInt(3000) # Starpoints
        self.writeVInt(6)  # Rank
        self.writeVInt(3750) # Starpoints
        self.writeVInt(7)  # Rank
        self.writeVInt(4500) # Starpoints
        self.writeVInt(8)  # Rank
        self.writeVInt(5500) # Starpoints
        self.writeVInt(9)  # Rank
        self.writeVInt(7000) # Starpoints
        self.writeVInt(10)  # Rank
        self.writeVInt(8750) # Starpoints
        self.writeVInt(11)  # Rank
        self.writeVInt(10000) # Starpoints
        self.writeVInt(12)  # Rank
        self.writeVInt(12500) # Starpoints
        self.writeVInt(13)  # Rank
        self.writeVInt(15000) # Starpoints
        self.writeVInt(14)  # Rank
        self.writeVInt(17500) # Starpoints
        self.writeVInt(15)  # Rank
        self.writeVInt(20000) # Starpoints
        self.writeVInt(16)  # Rank
        self.writeVInt(25000) # Starpoints
        self.writeVInt(17)  # Rank
        self.writeVInt(30000) # Starpoints
        self.writeVInt(18)  # Rank
        self.writeVInt(40000) # Starpoints
        self.writeVInt(19)  # Rank
        self.writeVInt(50000) # Starpoints
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0) # ReleaseEntry

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000039)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 0) # Graveyard Shift
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(48, 36217)
        self.writeLong(29, 14)  # Skin Group Active For Campaign
        self.writeLong(47, 41381)
        self.writeLong(50, 1)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 1)  # Double Token Event
        self.writeLong(31, 0)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)

        self.writeVInt(3)  # Timed Int Value Entry

        self.writeVInt(14)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(739760) # Time left

        self.writeVInt(29)
        self.writeVInt(10)
        self.writeVInt(79)
        self.writeVInt(691200) # Time left

        self.writeVInt(29)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(1330340) # Time left

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        fields["Unk1"] = calling_instance.readString()
        fields["Unk2"] = calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 204