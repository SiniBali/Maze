import pygame

pygame.init()

dimension = 19  # must be odd!
tile_size = 32
info_panel_height = tile_size
WIDTH = dimension * tile_size
HEIGHT = dimension * tile_size
monster_amount = 7
boss_amount = 1
coin_amount = 6
potion_amount = 4
well_amount = 1
shop_amount = 1
maze_level = 1
player_gold = 0
player_hp = 10
player_max_hp = 0
player_attack = 0
player_defense = 0
darkness = True
boss_defeated = False
quest_state = "not in progress"
outside = True

wall_surf = pygame.image.load("pictures/wall.png")
tile_surf = pygame.image.load("pictures/tile.png")
entrance_surf = pygame.image.load("pictures/entrance.png")
exit_surf = pygame.image.load("pictures/exit.png")
grid_surf = pygame.image.load("pictures/grid.png")
player_surf = pygame.image.load("pictures/player.png")
coin_surf = pygame.image.load("pictures/coin.png")
health_surf = pygame.image.load("pictures/health.png")
well_surf = pygame.image.load("pictures/well.png")
shop_surf = pygame.image.load("pictures/shop.png")
black_surf = pygame.image.load("pictures/black.png")
mask_surf = pygame.image.load("pictures/mask.png")
maze_surf = pygame.image.load("pictures/maze.png")
rat_surf = pygame.image.load("pictures/rat.png")
pearl_surf = pygame.image.load("pictures/pearl.png")
log_surf = pygame.image.load("pictures/log.png")
note_surf = pygame.image.load("pictures/note.png")
egg_surf = pygame.image.load("pictures/egg.png")
hit_surf = pygame.image.load("pictures/hit.png")
block_surf = pygame.image.load("pictures/block.png")
fight_stage_surf = pygame.image.load("pictures/fight_stage.png")

monster1_surf = pygame.image.load("pictures/monster1.png")
monster2_surf = pygame.image.load("pictures/monster2.png")
monster3_surf = pygame.image.load("pictures/monster3.png")
monster4_surf = pygame.image.load("pictures/monster4.png")
monster5_surf = pygame.image.load("pictures/monster5.png")
monster6_surf = pygame.image.load("pictures/monster5.png")
monster7_surf = pygame.image.load("pictures/monster5.png")
monster8_surf = pygame.image.load("pictures/monster5.png")
monster9_surf = pygame.image.load("pictures/monster5.png")
monster10_surf = pygame.image.load("pictures/monster5.png")

boss1_surf = pygame.image.load("pictures/boss1.png")
boss2_surf = pygame.image.load("pictures/boss2.png")
boss3_surf = pygame.image.load("pictures/boss3.png")
boss4_surf = pygame.image.load("pictures/boss4.png")
boss5_surf = pygame.image.load("pictures/boss5.png")
boss6_surf = pygame.image.load("pictures/boss5.png")
boss7_surf = pygame.image.load("pictures/boss5.png")
boss8_surf = pygame.image.load("pictures/boss5.png")
boss9_surf = pygame.image.load("pictures/boss5.png")
boss10_surf = pygame.image.load("pictures/boss5.png")

rusty_dagger_surf = pygame.image.load("pictures/rusty_dagger.png")
oak_staff_surf = pygame.image.load("pictures/oak_staff.png")
iron_mace_surf = pygame.image.load("pictures/iron_mace.png")
steel_sword_surf = pygame.image.load("pictures/steel_sword.png")
shadow_blade_surf = pygame.image.load("pictures/shadow_blade.png")
flame_axe_surf = pygame.image.load("pictures/flame_axe.png")
venom_dagger_surf = pygame.image.load("pictures/venom_dagger.png")
lightning_spear_surf = pygame.image.load("pictures/lightning_spear.png")
rune_staff_surf = pygame.image.load("pictures/rune_staff.png")
holy_hammer_surf = pygame.image.load("pictures/holy_hammer.png")
dragon_lance_surf = pygame.image.load("pictures/dragon_lance.png")

rusty_plate_surf = pygame.image.load("pictures/rusty_plate.png")
wooden_buckler_surf = pygame.image.load("pictures/wooden_buckler.png")
iron_shield_surf = pygame.image.load("pictures/iron_shield.png")
steel_shield_surf = pygame.image.load("pictures/steel_shield.png")
light_barrier_surf = pygame.image.load("pictures/light_barrier.png")
flame_aegis_surf = pygame.image.load("pictures/flame_aegis.png")
turtle_shield_surf = pygame.image.load("pictures/turtle_shield.png")
golden_barrier_surf = pygame.image.load("pictures/golden_barrier.png")
rune_engraved_surf = pygame.image.load("pictures/rune_engraved.png")
holy_aegis_surf = pygame.image.load("pictures/holy_aegis.png")
crystal_tower_surf = pygame.image.load("pictures/crystal_tower.png")

