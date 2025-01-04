import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler

OwnedBrawlersLatest = {
    0: {'CardID': 0, 'Skins': [29, 52, 122, 158, 194, 195, 319, 320, 321, 358], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    1: {'CardID': 4, 'Skins': [2, 103, 69, 134, 216, 302, 322, 323, 324, 325, 329, 330, 376], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    2: {'CardID': 8, 'Skins': [25, 64, 102, 177, 217, 218, 261, 391, 466], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    3: {'CardID': 12, 'Skins': [5, 58, 72, 91, 200, 241, 398, 399], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    4: {'CardID': 16, 'Skins': [26, 68, 129, 170, 222, 223, 395, 463], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    5: {'CardID': 20, 'Skins': [11, 96, 207, 262, 300, 301, 441], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    6: {'CardID': 24, 'Skins': [27, 59, 90, 92, 116, 219, 220, 356, 432], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    7: {'CardID': 28, 'Skins': [44, 47, 123, 161, 173, 252, 253, 393], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    8: {'CardID': 32, 'Skins': [15, 435, 60, 79, 147, 296, 297, 346], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    9: {'CardID': 36, 'Skins': [56, 57, 97, 159, 235, 275, 313, 314, 315, 396, 428, 429, 455], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    10: {'CardID': 40, 'Skins': [28, 30, 128, 182, 186, 212, 316, 317, 318, 353, 359, 434, 436], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    11: {'CardID': 44, 'Skins': [50, 63, 75, 172, 227, 229, 226, 228, 310], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    12: {'CardID': 48, 'Skins': [20, 49, 95, 100, 101, 247, 248, 388], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    13: {'CardID': 52, 'Skins': [71, 139, 213, 341, 404, 405], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    14: {'CardID': 56, 'Skins': [94, 98, 99, 162, 215, 244, 362, 363, 438, 467], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    15: {'CardID': 60, 'Skins': [108, 120, 146, 196, 197, 233, 380], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    16: {'CardID': 64, 'Skins': [178, 354, 409, 410], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    17: {'CardID': 68, 'Skins': [111, 144, 258, 259, 281], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    18: {'CardID': 72, 'Skins': [70, 157, 249, 250, 263, 350], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    19: {'CardID': 95, 'Skins': [61, 88, 164, 273, 446, 447], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    20: {'CardID': 100, 'Skins': [45, 125, 224, 225, 243], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    21: {'CardID': 105, 'Skins': [117, 171, 303, 304, 387], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    22: {'CardID': 110, 'Skins': [189, 242, 245, 246], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    23: {'CardID': 115, 'Skins': [110, 126, 130, 198, 199, 311], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    24: {'CardID': 120, 'Skins': [214, 308, 439, 448, 449, 472], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    25: {'CardID': 125, 'Skins': [93, 104, 131, 133, 266, 307, 422, 423], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    26: {'CardID': 130, 'Skins': [145, 221, 272, 344, 420, 421], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    27: {'CardID': 177, 'Skins': [109, 142, 282, 400, 401, 407], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    28: {'CardID': 182, 'Skins': [118, 209, 286, 370, 371], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    29: {'CardID': 188, 'Skins': [138, 187, 283, 284, 289, 364, 365], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    30: {'CardID': 194, 'Skins': [166, 184, 185, 208], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    31: {'CardID': 200, 'Skins': [151, 331, 332, 413, 468], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    32: {'CardID': 206, 'Skins': [136, 201, 231, 309, 402, 403], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    34: {'CardID': 218, 'Skins': [175, 188, 306, 437, 442, 443], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    35: {'CardID': 224, 'Skins': [179, 240, 366, 367, 386], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    36: {'CardID': 230, 'Skins': [193, 232, 368, 369], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    37: {'CardID': 236, 'Skins': [176, 210, 378, 381, 477, 481, 482], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    38: {'CardID': 279, 'Skins': [202, 291, 417, 485, 486], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    39: {'CardID': 296, 'Skins': [211, 269, 389, 426, 427], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    40: {'CardID': 303, 'Skins': [279, 424, 425], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    41: {'CardID': 320, 'Skins': [236, 265, 305, 444, 445], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    42: {'CardID': 327, 'Skins': [357], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    43: {'CardID': 334, 'Skins': [462, 280, 433], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    44: {'CardID': 341, 'Skins': [267, 285, 479, 480], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    45: {'CardID': 358, 'Skins': [276, 345, 418], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    46: {'CardID': 365, 'Skins': [293, 478], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    47: {'CardID': 372, 'Skins': [390, 416], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    48: {'CardID': 379, 'Skins': [471], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    49: {'CardID': 386, 'Skins': [342, 384, 483, 484], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    50: {'CardID': 393, 'Skins': [451], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    51: {'CardID': 410, 'Skins': [379], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    52: {'CardID': 417, 'Skins': [464], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    53: {'CardID': 427, 'Skins': [431], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    54: {'CardID': 434, 'Skins': [455], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    56: {'CardID': 448, 'Skins': [473], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
    57: {'CardID': 466, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    58: {'CardID': 474, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}
}


class LogicSelectSkinCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        pass

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["SkinID"] = calling_instance.readDataReference()
        fields["Unk"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data["SelectedSkins"].append(fields["SkinID"][1])
        db_instance.updatePlayerData(player_data, calling_instance)

    def getCommandType(self):
        return 506