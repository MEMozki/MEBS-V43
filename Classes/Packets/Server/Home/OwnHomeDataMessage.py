import time

from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Static.StaticData import StaticData
from Classes.Files.Classes.Cards import Cards
import Configuration

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(player.Trophies) # Trophies
        self.writeVInt(player.HighestTrophies) # Highest Trophies
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(0)

        self.writeVInt(len(player.SelectedSkins)) # Selected Skins
        for skinID in player.SelectedSkins:
        	self.writeDataReference(29, skinID)

        self.writeVInt(0) # Randomizer Skin Selected

        self.writeVInt(0) # Current Random Skin

        self.writeVInt(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVInt(0) # Unlocked Skin Purchase Option

        self.writeVInt(0) # New Item State

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(999999) # Trophy Road Timer
        self.writeVInt(999999) # Power Play Timer(Don't work')
        self.writeVInt(999999) # Brawl Pass Timer

        self.writeVInt(999)
        self.writeVInt(999)

        self.writeVInt(5)

        self.writeVInt(999)
        self.writeVInt(999)
        self.writeVInt(999)
        self.writeVInt(999)
        self.writeVInt(999)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(0)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change

        '''
        0: FREE BOX
        1: COINS
        2: RANDOM BRAWLER RARITY
        3: BRAWLER
        4: SKIN
        5: ?
        6: BRAWL BOX
        7: TICKETS
        8: POWER POINTS
        9: TOKEN DOUBLER
        10: MEGA BOX
        11: ?
        12: POWER POINTS
        13: NEW EVENT SLOT
        14: BIG BOX
        15: BRAWL BOX
        16: GEMS
        17: STAR POINTS
        18: QUEST???
        19: PIN
        20: SET OF PINS
        21: PIN PACK
        22: PIN PACK FOR
        23: PIN OF RARITY
        24: ?
        25: ?
        26: ?
        27: PIN PACK OF RARITY
        28: ?
        29: ?
        30: NEW BRAWLER UPGRADED TO LEVEL
        31: RANDOM BRAWLER OF RARITY UPGRADED TO LEVEL
        32: GEAR TOKENS
        33: SCRAP
        '''

        ShopData = StaticData.ShopData

        self.writeVInt(3 + len(ShopData["Offers"])) # Offers count

        self.writeVInt(1)  # RewardCount
        for i in range(1):
            self.writeVInt(6)  # ItemType
            self.writeVInt(0) # Amount
            self.writeDataReference(0)  # BrawlerID
            self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems,1-Gold,3-StarpoInts)
        self.writeVInt(1) #Cost
        self.writeVInt(172800) #Time
        self.writeVInt(2) # State
        self.writeVInt(0)
        if -3 in player.PushasedOffers:
            self.writeBoolean(True) # Claim
        else:
            self.writeBoolean(True) # Claim
        self.writeVInt(0) # Offer Index
        self.writeVInt(0)
        self.writeBoolean(False) #Daily Offer
        self.writeVInt(1) # Old price
        self.writeInt(0)
        self.writeString("Unlock all brawlers") # Text
        self.writeBoolean(False)
        self.writeString("offer_stuntshow") # Background
        self.writeVInt(-1)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(1) # Type Benefit
        self.writeVInt(100) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # unk
        self.writeDataReference(0, 0)
        self.writeDataReference(0, 0)
        
        self.writeVInt(2)  # RewardCount
        for i in range(1):
            self.writeVInt(1)  # ItemType
            self.writeVInt(1000) # Amount
            self.writeDataReference(0)  # CsvID
            self.writeVInt(0) # SkinID
        for i in range(1):
            self.writeVInt(16)  # ItemType
            self.writeVInt(250) # Amount
            self.writeDataReference(0)  # BrawlerID
            self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems,1-Gold,3-StarpoInts)
        self.writeVInt(0) #Cost
        self.writeVInt(172800) #Time
        self.writeVInt(2) # State
        self.writeVInt(0)
        if -2 in player.PushasedOffers:
            self.writeBoolean(True) # Claim
        else:
            self.writeBoolean(True) # Claim
        self.writeVInt(1) # Offer Index
        self.writeVInt(0)
        self.writeBoolean(False) #Daily Offer
        self.writeVInt(549) # Old price
        self.writeInt(0)
        self.writeString("Gift🤑") # Text
        self.writeBoolean(False)
        self.writeString("offer_stuntshow") # Background
        self.writeVInt(-1)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(2) # Type Benefit
        self.writeVInt(300) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Unk
        self.writeDataReference(0, 0)
        self.writeDataReference(0, 0)
        
        self.writeVInt(3)  # RewardCount
        for i in range(1):
            self.writeVInt(4)  # ItemType
            self.writeVInt(0) # Amount
            self.writeDataReference(16,1)  # BrawlerID
            self.writeVInt(376) # SkinID
        for i in range(1):
            self.writeVInt(19)  # ItemType
            self.writeVInt(250) # Amount
            self.writeDataReference(52, 272)  # CsvID
            self.writeVInt(272) # SkinID
        for i in range(1):
            self.writeVInt(9)  # ItemType
            self.writeVInt(1000) # Amount
            self.writeDataReference(0)  # BrawlerID
            self.writeVInt(1000) # SkinID

        self.writeVInt(0) # Currency(0-Gems,1-Gold,3-StarpoInts)
        self.writeVInt(109) #Cost
        self.writeVInt(172800) #Time
        self.writeVInt(2) # State
        self.writeVInt(0)
        if -1 in player.PushasedOffers:
            self.writeBoolean(True) # Claim
        else:
            self.writeBoolean(False) # Claim
        self.writeVInt(2) # Offer Index
        self.writeVInt(0)
        self.writeBoolean(False) #Daily Offer
        self.writeVInt(159) # Old price
        self.writeInt(0)
        self.writeString("АКЦИЯ К ДНЮ НЕЗАВИСИМОСТИ") # Text
        self.writeBoolean(False)
        self.writeString("offer_stuntshow") # Background
        self.writeVInt(-1)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(1) # Type Benefit
        self.writeVInt(2) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Unk
        self.writeDataReference(0, 0)
        self.writeDataReference(0, 0)

        for i in ShopData["Offers"]:
            self.writeVInt(len(i["Rewards"]))  # RewardCount
            for reward in i["Rewards"]:
                self.writeVInt(reward["ItemType"]) # ItemType
                self.writeVInt(reward["Amount"])
                if reward["BrawlerID"][0] != 0:
                    self.writeDataReference(reward["BrawlerID"][0], reward["BrawlerID"][1]) # CsvID
                else:
                    self.writeDataReference(0)
                self.writeVInt(reward["Extra"])

            self.writeVInt(i["Currency"])
            self.writeVInt(i["Cost"])
            self.writeVInt(i["Time"])
            self.writeVInt(0) # ?
            self.writeVInt(0)
            if ShopData["Offers"].index(i) in player.PushasedOffers:
            	self.writeBoolean(True) # Claim
            else:
            	self.writeBoolean(i['Claim']) # Claim
            self.writeVInt(ShopData["Offers"].index(i) + 3) # Offer Index
            self.writeVInt(0)
            self.writeBoolean(i["DailyOffer"])
            self.writeVInt(i["OldPrice"])
            self.writeInt(0)
            if i["Text"] == "None":
                self.writeString()
            else:
                self.writeString(i["Text"])
            self.writeBoolean(False)
            if i["Background"] == "None":
                self.writeString()
            else:
                self.writeString(i["Background"])
            self.writeVInt(-1)
            self.writeBoolean(i["Processed"])
            self.writeVInt(i["TypeBenefit"])
            self.writeVInt(i["Benefit"])
            self.writeString()
            self.writeBoolean(i["OneTimeOffer"])
            self.writeBoolean(False) # Unk
            self.writeDataReference(0, 0)
            self.writeDataReference(0, 0)

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVInt(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, player.TokensGained)  # TokensGained
        player.TokensGained = 0
        self.writeLong(4, player.TrophiesGained)  # TrophiesGained
        player.TrophiesGained = 0
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        if player.StarPoints == 0:
        	self.writeLong(9, 0)  # HideStarPoInts
        else:
        	self.writeLong(9, 1)  # ShowStarPoInts
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        if Configuration.settings["GoldRushEvent"] == True:
        	self.writeLong(14, player.CoinsGained)  # CoinsGained
        else:
        	self.writeLong(14, 0)  # CoinsGained
        player.CoinsGained = 0
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 0)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 0)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 0)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0)

        self.writeVInt(2)  # Brawlpass
        for i in range(10, 12):
            self.writeVInt(i)
            if i == 10:
            	self.writeVInt(34500)
            elif i == 11:
            	self.writeVInt(34500 + player.BPTokens)
            else:
            	self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0)

            self.writeByte(2)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVInt(0)

        QuestsData = StaticData.QuestsData
        self.writeBoolean(True) # LogicQuests
        self.writeVInt(len(QuestsData))
        for x in range(1):
        		for i in QuestsData:
        			self.writeVInt(0) # Unk
        			self.writeVInt(0) # Unk
        			self.writeVInt(i['MissionType']) # Mission Type
        			self.writeVInt(i['AchievedGoal']) # Achieved Goal
        			self.writeVInt(i['QuestGoal']) # Quest Goal
        			self.writeVInt(i['RewardType'])# Quest Reward Type
        			self.writeVInt(i['Extra']) #Quest Extra
        			self.writeBoolean(False) # Array
        			self.writeVInt(0) # Unk
        			self.writeVInt(0) # Unk
        			self.writeVInt(i['CurrentLevel']) # Current LVL
        			self.writeVInt(i['MaxLevel']) # Max LVL
        			self.writeVInt(i['Timer']) # Timer
        			self.writeInt8(i['State']) # Quest State
        			self.writeDataReference(16, i['BrawlerID']) # Brawler(16, <BrawlerID>)
        			self.writeVInt(i['GameMode']) # GameMode
        			self.writeVInt(0) # Unk
        			self.writeVInt(0) # Unk
        			self.writeVInt(0) # Unk
        
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(True) # Power League Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeVInt(17) # Rank Solo League
        self.writeVInt(7) # Season
        self.writeVInt(19) # Rank Team League
        self.writeVInt(0) # Unk
        self.writeVInt(17) # High Rank Solo League
        self.writeVInt(0) # Unk
        self.writeVInt(19) # High Rank Team League
        self.writeVInt(0) # Unk
        self.writeBoolean(True) # Eligibility for an award
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Array
        # Power League Data Array End #

        self.writeInt(0)

        self.writeVInt(0)

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
        self.writeVInt(0) #Challenge Variation
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
        self.writeBoolean(False) # Stage Rewards
        self.writeVInt(-1)
        self.writeBoolean(False) # Array
        self.writeBoolean(False) # Array
        
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
        self.writeVInt(0) #Challenge Variation
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
        self.writeBoolean(False) # Stage Rewards
        self.writeVInt(-1)
        self.writeBoolean(False) # Array
        self.writeBoolean(False) # Array
        
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
        self.writeVInt(0) # Challenge Variation
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
        self.writeBoolean(True) # Stage Rewards
        self.writeVInt(1)
        self.writeVInt(28)
        self.writeVInt(100)
        self.writeDataReference(0)
        self.writeVInt(0)
        self.writeVInt(-1)
        self.writeBoolean(False) # Challenge Final Reward
        self.writeBoolean(False) # Array
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
        self.writeVInt(8) # Season
        self.writeString("Шоу") # Name Season
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
        self.writeVInt(87) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(88) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(504) # SkinID
        
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
        self.writeVInt(8) # Season
        self.writeString("Шоу") # Name Season
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
        self.writeVInt(87) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(2) # Quest Type
        self.writeVInt(7) # Rank
        self.writeVInt(1) # Item Array
        self.writeVInt(25) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(88) # Thumbnail ID
        
        self.writeByte(3) # LogicRewardConfig
        self.writeByte(4) # Quest Type
        self.writeVInt(60) # Wins need
        self.writeVInt(1) # Item Array
        self.writeVInt(26) # ItemType
        self.writeVInt(1) 
        self.writeVInt(0)
        self.writeVInt(504) # SkinID
        
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

        self.writeVInt(0) # Comming Events

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0) # ReleaseEntry

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000000 + Configuration.settings["Theme"])  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 0) # Garveyard Shift
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(29, Configuration.settings["SkinPack"])  # Skin Group Active For Campaign
        self.writeLong(48, 26217)
        self.writeLong(50, 1)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, Configuration.settings["DoubleTokenEvent"])  # Double Token Event
        self.writeLong(31, Configuration.settings["GoldRushEvent"])  # Gold rush event
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
        self.writeVInt(15)
        self.writeVInt(0)
        self.writeVInt(691200) # Time left

        self.writeVInt(29)
        self.writeVInt(10)
        self.writeVInt(0)
        self.writeVInt(1330340) # Time left

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        notification = player.NotificationFactory
        self.writeVInt(len(notification)) # Notification Count
        for x in notification:
        	# BaseNotification::encode
        	self.writeVInt(x["Type"])
        	self.writeInt(x) # Notification Index
        	self.writeBoolean(x["Read"]) # Read
        	self.writeInt(x["Time"]) # Time Ago
        	self.writeString(x["Text"])
        	self.writeVInt(0)
        	if x["Type"] == 81:
        		self.writeVInt(1)
        	if x["Type"] == 72 or x["Type"] == 94:
        		DataRef = str(x["DataRef"][0]) + "000000"
        		Item = int(DataRef) + x["DataRef"][1]
        		self.writeVInt(Item)

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVInt(16)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(player.ClubCoins) # Club coins

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0)


        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        

        self.writeVInt(player.Gems)  # Diamonds
        self.writeVInt(player.Gems)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(5)
        self.writeVInt(0)
        self.writeVInt(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