rag_suit_surf = pygame.image.load("pictures/rag_suit.png")
linen_cloth_surf = pygame.image.load("pictures/linen_cloth.png")
chain_shirt_surf = pygame.image.load("pictures/chain_shirt.png")
steel_protector_surf = pygame.image.load("pictures/steel_protector.png")
shadow_cloak_surf = pygame.image.load("pictures/shadow_cloak.png")
venom_chainmail_surf = pygame.image.load("pictures/venom_chainmail.png")
flame_safeguard_surf = pygame.image.load("pictures/flame_safeguard.png")
golden_mail_surf = pygame.image.load("pictures/golden_mail.png")
holy_armor_surf = pygame.image.load("pictures/holy_armor.png")
crystal_plate_surf = pygame.image.load("pictures/crystal_plate.png")
rune_armor_surf = pygame.image.load("pictures/rune_armor.png")

# item parameters: price, attack, defense, place (0: right hand, 1: left hand, 2: head), surf
gears = (("Rusty Dagger", (0, 10, 0, 0), rusty_dagger_surf),
         ("Oak Staff", (5, 14, 0, 0), oak_staff_surf),
         ("Iron Mace", (15, 18, 0, 0), iron_mace_surf),
         ("Steel Sword", (40, 2, 0, 0), steel_sword_surf),
         ("Shadow Blade", (120, 2, 0, 0), shadow_blade_surf),
         ("Flame Axe", (300, 2, 0, 0), flame_axe_surf),
         ("Venom Dagger", (680, 2, 0, 0), venom_dagger_surf),
         ("Lightning Spear", (1760, 2, 0, 0), lightning_spear_surf),
         ("Rune Staff", (3100, 2, 0, 0), rune_staff_surf),
         ("Holy Hammer", (8500, 2, 0, 0), holy_hammer_surf),
         ("Dragon Lance", (15000, 2, 0, 0), dragon_lance_surf),
         ("Rusty plate", (0, 0, 6, 0), rusty_plate_surf),
         ("Wooden Buckler", (3, 0, 10, 0), wooden_buckler_surf),
         ("Iron Shield", (12, 0, 14, 0), iron_shield_surf),
         ("Steel Shield", (60, 2, 0, 0), steel_shield_surf),
         ("Light Barrier", (420, 2, 0, 0), light_barrier_surf),
         ("Flame Aegis", (1100, 2, 0, 0), flame_aegis_surf),
         ("Turtle Shield", (2900, 2, 0, 0), turtle_shield_surf),
         ("Golden Barrier", (4100, 2, 0, 0), golden_barrier_surf),
         ("Rune Engraved", (8300, 2, 0, 0), rune_engraved_surf),
         ("Holy Aegis", (12000, 2, 0, 0), holy_aegis_surf),
         ("Crystal Tower", (18000, 2, 0, 0), crystal_tower_surf),
         ("Rag suit", (0, 0, 0, 10), rag_suit_surf),
         ("Linen Cloth", (4, 0, 0, 18), linen_cloth_surf),
         ("Chain Shirt", (4, 0, 0, 25), chain_shirt_surf),
         ("Steel Protector", (4, 0, 0, 18), steel_protector_surf),
         ("Shadow Cloak", (4, 0, 0, 18), shadow_cloak_surf),
         ("Flame Safeguard", (4, 0, 0, 18), flame_safeguard_surf),
         ("Venom Chainmail", (4, 0, 0, 18), venom_chainmail_surf),
         ("Golden Mail", (4, 0, 0, 18), golden_mail_surf),
         ("Rune Armor", (4, 0, 0, 18), rune_armor_surf),
         ("Holy Armor", (4, 0, 0, 18), holy_armor_surf),
         ("Crystal Plate", (4, 0, 0, 18), crystal_plate_surf))

wears = [gears[0],
         gears[11],
         gears[22]]

quests = (("Too many rats are here.", "rat", rat_surf),
          ("My pearls are rolled away.", "pearl", pearl_surf),
          ("This rooms are so cold.", "log", log_surf),
          ("The wind blow my notes.", "note", note_surf),
          ("My hen lays egg anywhere.", "egg", egg_surf))

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
ouch_sound = pygame.mixer.Sound("sounds/ouch.wav")

normal_font = pygame.font.Font(None, 23)
highlighted_font = pygame.font.Font(None, 26)
menu_font = pygame.font.Font(None, 40)

monster_values = ((6, 8, 10, monster1_surf),  # atk, def, hp, surf
                  (9, 10, 20, monster2_surf),
                  [6, 6, 2, monster3_surf],
                  [6, 6, 2, monster4_surf],
                  [6, 6, 2, monster5_surf],
                  [6, 6, 2, monster6_surf],
                  [6, 6, 2, monster7_surf],
                  [6, 6, 2, monster8_surf],
                  [6, 6, 2, monster9_surf],
                  [6, 6, 2, monster10_surf])

boss_values = ((14, 10, 25, boss1_surf),  # atk, def, hp, surf
               (18, 14, 35, boss2_surf),
               (14, 10, 25, boss3_surf),
               (14, 10, 25, boss4_surf),
               (14, 10, 25, boss5_surf),
               (14, 10, 25, boss6_surf),
               (14, 10, 25, boss7_surf),
               (14, 10, 25, boss8_surf),
               (14, 10, 25, boss9_surf),
               (14, 10, 25, boss10_surf))
