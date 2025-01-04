import json

class StaticData:
    ShopData = None
    EventsData = None
    QuestsData = None

    def Preload():
        StaticData.ShopData = json.loads(open("Static/Shop.json", 'r').read())
        StaticData.EventsData = json.loads(open("Static/Events.json", 'r').read())
        StaticData.QuestsData = json.loads(open("Static/Quests.json", 'r').read())
