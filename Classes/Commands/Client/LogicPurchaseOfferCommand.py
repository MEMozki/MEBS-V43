import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
from Classes.ByteStream import ByteStream
import random


OwnedBrawlersLatest = {
    0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    1: {'CardID': 4, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    2: {'CardID': 8, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    3: {'CardID': 12, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    4: {'CardID': 16, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    5: {'CardID': 20, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    6: {'CardID': 24, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    7: {'CardID': 28, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    8: {'CardID': 32, 'Skins': [435], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    9: {'CardID': 36, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    10: {'CardID': 40, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    11: {'CardID': 44, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    12: {'CardID': 48, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    13: {'CardID': 52, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    14: {'CardID': 56, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    15: {'CardID': 60, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    16: {'CardID': 64, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    17: {'CardID': 68, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    18: {'CardID': 72, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    19: {'CardID': 95, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    20: {'CardID': 100, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    21: {'CardID': 105, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    22: {'CardID': 110, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    23: {'CardID': 115, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    24: {'CardID': 120, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    25: {'CardID': 125, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    26: {'CardID': 130, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    27: {'CardID': 177, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    28: {'CardID': 182, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    29: {'CardID': 188, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    30: {'CardID': 194, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    31: {'CardID': 200, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    32: {'CardID': 206, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    34: {'CardID': 218, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    35: {'CardID': 224, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    36: {'CardID': 230, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    37: {'CardID': 236, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    38: {'CardID': 279, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    39: {'CardID': 296, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    40: {'CardID': 303, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    41: {'CardID': 320, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    42: {'CardID': 327, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    43: {'CardID': 334, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    44: {'CardID': 341, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    45: {'CardID': 358, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    46: {'CardID': 365, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    47: {'CardID': 372, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    48: {'CardID': 379, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    49: {'CardID': 386, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    50: {'CardID': 393, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    51: {'CardID': 410, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    52: {'CardID': 417, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    53: {'CardID': 427, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    54: {'CardID': 434, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    56: {'CardID': 448, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    57: {'CardID': 466, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    58: {'CardID': 474, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
}

class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        if fields["Unk1"] == 0:
            player_data["OwnedBrawlers"] = OwnedBrawlersLatest
            player_data["PushasedOffers"].append(-3)
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            box['Type'] = 100
            a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54, 56]
            for x in a:
            	item = {'Amount': 1, 'DataRef': [16, x], 'RewardID': 1}
            	box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            
        if fields["Unk1"] == 2:
            player_data["TokensDoubler"] = player_data["TokensDoubler"] + 1000
            player_data["OwnedPins"].append(272)
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(376)
            player_data["PushasedOffers"].append(-1)
            player_data["Gems"] = player_data["Gems"] -109
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 376], 'RewardID': 9}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [52, 272], 'RewardID': 11}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1000, 'DataRef': [0, 0], 'RewardID': 2}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 4:
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            brawlers= list(player_data["OwnedBrawlers"].keys())
            pp1= random.randint(9,127)
            pp2 = random.randint(9,127)
            pp3 = random.randint(9,127)
            pp4 = random.randint(9,127)
            pp5 = random.randint(9,127)
            ppbr = random.randint(75, 120)
            brawlerID1= random.choice(brawlers)
            brawlerID2 = random.choice(brawlers)
            brawlerID3 = random.choice(brawlers)
            brawlerID4 = random.choice(brawlers)
            brawlerID5 = random.choice(brawlers)
            while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
        	    brawlerID2 = random.choice(brawlers)
            while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
        	    brawlerID3 = random.choice(brawlers)
            if len(brawlers) >= 4:
        	     while brawlerID4 == brawlerID1 or brawlerID4 == brawlerID2 or brawlerID4 == brawlerID3 or brawlerID4 == brawlerID5:
        	     	brawlerID4 = random.choice(brawlers)
            if len(brawlers) >= 5:
        	    while brawlerID5 == brawlerID1 or brawlerID5 == brawlerID2 or brawlerID5 == brawlerID3 or brawlerID5 == brawlerID4:
        	    	brawlerID5 = random.choice(brawlers)
            brawlerID6 = random.randint(0, 58)
            while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
            	brawlerID6 = random.randint(0, 58)
            gold = random.randint(53, 271)
            if random.randint(0, 10) == 7:
            	gems = random.randint(30, 90)
            elif random.randint(0, 5) == 2:
            	gems = random.randint(20, 50)
            else:
            	gems = random.randint(5, 30)
            box['Type'] = 11
            item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
            box['Items'].append(item)
            item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
            box['Items'].append(item)
            item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
            box['Items'].append(item)
            item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
            box['Items'].append(item)
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID1)]["CardID"]:
            		v["PowerPoints"] += pp1
            for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID2)]["CardID"]:
            			v["PowerPoints"] += pp2
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID3)]["CardID"]:
            		v["PowerPoints"] += pp3
            if len(brawlers) >= 4:
            	item = {'Amount': pp4, 'DataRef': [16, brawlerID4], 'RewardID': 6}
            	box['Items'].append(item)
            	for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID4)]["CardID"]:
            			v["PowerPoints"] += pp4
            if len(brawlers) >= 5:
            	item = {'Amount': pp5, 'DataRef': [16, brawlerID5], 'RewardID': 6}
            	box['Items'].append(item)
            	for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID5)]["CardID"]:
            			v["PowerPoints"] += pp5
            if random.randint(0, 5) == 3:
            	 item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
            	 box['Items'].append(item)
            	 player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            else:
            	 if random.randint(0, 3) == 2:
            	 	item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
            	 	box['Items'].append(item)
            if random.randint(0, 3) == 2:
              item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
              box['Items'].append(item)
              player_data["Gems"] += gems
            player_data["Gems"] -= 60
            player_data["Coins"] += gold
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 1:
            player_data["Coins"] = player_data["Coins"] + 1000
            player_data["Gems"] = player_data["Gems"] + 250
            player_data["PushasedOffers"].append(-2)
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1000, 'DataRef': [0, 0], 'Value': 250, 'RewardID': 7}
            box['Items'].append(item)
            box['Type'] = 100
            item = {'Amount': 250, 'DataRef': [0, 0], 'RewardID': 8}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 21:
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(434)
                if 433 and 432 and 434 and 441 in v["Skins"]:
                	player_data["OwnedPins"].append(649)
                	player_data["OwnedPins"].append(650)
                	player_data["OwnedPins"].append(651)
                	player_data["OwnedPins"].append(652)
                	player_data["OwnedPins"].append(653)
            player_data["Gems"] = player_data["Gems"] -149
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 434], 'RewardID': 9}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 19:
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(432)
                if 433 and 434 and 435 and 441 in v["Skins"]:
                	player_data["OwnedPins"].append(649)
                	player_data["OwnedPins"].append(650)
                	player_data["OwnedPins"].append(651)
                	player_data["OwnedPins"].append(652)
                	player_data["OwnedPins"].append(653)
            player_data["Gems"] = player_data["Gems"] -149
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 432], 'RewardID': 9}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 20:
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(433)
                if 432 and 434 and 435 and 441 in v["Skins"]:
                	player_data["OwnedPins"].append(649)
                	player_data["OwnedPins"].append(650)
                	player_data["OwnedPins"].append(651)
                	player_data["OwnedPins"].append(652)
                	player_data["OwnedPins"].append(653)
            player_data["Gems"] = player_data["Gems"] - 149
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 433], 'RewardID': 9}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 23:
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(441)
                if 433 and 432 and 434 and 435 in v["Skins"]:
                	player_data["OwnedPins"].append(649)
                	player_data["OwnedPins"].append(650)
                	player_data["OwnedPins"].append(651)
                	player_data["OwnedPins"].append(652)
                	player_data["OwnedPins"].append(653)
            player_data["Gems"] = player_data["Gems"] -149
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 441], 'RewardID': 9}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 22:
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(435)
                if 433 and 434 and 432 and 441 in v["Skins"]:
                	player_data["OwnedPins"].append(649)
                	player_data["OwnedPins"].append(650)
                	player_data["OwnedPins"].append(651)
                	player_data["OwnedPins"].append(652)
                	player_data["OwnedPins"].append(653)
            player_data["Gems"] = player_data["Gems"] -149
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 435], 'RewardID': 9}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 3:
            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            box['Type'] = 10
            brawlers= list(player_data["OwnedBrawlers"].keys())
            pp1= random.randint(9,69)
            pp2 = random.randint(9,69)
            pp3 = random.randint(9,69)
            ppbr = random.randint(20, 54)
            brawlerID1= random.choice(brawlers)
            brawlerID2 = random.choice(brawlers)
            brawlerID3 = random.choice(brawlers)
            while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
                brawlerID2 = random.choice(brawlers)
            while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
                brawlerID3 = random.choice(brawlers)
            brawlerID6 = random.randint(0, 58)
            while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
                brawlerID6 = random.randint(0, 58)
            player_data["delivery_items"]['Type'] = 10
            if random.randint(0, 15) == 3:
                item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
                box['Items'].append(item)
                player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            elif random.randint(0, 9) == 2:
                item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
                box['Items'].append(item)
            else:
                gold = random.randint(7, 59)
                if random.randint(0, 10) == 7:
                	gems = random.randint(15, 30)
                elif random.randint(0, 5) == 2:
                	gems = random.randint(7, 19)
                else:
                	gems = random.randint(3, 11)
                item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
                box['Items'].append(item)
                item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
                box['Items'].append(item)
                item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
                box['Items'].append(item)
                item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
                box['Items'].append(item)
                for i,v in player_data["OwnedBrawlers"].items():
                	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID1)]["CardID"]:
                		v["PowerPoints"] += pp1
                for i,v in player_data["OwnedBrawlers"].items():
                	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID2)]["CardID"]:
                		v["PowerPoints"] += pp2
                for i,v in player_data["OwnedBrawlers"].items():
                			if v["CardID"] == OwnedBrawlersLatest[int(brawlerID3)]["CardID"]:
                				v["PowerPoints"] += pp3
                if random.randint(0, 3) == 2:
                	 item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
                	 box['Items'].append(item)
                	 player_data["Gems"] += gems
                player_data["Coins"] += gold
                player_data["delivery_items"]['Boxes'].append(box)
        if fields["Unk1"] == 9:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(245)
            	player_data["Gems"] = player_data["Gems"] - 29
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
            	'Type': 0,
            	'Items': []
            	}
            	item = {'Amount': 1, 'DataRef': [29, 245], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 10:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(416)
            	player_data["Gems"] = player_data["Gems"] - 79
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 416], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 11:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(422)
            	player_data["Coins"] = player_data["Coins"] - 10000
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 422], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 12:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(356)
            	player_data["Gems"] = player_data["Gems"] - 79
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 356], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 13:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(381)
            	player_data["Gems"] = player_data["Gems"] - 79
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 381], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 14:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(233)
            	player_data["Gems"] = player_data["Gems"] - 79
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 233], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 15:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(359)
            	player_data["Gems"] = player_data["Gems"] - 149
            	player_data["OwnedPins"].append(550)
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 359], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)
            	box = {'Type': 0, 'Items': []}
            	item = {'Amount': 1, 'DataRef': [52, 550], 'RewardID': 11}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 16:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(310)
            	player_data["Gems"] = player_data["Gems"] - 79
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 310], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 17:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(99)
            	player_data["StarPoints"] = player_data["StarPoints"] - 50000
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 99], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 18:
            	for i,v in player_data["OwnedBrawlers"].items():
            		v["Skins"].append(267)
            	player_data["StarPoints"] = player_data["StarPoints"] - 10000
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [29, 267], 'RewardID': 9}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 25:
            	player_data["OwnedBrawlers"][52] = {'CardID': 417, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            	player_data["Gems"] = player_data["Gems"] - 109
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 1, 'DataRef': [16, 52], 'RewardID': 1}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 26:
            	player_data["OwnedBrawlers"][51] = {'CardID': 410, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            	player_data["Gems"] = player_data["Gems"] - 229
            	player_data["delivery_items"] = {
            	'Boxes': []
            	}
            	box = {
                'Type': 0,
                'Items': []
                }
            	item = {'Amount': 11, 'DataRef': [16, 51], 'RewardID': 1}
            	box['Type'] = 100
            	box['Items'].append(item)
            	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 27:
            player_data["OwnedBrawlers"][43] = {'CardID': 334, 'Skins': [281], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': 1, 'DataRef': [16, 43], 'RewardID': 1}
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [29, 281], 'RewardID': 9}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 28:
            player_data["Gems"] = player_data["Gems"] + 499
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': 499, 'DataRef': [0, 0], 'RewardID': 8}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)
            
        if fields["Unk1"] == 29:
            a = random.randint(0, 654)
            b = random.randint(0, 654)
            c = random.randint(0, 654)
            player_data["OwnedPins"].append(a)
            player_data["OwnedPins"].append(b)
            player_data["OwnedPins"].append(c)
            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {'Type': 0, 'Items': []}
            item = {'Amount': 1, 'DataRef': [52, a], 'RewardID': 11}
            box['Type'] = 100
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [52, b], 'RewardID': 11}
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [52, c], 'RewardID': 11}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 30:
            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {'Type': 0, 'Items': []}
            brawlers= list(player_data["OwnedBrawlers"].keys())
            pp1= random.randint(9,127)
            pp2 = random.randint(9,127)
            pp3 = random.randint(9,127)
            pp4 = random.randint(9,127)
            pp5 = random.randint(9,127)
            ppbr = random.randint(75, 120)
            brawlerID1= random.choice(brawlers)
            brawlerID2 = random.choice(brawlers)
            brawlerID3 = random.choice(brawlers)
            brawlerID4 = random.choice(brawlers)
            brawlerID5 = random.choice(brawlers)
            while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
        	    brawlerID2 = random.choice(brawlers)
            while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
        	    brawlerID3 = random.choice(brawlers)
            if len(brawlers) >= 4:
        	     while brawlerID4 == brawlerID1 or brawlerID4 == brawlerID2 or brawlerID4 == brawlerID3 or brawlerID4 == brawlerID5:
        	     	brawlerID4 = random.choice(brawlers)
            if len(brawlers) >= 5:
        	    while brawlerID5 == brawlerID1 or brawlerID5 == brawlerID2 or brawlerID5 == brawlerID3 or brawlerID5 == brawlerID4:
        	    	brawlerID5 = random.choice(brawlers)
            brawlerID6 = random.randint(0, 58)
            while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
                  brawlerID6 = random.randint(0, 58)
            gold = random.randint(53, 271)
            if random.randint(0, 10) == 7:
            	gems = random.randint(30, 90)
            elif random.randint(0, 5) == 2:
            	gems = random.randint(20, 50)
            else:
            	gems = random.randint(5, 30)
            box['Type'] = 11
            item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
            box['Items'].append(item)
            item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
            box['Items'].append(item)
            item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
            box['Items'].append(item)
            item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
            box['Items'].append(item)
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID1)]["CardID"]:
            		v["PowerPoints"] += pp1
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID2)]["CardID"]:
            		v["PowerPoints"] += pp2
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID3)]["CardID"]:
            		v["PowerPoints"] += pp3
            if len(brawlers) >= 4:
            	item = {'Amount': pp4, 'DataRef': [16, brawlerID4], 'RewardID': 6}
            	box['Items'].append(item)
            	for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID4)]["CardID"]:
            			v["PowerPoints"] += pp4
            if len(brawlers) >= 5:
            	item = {'Amount': pp5, 'DataRef': [16, brawlerID5], 'RewardID': 6}
            	box['Items'].append(item)
            	for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID5)]["CardID"]:
            			v["PowerPoints"] += pp5
            if random.randint(0, 5) == 3:
            	 item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
            	 box['Items'].append(item)
            	 player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            else:
            	 if random.randint(0, 3) == 2:
            	 	item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
            	 	box['Items'].append(item)
            if random.randint(0, 3) == 2:
              item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
              box['Items'].append(item)
              player_data["Gems"] += gems
            player_data["Gems"] -= 39
            player_data["Coins"] += gold
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 33:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(469)
        	       if 468 and 467 and 473 and 477 and 482 and 483 in v["Skins"]:
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 469], 'RewardID': 9}
        	box['Items'].append(item)
        	if 468 and 467 and 473 and 477 and 482 and 483 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 31:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(467)
        	       if 468 and 469 and 473 and 477 and 482 and 483 in v["Skins"]:
        	       	player_data["delivery_items"]['Boxes'].append(box)
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 467], 'RewardID': 9}
        	box['Items'].append(item)
        	if 468 and 469 and 473 and 477 and 482 and 483 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 32:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(468)
        	       if 467 and 469 and 473 and 477 and 482 and 483 in v["Skins"]:
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 468], 'RewardID': 9}
        	box['Items'].append(item)
        	if 467 and 469 and 473 and 477 and 482 and 483 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 35:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(477)
        	       if 468 and 469 and 473 and 467 and 482 and 483 in v["Skins"]:
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 477], 'RewardID': 9}
        	box['Items'].append(item)
        	if 468 and 469 and 473 and 467 and 482 and 483 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 34:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(473)
        	       if 468 and 469 and 467 and 477 and 482 and 483 in v["Skins"]:
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 473], 'RewardID': 9}
        	box['Items'].append(item)
        	if 468 and 469 and 467 and 477 and 482 and 483 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 36:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(482)
        	       if 468 and 469 and 473 and 477 and 467 and 483 in v["Skins"]:
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 482], 'RewardID': 9}
        	box['Items'].append(item)
        	if 468 and 469 and 473 and 477 and 467 and 483 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 37:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(483)
        	       if 468 and 469 and 473 and 477 and 482 and 467 in v["Skins"]:
        	       	player_data["OwnedPins"].append(679)
        	       	player_data["OwnedPins"].append(680)
        	       	player_data["OwnedPins"].append(681)
        	       	player_data["OwnedPins"].append(682)
        	       	player_data["OwnedPins"].append(683)
        	       	player_data["OwnedPins"].append(684)
        	       	player_data["OwnedPins"].append(685)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 483], 'RewardID': 9}
        	box['Items'].append(item)
        	if 468 and 469 and 473 and 477 and 482 and 467 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 679], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 680], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 681], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 682], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 683], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 684], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 685], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 24:
        	brawler = fields["Unk2"][1]
        	for i,v in player_data["OwnedBrawlers"].items():
        		if v["CardID"] == OwnedBrawlersLatest[brawler]["CardID"]:
        			v["PowerPoints"] += 250
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {
        	'Type': 0,
        	'Items': []
        	}
        	box['Type'] = 100
        	item = {'Amount': 250, 'DataRef': [16, brawler], 'RewardID': 6}
        	box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 38:
        	brawler = fields["Unk2"][1]
        	for i,v in player_data["OwnedBrawlers"].items():
        		if v["CardID"] == OwnedBrawlersLatest[brawler]["CardID"]:
        			v["PowerPoints"] += 100
        	player_data["Coins"] += 300
        	player_data["OwnedBrawlers"][35] = OwnedBrawlersLatest[35]
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {
        	'Type': 0,
        	'Items': []
        	}
        	box['Type'] = 100
        	item = {'Amount': 100, 'DataRef': [16, brawler], 'RewardID': 6}
        	box['Items'].append(item)
        	item = {'Amount': 300, 'DataRef': [0, 0], 'RewardID': 7}
        	box['Items'].append(item)
        	item = {'Amount': 1, 'DataRef': [16, 35], 'RewardID': 1}
        	box['Items'].append(item)
        	player_data["Gems"] -= 129
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 39:
        	brawler = fields["Unk2"][1]
        	for i,v in player_data["OwnedBrawlers"].items():
        		if v["CardID"] == OwnedBrawlersLatest[brawler]["CardID"]:
        			v["PowerPoints"] += 500
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {
        	'Type': 0,
        	'Items': []
        	}
        	item = {'Amount': 500, 'DataRef': [16, brawler], 'RewardID': 6}
        	box['Items'].append(item)
        	box['Type'] = 100
        	player_data["Gems"] -= 149
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 40:
            player_data["delivery_items"] = {
            'Boxes': []
            }
            for i in range(5):
            	box = {'Type': 0, 'Items': []}
            	brawlers= list(player_data["OwnedBrawlers"].keys())
            	pp1= random.randint(9,127)
            	pp2 = random.randint(9,127)
            	pp3 = random.randint(9,127)
            	pp4 = random.randint(9,127)
            	pp5 = random.randint(9,127)
            	ppbr = random.randint(75, 120)
            	brawlerID1= random.choice(brawlers)
            	brawlerID2 = random.choice(brawlers)
            	brawlerID3 = random.choice(brawlers)
            	brawlerID4 = random.choice(brawlers)
            	brawlerID5 = random.choice(brawlers)
            	while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
            		brawlerID2 = random.choice(brawlers)
            	while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
            		brawlerID3 = random.choice(brawlers)
            	if len(brawlers) >= 4:
            	 	while brawlerID4 == brawlerID1 or brawlerID4 == brawlerID2 or brawlerID4 == brawlerID3 or brawlerID4 == brawlerID5:
            	 		brawlerID4 = random.choice(brawlers)
            	if len(brawlers) >= 5:
            	 	while brawlerID5 == brawlerID1 or brawlerID5 == brawlerID2 or brawlerID5 == brawlerID3 or brawlerID5 == brawlerID4:
            	 		brawlerID5 = random.choice(brawlers)
            	brawlerID6 = random.randint(0, 58)
            	while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
            	 brawlerID6 = random.randint(0, 58)
            	gold = random.randint(53, 271)
            	if random.randint(0, 10) == 7:
            	 gems = random.randint(30, 90)
            	elif random.randint(0, 5) == 2:
            	 gems = random.randint(20, 50)
            	else:
            	 gems = random.randint(5, 30)
            	 box['Type'] = 11
            	 item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
            	 box['Items'].append(item)
            	 item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
            	 box['Items'].append(item)
            	 item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
            	 box['Items'].append(item)
            	 item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
            	 box['Items'].append(item)
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID1)]["CardID"]:
            	 		v["PowerPoints"] += pp1
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID2)]["CardID"]:
            	 		v["PowerPoints"] += pp2
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID3)]["CardID"]:
            	 		v["PowerPoints"] += pp3
            	 if len(brawlers) >= 4:
            	 	item = {'Amount': pp4, 'DataRef': [16, brawlerID4], 'RewardID': 6}
            	 	box['Items'].append(item)
            	 	for i,v in player_data["OwnedBrawlers"].items():
            	 		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID4)]["CardID"]:
            	 			v["PowerPoints"] += pp4
            	 if len(brawlers) >= 5:
            	 	item = {'Amount': pp5, 'DataRef': [16, brawlerID5], 'RewardID': 6}
            	 	box['Items'].append(item)
            	 	for i,v in player_data["OwnedBrawlers"].items():
            	 		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID5)]["CardID"]:
            	 			v["PowerPoints"] += pp5
            	 if random.randint(0, 5) == 3:
            	 	item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
            	 	box['Items'].append(item)
            	 	player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            	 else:
            	 	if random.randint(0, 3) == 2:
            	 		item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
            	 		box['Items'].append(item)
            	 if random.randint(0, 3) == 2:
            	 	item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
            	 	box['Items'].append(item)
            	 	player_data["Gems"] += gems
            	 player_data["Coins"] += gold
            	 player_data["delivery_items"]['Boxes'].append(box)
            player_data["Gems"] -= 240

        if fields["Unk1"] == 41:
            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {'Type': 0, 'Items': []}
            brawler = fields["Unk2"][1]
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[brawler]["CardID"]:
            		v["PowerPoints"] += 150
            box['Type'] = 100
            item = {'Amount': 150, 'DataRef': [16, brawler], 'RewardID': 6}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            a = random.randint(0, 654)
            b = random.randint(0, 654)
            c = random.randint(0, 654)
            player_data["OwnedPins"].append(a)
            player_data["OwnedPins"].append(b)
            player_data["OwnedPins"].append(c)
            box = {'Type': 0, 'Items': []}
            item = {'Amount': 1, 'DataRef': [52, a], 'RewardID': 11}
            box['Type'] = 100
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [52, b], 'RewardID': 11}
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [52, c], 'RewardID': 11}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            for i in range(2):
            	box = {'Type': 0, 'Items': []}
            	brawlers= list(player_data["OwnedBrawlers"].keys())
            	pp1= random.randint(9,127)
            	pp2 = random.randint(9,127)
            	pp3 = random.randint(9,127)
            	pp4 = random.randint(9,127)
            	pp5 = random.randint(9,127)
            	ppbr = random.randint(75, 120)
            	brawlerID1= random.choice(brawlers)
            	brawlerID2 = random.choice(brawlers)
            	brawlerID3 = random.choice(brawlers)
            	brawlerID4 = random.choice(brawlers)
            	brawlerID5 = random.choice(brawlers)
            	while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
            		brawlerID2 = random.choice(brawlers)
            	while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
            		brawlerID3 = random.choice(brawlers)
            	if len(brawlers) >= 4:
            	 	while brawlerID4 == brawlerID1 or brawlerID4 == brawlerID2 or brawlerID4 == brawlerID3 or brawlerID4 == brawlerID5:
            	 		brawlerID4 = random.choice(brawlers)
            	if len(brawlers) >= 5:
            	 	while brawlerID5 == brawlerID1 or brawlerID5 == brawlerID2 or brawlerID5 == brawlerID3 or brawlerID5 == brawlerID4:
            	 		brawlerID5 = random.choice(brawlers)
            	brawlerID6 = random.randint(0, 58)
            	while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
            	 brawlerID6 = random.randint(0, 58)
            	gold = random.randint(53, 271)
            	if random.randint(0, 10) == 7:
            	 gems = random.randint(30, 90)
            	elif random.randint(0, 5) == 2:
            	 gems = random.randint(20, 50)
            	else:
            	 gems = random.randint(5, 30)
            	 box['Type'] = 11
            	 item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
            	 box['Items'].append(item)
            	 item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
            	 box['Items'].append(item)
            	 item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
            	 box['Items'].append(item)
            	 item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
            	 box['Items'].append(item)
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID1)]["CardID"]:
            	 		v["PowerPoints"] += pp1
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID2)]["CardID"]:
            	 		v["PowerPoints"] += pp2
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID3)]["CardID"]:
            	 		v["PowerPoints"] += pp3
            	 if len(brawlers) >= 4:
            	 	item = {'Amount': pp4, 'DataRef': [16, brawlerID4], 'RewardID': 6}
            	 	box['Items'].append(item)
            	 	for i,v in player_data["OwnedBrawlers"].items():
            	 		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID4)]["CardID"]:
            	 			v["PowerPoints"] += pp4
            	 if len(brawlers) >= 5:
            	 	item = {'Amount': pp5, 'DataRef': [16, brawlerID5], 'RewardID': 6}
            	 	box['Items'].append(item)
            	 	for i,v in player_data["OwnedBrawlers"].items():
            	 		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID5)]["CardID"]:
            	 			v["PowerPoints"] += pp5
            	 if random.randint(0, 5) == 3:
            	 	item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
            	 	box['Items'].append(item)
            	 	player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            	 else:
            	 	if random.randint(0, 3) == 2:
            	 		item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
            	 		box['Items'].append(item)
            	 if random.randint(0, 3) == 2:
            	 	item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
            	 	box['Items'].append(item)
            	 	player_data["Gems"] += gems
            	 player_data["Coins"] += gold
            	 player_data["delivery_items"]['Boxes'].append(box)
            player_data["Gems"] -= 205

        if fields["Unk1"] == 42:
            player_data["Coins"] = player_data["Coins"] + 500
            player_data["Gems"] = player_data["Gems"] + 439
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 500, 'DataRef': [0, 0], 'RewardID': 7}
            box['Items'].append(item)
            box['Type'] = 100
            item = {'Amount': 439, 'DataRef': [0, 0], 'RewardID': 8}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 43:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(501)
        	if 502 and 510 in v["Skins"]:
        	    player_data["OwnedPins"].append(721)
        	    player_data["OwnedPins"].append(722)
        	    player_data["OwnedPins"].append(723)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 501], 'RewardID': 9}
        	box['Items'].append(item)
        	if 502 and 510 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 721], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 722], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 723], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 44:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(502)
        	if 501 and 510 in v["Skins"]:
        	    player_data["OwnedPins"].append(721)
        	    player_data["OwnedPins"].append(722)
        	    player_data["OwnedPins"].append(723)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 502], 'RewardID': 9}
        	box['Items'].append(item)
        	if 501 and 510 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 721], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 722], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 723], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 45:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(510)
        	if 502 and 501 in v["Skins"]:
        	    player_data["OwnedPins"].append(721)
        	    player_data["OwnedPins"].append(722)
        	    player_data["OwnedPins"].append(723)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 510], 'RewardID': 9}
        	box['Items'].append(item)
        	if 502 and 501 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 721], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 722], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 723], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 46:
        	player_data["OwnedThumbnails"].append(102)
        	player_data["Gems"] = player_data["Gems"] -50
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [28, 102], 'RewardID': 11}
        	box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 47:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(79)
        	if 162 and 284 and 285 and 506 in v["Skins"]:
        	    player_data["OwnedPins"].append(727)
        	    player_data["OwnedPins"].append(731)
        	    player_data["OwnedPins"].append(732)
        	    player_data["OwnedPins"].append(733)
        	    player_data["OwnedPins"].append(734)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 79], 'RewardID': 9}
        	box['Items'].append(item)
        	if 162 and 284 and 285 and 506 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 727], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 731], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 732], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 733], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 734], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 48:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(162)
        	if 79 and 284 and 285 and 506 in v["Skins"]:
        	    player_data["OwnedPins"].append(727)
        	    player_data["OwnedPins"].append(731)
        	    player_data["OwnedPins"].append(732)
        	    player_data["OwnedPins"].append(733)
        	    player_data["OwnedPins"].append(734)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 162], 'RewardID': 9}
        	box['Items'].append(item)
        	if 79 and 284 and 285 and 506 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 727], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 731], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 732], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 733], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 734], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 49:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(284)
        	if 162 and 79 and 285 and 506 in v["Skins"]:
        	    player_data["OwnedPins"].append(727)
        	    player_data["OwnedPins"].append(731)
        	    player_data["OwnedPins"].append(732)
        	    player_data["OwnedPins"].append(733)
        	    player_data["OwnedPins"].append(734)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 284], 'RewardID': 9}
        	box['Items'].append(item)
        	if 162 and 79 and 285 and 506 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 727], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 731], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 732], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 733], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 734], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 50:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(285)
        	if 162 and 284 and 79 and 506 in v["Skins"]:
        	    player_data["OwnedPins"].append(727)
        	    player_data["OwnedPins"].append(731)
        	    player_data["OwnedPins"].append(732)
        	    player_data["OwnedPins"].append(733)
        	    player_data["OwnedPins"].append(734)
        	player_data["Gems"] = player_data["Gems"] -149
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 285], 'RewardID': 9}
        	box['Items'].append(item)
        	if 162 and 284 and 79 and 506 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 727], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 731], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 732], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 733], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 734], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 51:
        	for i,v in player_data["OwnedBrawlers"].items():
        	       v["Skins"].append(506)
        	if 162 and 284 and 285 and 79 in v["Skins"]:
        	    player_data["OwnedPins"].append(727)
        	    player_data["OwnedPins"].append(731)
        	    player_data["OwnedPins"].append(732)
        	    player_data["OwnedPins"].append(733)
        	    player_data["OwnedPins"].append(734)
        	player_data["Gems"] = player_data["Gems"] -79
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {'Type': 0, 'Items': []}
        	box['Type'] = 100
        	item = {'Amount': 1, 'DataRef': [29, 506], 'RewardID': 9}
        	box['Items'].append(item)
        	if 162 and 284 and 285 and 79 in v["Skins"]:
        		player_data["delivery_items"]['Boxes'].append(box)
        		box = {'Type': 0, 'Items': []}
        		box['Type'] = 100
        		item = {'Amount': 1, 'DataRef': [52, 727], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 731], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 732], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 733], 'RewardID': 11}
        		box['Items'].append(item)
        		item = {'Amount': 1, 'DataRef': [52, 734], 'RewardID': 11}
        		box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)

        if fields["Unk1"] == 52:
            player_data["OwnedThumbnails"].append(104)
            player_data["Coins"] = player_data["Coins"] + 2500
            brawler = fields["Unk2"][1]
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[brawler]["CardID"]:
            		v["PowerPoints"] += 150
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [28, 104], 'RewardID': 11}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)
            box = {
            'Type': 0,
            'Items': []
            }
            box['Type'] = 100
            item = {'Amount': 2500, 'DataRef': [0, 0], 'RewardID': 7}
            box['Items'].append(item)
            item = {'Amount': 150, 'DataRef': [16, brawler], 'RewardID': 6}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            player_data["Gems"] = player_data["Gems"] - 259

        if fields["Unk1"] == 53:
            player_data["delivery_items"] = {
            'Boxes': []
            }
            for i in range(10):
            	box = {'Type': 0, 'Items': []}
            	brawlers= list(player_data["OwnedBrawlers"].keys())
            	pp1= random.randint(9,127)
            	pp2 = random.randint(9,127)
            	pp3 = random.randint(9,127)
            	pp4 = random.randint(9,127)
            	pp5 = random.randint(9,127)
            	ppbr = random.randint(75, 120)
            	brawlerID1= random.choice(brawlers)
            	brawlerID2 = random.choice(brawlers)
            	brawlerID3 = random.choice(brawlers)
            	brawlerID4 = random.choice(brawlers)
            	brawlerID5 = random.choice(brawlers)
            	while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
            		brawlerID2 = random.choice(brawlers)
            	while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
            		brawlerID3 = random.choice(brawlers)
            	if len(brawlers) >= 4:
            	 	while brawlerID4 == brawlerID1 or brawlerID4 == brawlerID2 or brawlerID4 == brawlerID3 or brawlerID4 == brawlerID5:
            	 		brawlerID4 = random.choice(brawlers)
            	if len(brawlers) >= 5:
            	 	while brawlerID5 == brawlerID1 or brawlerID5 == brawlerID2 or brawlerID5 == brawlerID3 or brawlerID5 == brawlerID4:
            	 		brawlerID5 = random.choice(brawlers)
            	brawlerID6 = random.randint(0, 58)
            	while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
            	 brawlerID6 = random.randint(0, 58)
            	gold = random.randint(53, 271)
            	if random.randint(0, 10) == 7:
            	 gems = random.randint(30, 90)
            	elif random.randint(0, 5) == 2:
            	 gems = random.randint(20, 50)
            	else:
            	 gems = random.randint(5, 30)
            	 box['Type'] = 11
            	 item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
            	 box['Items'].append(item)
            	 item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
            	 box['Items'].append(item)
            	 item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
            	 box['Items'].append(item)
            	 item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
            	 box['Items'].append(item)
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID1)]["CardID"]:
            	 		v["PowerPoints"] += pp1
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID2)]["CardID"]:
            	 		v["PowerPoints"] += pp2
            	 for i,v in player_data["OwnedBrawlers"].items():
            	 	if v["CardID"] == OwnedBrawlersLatest[int(brawlerID3)]["CardID"]:
            	 		v["PowerPoints"] += pp3
            	 if len(brawlers) >= 4:
            	 	item = {'Amount': pp4, 'DataRef': [16, brawlerID4], 'RewardID': 6}
            	 	box['Items'].append(item)
            	 	for i,v in player_data["OwnedBrawlers"].items():
            	 		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID4)]["CardID"]:
            	 			v["PowerPoints"] += pp4
            	 if len(brawlers) >= 5:
            	 	item = {'Amount': pp5, 'DataRef': [16, brawlerID5], 'RewardID': 6}
            	 	box['Items'].append(item)
            	 	for i,v in player_data["OwnedBrawlers"].items():
            	 		if v["CardID"] == OwnedBrawlersLatest[int(brawlerID5)]["CardID"]:
            	 			v["PowerPoints"] += pp5
            	 if random.randint(0, 5) == 3:
            	 	item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
            	 	box['Items'].append(item)
            	 	player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            	 else:
            	 	if random.randint(0, 3) == 2:
            	 		item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
            	 		box['Items'].append(item)
            	 if random.randint(0, 3) == 2:
            	 	item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
            	 	box['Items'].append(item)
            	 	player_data["Gems"] += gems
            	 player_data["Coins"] += gold
            	 player_data["delivery_items"]['Boxes'].append(box)
            player_data["Gems"] -= 319

        if fields["Unk1"] == 54:
            a = random.randint(0, 654)
            b = random.randint(0, 654)
            c = random.randint(0, 654)
            player_data["OwnedPins"].append(a)
            player_data["OwnedPins"].append(b)
            player_data["OwnedPins"].append(c)
            player_data["Coins"] += 2000
            player_data["delivery_items"] = {
            'Boxes': []
            }
            box = {'Type': 0, 'Items': []}
            item = {'Amount': 2000, 'DataRef': [0, 0], 'RewardID': 7}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
            box = {'Type': 0, 'Items': []}
            item = {'Amount': 1, 'DataRef': [52, a], 'RewardID': 11}
            box['Type'] = 100
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [52, b], 'RewardID': 11}
            box['Items'].append(item)
            item = {'Amount': 1, 'DataRef': [52, c], 'RewardID': 11}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)
                       
        if fields["Unk1"] == 55:
            player_data["Coins"] = player_data["Coins"] + 500
            player_data["Gems"] = player_data["Gems"] + 50
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 500, 'DataRef': [0, 0],  'RewardID': 7}
            box['Items'].append(item)
            box['Type'] = 100
            item = {'Amount': 50, 'DataRef': [0, 0], 'RewardID': 8}
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)     
             
        if fields["Unk1"] == 56:
            player_data["Coins"] = player_data["Coins"] + 50000
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 50000, 'DataRef': [0, 0],  'RewardID': 7}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)                      
        if fields["Unk1"] == 57:
            player_data["OwnedBrawlers"][54] = {'CardID': 434, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': 1, 'DataRef': [16, 54], 'RewardID': 1}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)   
        if fields["Unk1"] == 58:
            player_data["OwnedPins"].append(625)
            player_data["PushasedOffers"].append(-1)
            player_data["Gems"] = player_data["Gems"] -19
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [52, 625], 'RewardID': 11}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)
        if fields["Unk1"] == 59:
            player_data["OwnedBrawlers"][41] = {'CardID': 320, 'Skins': [265], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            for i,v in player_data["OwnedBrawlers"].items():
                v["Skins"].append(265)
            player_data["PushasedOffers"].append(-1)
            player_data["Gems"] = player_data["Gems"] - 89
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [16, 41], 'RewardID': 1}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)   
            box = {
        	'Type': 0,
        	'Items': []
        	}
            item = {'Amount': 1, 'DataRef': [29, 266], 'RewardID': 9}
            box['Items'].append(item)
            box['Type'] = 100
            player_data["delivery_items"]['Boxes'].append(box)    
        if fields["Unk1"] == 60:
            player_data["OwnedBrawlers"][49] = {'CardID': 386, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
            player_data["delivery_items"] = {
                'Boxes': []
            }
            box = {
            'Type': 0,
            'Items': []
            }
            item = {'Amount': 1, 'DataRef': [16, 49], 'RewardID': 1}
            box['Type'] = 100
            box['Items'].append(item)
            player_data["delivery_items"]['Boxes'].append(box)   
               
        if fields["Unk1"] - 3 != 0:
        	player_data["PushasedOffers"].append(fields["Unk1"] - 3)
        	db_instance.updatePlayerData(player_data, calling_instance)
        	fields["Socket"] = calling_instance.client
        	fields["Command"] = {"ID": 203}
        	fields["PlayerID"] = calling_instance.player.ID
        	Messaging.sendMessage(24111, fields)
        elif fields["Unk1"] - 3 == 0:
        	if fields["Unk1"] - 3 in player_data["PushasedOffers"]:
        		pass
        	else:
        		player_data["PushasedOffers"].append(fields["Unk1"] - 3)
        		db_instance.updatePlayerData(player_data, calling_instance)
        		fields["Socket"] = calling_instance.client
        		fields["Command"] = {"ID": 203}
        		fields["PlayerID"] = calling_instance.player.ID
        		Messaging.sendMessage(24111, fields)
        else:
        	db_instance.updatePlayerData(player_data, calling_instance)
        	fields["Socket"] = calling_instance.client
        	fields["Command"] = {"ID": 203}
        	fields["PlayerID"] = calling_instance.player.ID
        	Messaging.sendMessage(24111, fields)


    def getCommandType(self):
        return 519