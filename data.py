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
player_gold = 200
player_hp = 10
additional_hp = 0
player_attack = 0
player_defense = 0
fill_items = True  # FOR TESTING
darkness = True  # FOR TESTING
boss_defeated = False
quest_state = "not in progress"
backpack = []
wears = ("Rusty Dagger", "Wooden Buckler", "Straw hat")

# item parameters: price, attack, defense, place (0: right hand, 1: left hand, 2: head)
gears = (("Rusty Dagger", (1, 1, 0, 0)),
         ("Oak Staff", (5, 2, 0, 0)),
         ("Iron Mace", (15, 2, 0, 0)),
         ("Steel Sword", (40, 2, 0, 0)),
         ("Shadow Blade", (120, 2, 0, 0)),
         ("Flame Axe", (300, 2, 0, 0)),
         ("Lightning Spear", (680, 2, 0, 0)),
         ("Crystal Wand", (1200, 2, 0, 0)),
         ("Venom Dagger", (1760, 2, 0, 0)),
         ("Rune Staff", (3100, 2, 0, 0)),
         ("Holy Hammer", (8500, 2, 0, 0)),
         ("Dragon Lance", (15000, 2, 0, 1)),
         ("Wooden Buckler", (3, 2, 0, 1)),
         ("Iron Shield", (12, 2, 0, 1)),
         ("Bull Shield", (60, 2, 0, 1)),
         ("Light Barrier", (420, 2, 0, 1)),
         ("Crystal Tower", (1100, 2, 0, 1)),
         ("Turtle Shield", (2900, 2, 0, 1)),
         ("Golden Barrier", (4100, 2, 0, 1)),
         ("Flame Aegis", (8300, 2, 0, 1)),
         ("Rune Engraved", (12000, 2, 0, 1)),
         ("Holy Aegis", (18000, 2, 0, 1)))

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