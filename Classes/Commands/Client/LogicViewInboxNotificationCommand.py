import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
from Classes.ByteStream import ByteStream
import random
from Classes.Packets.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage


class LogicViewInboxNotificationCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        pass

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["NotificationIndex"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data["delivery_items"] = {
        'Boxes': []
        }
        box = {
        'Type': 0,
        'Items': []
        }
        notification = player_data["NotificationFactory"]
        for x in notification:
        	if x["Type"] == 81:
        		pass
        	if x["Type"] == 72 or x["Type"] == 94:
        		if x["DataRef"][0] == 29:
        			RewardID = 9
        		if x["DataRef"][0] == 28 or x["DataRef"][0] == 52:
        			RewardID = 11
        		item = {'Amount': 1, 'DataRef': x["DataRef"], 'RewardID': RewardID}
        		box['Type'] = 100
        		box['Items'].append(item)
        		player_data["delivery_items"]['Boxes'].append(box)


    def getCommandType(self):
        return 528