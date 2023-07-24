import pygame

pygame.init()

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
potion_amount = 5
treasure_amount = 1
shop_amount = 1
maze_level = 1
player_gold = 0
player_hp = 5
player_max_hp = 10
additional_hp = 0
player_attack = 0
player_defense = 0
fill_items = True  # FOR TESTING
darkness = False  # FOR TESTING
boss_defeated = False
quest_state = "not in progress"
outside = True


wall_surf = pygame.image.load("pictures/wall.png")
tile_surf = pygame.image.load("pictures/tile.png")
entrance_surf = pygame.image.load("pictures/entrance.png")
exit_surf = pygame.image.load("pictures/exit.png")
grid_surf = pygame.image.load("pictures/grid.png")
player_surf = pygame.image.load("pictures/player.png")
monster_surf = pygame.image.load("pictures/monster.png")
boss_surf = pygame.image.load("pictures/boss.png")
coin_surf = pygame.image.load("pictures/coin.png")
health_surf = pygame.image.load("pictures/health.png")
chest_surf = pygame.image.load("pictures/chest.png")
shop_surf = pygame.image.load("pictures/shop.png")
black_surf = pygame.image.load("pictures/black.png")
mask_surf = pygame.image.load("pictures/mask.png")
maze_surf = pygame.image.load("pictures/maze.png")
rat_surf = pygame.image.load("pictures/rat.png")
pearl_surf = pygame.image.load("pictures/pearl.png")
log_surf = pygame.image.load("pictures/log.png")

rusty_dagger_surf = pygame.image.load("pictures/rusty_dagger.png")
oak_staff_surf = pygame.image.load("pictures/oak_staff.png")
iron_mace_surf = pygame.image.load("pictures/iron_mace.png")
steel_sword_surf = pygame.image.load("pictures/steel_sword.png")
shadow_blade_surf = pygame.image.load("pictures/shadow_blade.png")
flame_axe_surf = pygame.image.load("pictures/flame_axe.png")
lightning_spear_surf = pygame.image.load("pictures/lightning_spear.png")
venom_dagger_surf = pygame.image.load("pictures/venom_dagger.png")
rune_staff_surf = pygame.image.load("pictures/rune_staff.png")
holy_hammer_surf = pygame.image.load("pictures/holy_hammer.png")
dragon_lance_surf = pygame.image.load("pictures/dragon_lance.png")

rusty_plate_surf = pygame.image.load("pictures/rusty_plate.png")
wooden_buckler_surf = pygame.image.load("pictures/wooden_buckler.png")
iron_shield_surf = pygame.image.load("pictures/iron_shield.png")
bull_shield_surf = pygame.image.load("pictures/bull_shield.png")
light_barrier_surf = pygame.image.load("pictures/light_barrier.png")
crystal_tower_surf = pygame.image.load("pictures/crystal_tower.png")
turtle_shield_surf = pygame.image.load("pictures/turtle_shield.png")
golden_barrier_surf = pygame.image.load("pictures/golden_barrier.png")
flame_aegis_surf = pygame.image.load("pictures/flame_aegis.png")
rune_engraved_surf = pygame.image.load("pictures/rune_engraved.png")
holy_aegis_surf = pygame.image.load("pictures/holy_aegis.png")

rag_suit_surf = pygame.image.load("pictures/rag_suit.png")
linen_cloth_surf = pygame.image.load("pictures/linen_cloth.png")

# item parameters: price, attack, defense, place (0: right hand, 1: left hand, 2: head), surf
gears = (("Rusty Dagger", (0, 0, 0, 0), rusty_dagger_surf),
         ("Oak Staff", (5, 2, 0, 0), oak_staff_surf),
         ("Iron Mace", (15, 2, 0, 0), iron_mace_surf),
         ("Steel Sword", (40, 2, 0, 0), steel_sword_surf),
         ("Shadow Blade", (120, 2, 0, 0), shadow_blade_surf),
         ("Flame Axe", (300, 2, 0, 0), flame_axe_surf),
         ("Lightning Spear", (680, 2, 0, 0), lightning_spear_surf),
         ("Venom Dagger", (1760, 2, 0, 0), venom_dagger_surf),
         ("Rune Staff", (3100, 2, 0, 0), rune_staff_surf),
         ("Holy Hammer", (8500, 2, 0, 0), holy_hammer_surf),
         ("Dragon Lance", (15000, 2, 0, 1), dragon_lance_surf),
         ("Rusty plate", (0, 0, 0, 0), rusty_plate_surf),
         ("Wooden Buckler", (3, 2, 0, 1), wooden_buckler_surf),
         ("Iron Shield", (12, 2, 0, 1), iron_shield_surf),
         ("Bull Shield", (60, 2, 0, 1), bull_shield_surf),
         ("Light Barrier", (420, 2, 0, 1), light_barrier_surf),
         ("Crystal Tower", (1100, 2, 0, 1), crystal_tower_surf),
         ("Turtle Shield", (2900, 2, 0, 1), turtle_shield_surf),
         ("Golden Barrier", (4100, 2, 0, 1), golden_barrier_surf),
         ("Flame Aegis", (8300, 2, 0, 1), flame_aegis_surf),
         ("Rune Engraved", (12000, 2, 0, 1), rune_engraved_surf),
         ("Holy Aegis", (18000, 2, 0, 1), holy_aegis_surf),
         ("Rag suit", (0, 0, 0, 2), rag_suit_surf),
         ("Linen Cloth", (4, 2, 0, 2), linen_cloth_surf),
         ("Linen Cloth", (4, 2, 0, 2), linen_cloth_surf))

wears = [gears[0],
         gears[11],
         gears[22]]

quests = (("Too many rats are here.", "rat", rat_surf),
          ("My wife's pearls rolled apart.", "pearl", pearl_surf),
          ("This rooms are so cold.", "log", log_surf))

pygame.mixer.music.load("sounds/menu.wav")
grid_open_sound = pygame.mixer.Sound("sounds/grid_open.wav")
grid_slam_sound = pygame.mixer.Sound("sounds/grid_slam.wav")
steps_sound = pygame.mixer.Sound("sounds/steps.wav")
coin_sound = pygame.mixer.Sound("sounds/coin.wav")
chest_sound = pygame.mixer.Sound("sounds/chest.wav")
health_sound = pygame.mixer.Sound("sounds/health.wav")
monster_sound = pygame.mixer.Sound("sounds/monster.wav")
boss_sound = pygame.mixer.Sound("sounds/boss.wav")
shop_sound = pygame.mixer.Sound("sounds/shop.wav")
new_level_sound = pygame.mixer.Sound("sounds/new_level.wav")
rat_sound = pygame.mixer.Sound("sounds/rat.wav")
chop_sound = pygame.mixer.Sound("sounds/chop.wav")

normal_font = pygame.font.Font(None, 23)
highlighted_font = pygame.font.Font(None, 26)
menu_font = pygame.font.Font(None, 40)
