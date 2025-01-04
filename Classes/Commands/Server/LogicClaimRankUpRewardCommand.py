from Classes.ByteStream import ByteStream
#from Classes.Logic.LogicBoxData import LogicBoxData
from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
import json
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
    56: {'CardID': 448, 'Skins': [0, 0], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    57: {'CardID': 466, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    58: {'CardID': 474, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
}


class LogicClaimRankUpRewardCommand(LogicServerCommand):
    
    def __init__(self, commandData):
        super().__init__(commandData)

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["RewardID"] = calling_instance.readVInt()
        fields["Unk"] = calling_instance.readVInt()
        fields["BPSeason"] = calling_instance.readVInt()
        fields["LVL"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def encode(self, fields):
    	pass

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        if fields["LVL"] == 70:
        	a = random.randint(0, 654)
        	b = random.randint(0, 654)
        	c = random.randint(0, 654)
        	player_data["OwnedPins"].append(a)
        	player_data["OwnedPins"].append(b)
        	player_data["OwnedPins"].append(c)
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {
        	'Type': 0,
        	'Items': []
        	}
        	item = {'Amount': 1, 'DataRef': [52, a], 'RewardID': 11}
        	box['Type'] = 100
        	box['Items'].append(item)
        	item = {'Amount': 1, 'DataRef': [52, b], 'RewardID': 11}
        	box['Items'].append(item)
        	item = {'Amount': 1, 'DataRef': [52, c], 'RewardID': 11}
        	box['Items'].append(item)
        	player_data["delivery_items"]['Boxes'].append(box)
        if fields["RewardID"] == 10 and fields["LVL"] == 0 or fields["LVL"] == 3 or fields["LVL"] == 5 or fields["LVL"] == 7 or fields["LVL"] == 9 or fields["LVL"] == 11 or fields["LVL"] == 13 or fields["LVL"] == 15 or fields["LVL"] == 17 or fields["LVL"] == 19 or fields["LVL"] == 23 or fields["LVL"] == 25 or fields["LVL"] == 27 or fields["LVL"] == 29 or fields["LVL"] == 31 or fields["LVL"] == 35 or fields["LVL"] == 37 or fields["LVL"] == 47 or fields["LVL"] == 49 or fields["LVL"] == 53 or fields["LVL"] == 57 or fields["LVL"] == 59 or fields["LVL"] == 61 or fields["LVL"] == 66:
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
        	brawlerID1= random.choice(brawlers)
        	brawlerID2 = random.choice(brawlers)
        	brawlerID3 = random.choice(brawlers)
        	ppbr = random.randint(20, 64)
        	while brawlerID2 == brawlerID1 or brawlerID2 == brawlerID3:
        		brawlerID2 = random.choice(brawlers)
        	while brawlerID3 == brawlerID1 or brawlerID3 == brawlerID2:
        		brawlerID3 = random.choice(brawlers)
        	brawlerID6 = random.randint(0, 58)
        	while brawlerID6 == 33 or brawlerID6 == 55 or brawlerID6 in brawlers:
        		brawlerID6 = random.randint(0, 58)
        	gold = random.randint(21, 134)
        	if random.randint(0, 10) == 7:
        		gems = random.randint(30, 90)
        	elif random.randint(0, 5) == 2:
        		gems = random.randint(20, 50)
        	else:
        		gems = random.randint(5, 30)
        	box['Type'] = 12
        	item = {'Amount': gold, 'DataRef': [0, 0], 'RewardID': 7}
        	box['Items'].append(item)
        	item = {'Amount': pp1, 'DataRef': [16, brawlerID1], 'RewardID': 6}
        	box['Items'].append(item)
        	item = {'Amount': pp2, 'DataRef': [16, brawlerID2], 'RewardID': 6}
        	box['Items'].append(item)
        	item = {'Amount': pp3, 'DataRef': [16, brawlerID3], 'RewardID': 6}
        	box['Items'].append(item)
        	for i,v in player_data["OwnedBrawlers"].items():
        			if v["CardID"] == OwnedBrawlersLatest[brawlerID1]["CardID"]:
        				v["PowerPoints"] += pp1
        for i,v in player_data["OwnedBrawlers"].items():
        			if v["CardID"] == OwnedBrawlersLatest[brawlerID2]["CardID"]:
        				v["PowerPoints"] += pp2
        for i,v in player_data["OwnedBrawlers"].items():
        			if v["CardID"] == OwnedBrawlersLatest[brawlerID3]["CardID"]:
        				v["PowerPoints"] += pp3
        if random.randint(0, 10) == 3:
             item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
             box['Items'].append(item)
             player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
        else:
             if random.randint(0, 6) == 2:
             	item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
             	box['Items'].append(item)
        if random.randint(0, 3) == 2:
        	       item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
        	       box['Items'].append(item)
        player_data["Gems"] += gems
        player_data["delivery_items"]['Boxes'].append(box)

        if fields["RewardID"] == 10 and fields["LVL"] == 10 or fields["LVL"] == 20 or fields["LVL"] == 30 or fields["LVL"] == 40 or fields["LVL"] == 45 or fields["LVL"] == 51 or fields["LVL"] == 55 or fields["LVL"] == 60 or fields["LVL"] == 65 or fields["LVL"] == 68:
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
            	if v["CardID"] == OwnedBrawlersLatest[brawlerID1]["CardID"]:
            		v["PowerPoints"] += pp1
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[brawlerID2]["CardID"]:
            		v["PowerPoints"] += pp2
            for i,v in player_data["OwnedBrawlers"].items():
            	if v["CardID"] == OwnedBrawlersLatest[brawlerID3]["CardID"]:
            		v["PowerPoints"] += pp3
            if len(brawlers) >= 4:
            	item = {'Amount': pp4, 'DataRef': [16, brawlerID4], 'RewardID': 6}
            	box['Items'].append(item)
            	for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[brawlerID4]["CardID"]:
            			v["PowerPoints"] += pp4
            if len(brawlers) >= 5:
            	item = {'Amount': pp5, 'DataRef': [16, brawlerID5], 'RewardID': 6}
            	box['Items'].append(item)
            	for i,v in player_data["OwnedBrawlers"].items():
            		if v["CardID"] == OwnedBrawlersLatest[brawlerID5]["CardID"]:
            			v["PowerPoints"] += pp5
            if random.randint(0, 10) == 3:
                item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
                box['Items'].append(item)
                player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
            else:
             	if random.randint(0, 6) == 2:
             		item = {'Amount': ppbr, 'DataRef': [0, 0], 'RewardID': 19}
             		box['Items'].append(item)
            if random.randint(0, 3) == 2:
                 item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
                 box['Items'].append(item)
                 player_data["Gems"] += gems
            player_data["Coins"] += gold
            player_data["delivery_items"]['Boxes'].append(box)

        if fields["RewardID"] == 6 and fields["LVL"] == 0 or fields["LVL"] == 2 or fields["LVL"] == 5 or fields["LVL"] == 13:
        	player_data["delivery_items"] = {
                'Boxes': []
            }
        	box = {
        	'Type': 0,
        	'Items': []
        	}
        	brawlers= list(player_data["OwnedBrawlers"].keys())
        	pp1= random.randint(9,69)
        	pp2 = random.randint(9,69)
        	pp3 = random.randint(9,69)
        	ppbr = random.randint(10, 32)
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
        	box['Type'] = 10
        	if random.randint(0, 15) == 3:
        	    item = {'Amount': 1, 'DataRef': [16, brawlerID6], 'RewardID': 1}
        	    box['Items'].append(item)
        	    player_data["OwnedBrawlers"][brawlerID6] = OwnedBrawlersLatest[brawlerID6]
        	elif random.randint(0, 12) == 2:
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
        	if random.randint(0, 3) == 2:
        	   		    item = {'Amount': gems, 'DataRef': [0, 0], 'RewardID': 8}
        	   		    box['Items'].append(item)
        	   		    player_data["Gems"] += gems
        	player_data["Coins"] += gold
        	player_data["delivery_items"]['Boxes'].append(box)


        if fields["RewardID"] == 6:
        	player_data["TrophyRoadTier"] += 1
        
        db_instance.updatePlayerData(player_data, calling_instance)
        fields["Socket"] = calling_instance.client
        fields["Command"] = {"ID": 203}
        fields["PlayerID"] = calling_instance.player.ID
        Messaging.sendMessage(24111, fields)


    def getCommandType(self):
        return 517


