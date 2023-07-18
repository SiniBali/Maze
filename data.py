dimension = 19  # must be odd!
tile_size = 32
info_panel_height = tile_size
WIDTH = dimension * tile_size
HEIGHT = dimension * tile_size
BG_COLOR = "grey30"
FONT_COLOR = "white"
monster_amount = 5
boss_amount = 1
coin_amount = 12
health_amount = 5
treasure_amount = 1
shop_amount = 1
maze_level = 1
player_gold = 0
player_hp = 10
additional_hp = 0
player_attack = 0
player_defense = 0
fill_items = True  # FOR TESTING
darkness = True  # FOR TESTING
boss_defeated = False
quest_state = "not in progress"
backpack = []
wears = {"hand": "Rusty Dagger"}
# wears = {"head": "Straw hat", "hand": "Rusty Dagger", "body": "Linen shirt"}
# item parameters: price, attack, defense, HP, place
gears = {"Rusty Dagger": (1, 1, 0, 0, "hand"),
         "Oak Staff": (5, 2, 0, 0, "hand"),
         "Iron Mace": (15, 2, 0, 0, "hand"),
         "Steel Sword": (40, 2, 0, 0, "hand"),
         "Shadow Blade": (120, 2, 0, 0, "hand"),
         "Flame Axe": (300, 2, 0, 0, "hand"),
         "Lightning Spear": (680, 2, 0, 0, "hand"),
         "Crystal Wand": (1200, 2, 0, 0, "hand"),
         "Venom Dagger": (1760, 2, 0, 0, "hand"),
         "Rune Staff": (3100, 2, 0, 0, "hand"),
         "Holy Hammer": (8500, 2, 0, 0, "hand"),
         "Dragon Lance": (15000, 2, 0, 0, "hand")}

quests = ("Too many rats are here. Kill 10 of them.",
          "I hid a treasure near. Go check the tiles.",
          "I love nature. Plant trees on the corners.",
          "The gates are squeaks a lot. Please oil them.",
          "There is a chest somewhere. Please bring it to me.",
          "I lost my cat. Mossy like to climb up to trees",
          "This rooms are so cold. Please bring me 4 logs")

"""{"Straw hat": (0, 0, 0, 0, "head"),
         "Leather cap": (3, 0, 1, 0, "head"),
         "Rusty Dagger": (1, 1, 0, 0, "hand"),
         "Oak Staff": (5, 2, 0, 0, "hand"),
         "Iron Mace": (15, 2, 0, 0, "hand"),
         "Steel Sword": (40, 2, 0, 0, "hand"),
         "Shadow Blade": (120, 2, 0, 0, "hand"),
         "Flame Axe": (300, 2, 0, 0, "hand"),
         "Lightning Spear": (680, 2, 0, 0, "hand"),
         "Crystal Wand": (1200, 2, 0, 0, "hand"),
         "Venom Dagger": (1760, 2, 0, 0, "hand"),
         "Rune Staff": (3100, 2, 0, 0, "hand"),
         "Holy Hammer": (8500, 2, 0, 0, "hand"),
         "Dragon Lance": (15000, 2, 0, 0, "hand"),
         "Linen shirt": (0, 0, 0, 0, "chest"),
         "Leather armor": (6, 0, 1, 1, "chest")}"""