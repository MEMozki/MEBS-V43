import json
import random
import string
from Classes.Files.Classes.Cards import Cards


class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    AllianceID = [0, 0]
    Token = ""
    Name = "Brawler"
    Registered = False
    Thumbnail = 0
    Namecolor = 0
    Region = "RU"
    ContentCreator = "MEBS"

    Coins = 6000
    CoinsGained = 0
    Gems = 45000
    StarPoints = 6500
    ClubCoins = 600
    Trophies = 0
    HighestTrophies = 0
    TrophiesGained = 0
    TrophyRoadTier = 99999
    Experience = 250
    Level = 500
    Tokens = 200
    TokensGained = 0
    TokensDoubler = 0
    
    PushasedOffers = []
    
    delivery_items = {}
    
    BattleLogs = {}
    
    banned = False
    
    BPTokens = 5000
    
    NotificationFactory = {}

    SelectedSkins = []
    SelectedBrawlers = [0, 1, 8]
    RandomizerSelectedSkins = []
    OwnedPins = []
    OwnedThumbnails = []
    SelectedBrawlersSkins = {
        0: 0,
        1: 0,
        8: 0,
    }
    OwnedBrawlers = {
        0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
        1: {'CardID': 4, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
        8: {'CardID': 32, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 or lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(1, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(1, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'AllianceID': self.AllianceID,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'CoinsGained': self.CoinsGained,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,
            'ClubCoins': self.ClubCoins,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophiesGained': self.TrophiesGained,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensGained': self.TokensGained,
            'TokensDoubler': self.TokensDoubler,
            'PushasedOffers': self.PushasedOffers,
            'delivery_items': self.delivery_items,
            'BattleLogs': self.BattleLogs,
            'banned': self.banned,
            'BPTokens': self.BPTokens,
            'NotificationFactory': self.NotificationFactory,
            'SelectedSkins': self.SelectedSkins,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
