import pygame

pygame.init()

dimension = 19
tile_size = 32
info_panel_height = tile_size
WIDTH = dimension * tile_size
HEIGHT = dimension * tile_size
boss_amount = 1
coin_amount = 8
well_amount = 1
shop_amount = 1
maze_level = 1
player_gold = 0
player_atk = 0
player_dmg = 0
player_def = 0
player_max_hp = 0
outside = True
darkness = True
boss_defeated = False
quest_state = "not in progress"
mirror = False
power = 1
magic_shield = 0
freezing = False
speed = False
focus = "indicator"
frame = 0

tile_surf = pygame.image.load("pictures/tile.png")
wall_surf = pygame.image.load("pictures/wall.png")
entrance_surf = pygame.image.load("pictures/entrance.png")
exit_surf = pygame.image.load("pictures/exit.png")
grid_surf = pygame.image.load("pictures/grid.png")
player_surf = (pygame.image.load("pictures/player_0.png"), pygame.image.load("pictures/player_1.png"))
coin_surf = (pygame.image.load("pictures/coin_0.png"),
             pygame.image.load("pictures/coin_1.png"))
health_surf = (pygame.image.load("pictures/health_0.png"),
               pygame.image.load("pictures/health_1.png"))
well_surf = (pygame.image.load("pictures/well_0.png"),
             pygame.image.load("pictures/well_1.png"))
shop_surf = pygame.image.load("pictures/shop.png")
source_surf = (pygame.image.load("pictures/source_0.png"),
               pygame.image.load("pictures/source_1.png"))
black_surf = pygame.image.load("pictures/black.png")
mask_surf = (pygame.image.load("pictures/mask_0.png"),
             pygame.image.load("pictures/mask_1.png"),
             pygame.image.load("pictures/mask_2.png"))
maze_surf = pygame.image.load("pictures/maze.png")
rat_surf = pygame.image.load("pictures/rat.png")
pearl_surf = pygame.image.load("pictures/pearl.png")
log_surf = pygame.image.load("pictures/log.png")
note_surf = pygame.image.load("pictures/note.png")
egg_surf = pygame.image.load("pictures/egg.png")
pear_surf = pygame.image.load("pictures/pear.png")
arrow_surf = pygame.image.load("pictures/arrow.png")
hit_surf = pygame.image.load("pictures/hit.png")
block_surf = pygame.image.load("pictures/block.png")
fight_stage_surf = pygame.image.load("pictures/fight_stage.png")
gate_surf = pygame.image.load("pictures/gate.png")
finish_surf = pygame.image.load("pictures/finish.png")
magic_shield_surf = pygame.image.load("pictures/magic_shield.png")
shop_exit_surf = pygame.image.load("pictures/shop_exit.png")
info_panel_surf = pygame.image.load("pictures/info_panel.png")
gift_panel_surf = pygame.image.load("pictures/gift_panel.png")

monster1_surf = (pygame.image.load("pictures/monster1_0.png"), pygame.image.load("pictures/monster1_1.png"))
monster2_surf = (pygame.image.load("pictures/monster2_0.png"), pygame.image.load("pictures/monster2_1.png"))
monster3_surf = (pygame.image.load("pictures/monster3_0.png"), pygame.image.load("pictures/monster3_1.png"))
monster4_surf = (pygame.image.load("pictures/monster4_0.png"), pygame.image.load("pictures/monster4_1.png"))
monster5_surf = (pygame.image.load("pictures/monster5_0.png"), pygame.image.load("pictures/monster5_1.png"))
monster6_surf = (pygame.image.load("pictures/monster6_0.png"), pygame.image.load("pictures/monster6_1.png"))
monster7_surf = (pygame.image.load("pictures/monster7_0.png"), pygame.image.load("pictures/monster7_1.png"))
monster8_surf = (pygame.image.load("pictures/monster8_0.png"), pygame.image.load("pictures/monster8_1.png"))
monster9_surf = (pygame.image.load("pictures/monster9_0.png"), pygame.image.load("pictures/monster9_1.png"))
monster10_surf = (pygame.image.load("pictures/monster10_0.png"), pygame.image.load("pictures/monster10_1.png"))

boss1_surf = (pygame.image.load("pictures/boss1_0.png"), pygame.image.load("pictures/boss1_1.png"))
boss2_surf = (pygame.image.load("pictures/boss2_0.png"), pygame.image.load("pictures/boss2_1.png"))
boss3_surf = (pygame.image.load("pictures/boss3_0.png"), pygame.image.load("pictures/boss3_1.png"))
boss4_surf = (pygame.image.load("pictures/boss4_0.png"), pygame.image.load("pictures/boss4_1.png"))
boss5_surf = (pygame.image.load("pictures/boss5_0.png"), pygame.image.load("pictures/boss5_1.png"))
boss6_surf = (pygame.image.load("pictures/boss6_0.png"), pygame.image.load("pictures/boss6_1.png"))
boss7_surf = (pygame.image.load("pictures/boss7_0.png"), pygame.image.load("pictures/boss7_1.png"))
boss8_surf = (pygame.image.load("pictures/boss8_0.png"), pygame.image.load("pictures/boss8_1.png"))
boss9_surf = (pygame.image.load("pictures/boss9_0.png"), pygame.image.load("pictures/boss9_1.png"))
boss10_surf = (pygame.image.load("pictures/boss10_0.png"), pygame.image.load("pictures/boss10_1.png"))

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

rag_suit_surf = (pygame.image.load("pictures/rag_suit_0.png"),
                 pygame.image.load("pictures/rag_suit_1.png"))
linen_cloth_surf = (pygame.image.load("pictures/linen_cloth_0.png"),
                    pygame.image.load("pictures/linen_cloth_1.png"))
chain_shirt_surf = (pygame.image.load("pictures/chain_shirt_0.png"),
                    pygame.image.load("pictures/chain_shirt_1.png"))
steel_protector_surf = (pygame.image.load("pictures/steel_protector_0.png"),
                        pygame.image.load("pictures/steel_protector_1.png"))
shadow_cloak_surf = (pygame.image.load("pictures/shadow_cloak_0.png"),
                     pygame.image.load("pictures/shadow_cloak_1.png"))
venom_chainmail_surf = (pygame.image.load("pictures/venom_chainmail_0.png"),
                        pygame.image.load("pictures/venom_chainmail_1.png"))
flame_safeguard_surf = (pygame.image.load("pictures/flame_safeguard_0.png"),
                        pygame.image.load("pictures/flame_safeguard_1.png"))
golden_mail_surf = (pygame.image.load("pictures/golden_mail_0.png"),
                    pygame.image.load("pictures/golden_mail_1.png"))
holy_armor_surf = (pygame.image.load("pictures/holy_armor_0.png"),
                   pygame.image.load("pictures/holy_armor_1.png"))
crystal_plate_surf = (pygame.image.load("pictures/crystal_plate_0.png"),
                      pygame.image.load("pictures/crystal_plate_1.png"))
rune_armor_surf = (pygame.image.load("pictures/rune_armor_0.png"),
                   pygame.image.load("pictures/rune_armor_1.png"))

# item parameters: price, ATK, DMG, DEF, HP, surf
gears = (("Rusty Dagger", (0, 12, 75, 0, 0), rusty_dagger_surf),
         ("Oak Staff", (15, 18, 90, 0, 0), oak_staff_surf),
         ("Iron Mace", (45, 30, 120, 0, 0), iron_mace_surf),
         ("Steel Sword", (120, 45, 180, 0, 0), steel_sword_surf),
         ("Shadow Blade", (360, 69, 360, 0, 0), shadow_blade_surf),
         ("Flame Axe", (900, 90, 450, 0, 0), flame_axe_surf),
         ("Venom Dagger", (2040, 120, 675, 0, 0), venom_dagger_surf),
         ("Lightning Spear", (5280, 195, 840, 0, 0), lightning_spear_surf),
         ("Rune Staff", (9300, 225, 1135, 0, 0), rune_staff_surf),
         ("Holy Hammer", (25500, 300, 1800, 0, 0), holy_hammer_surf),
         ("Dragon Lance", (45000, 450, 2400, 0, 0), dragon_lance_surf),

         ("Rusty plate", (0, 0, 0, 15, 0), rusty_plate_surf),
         ("Wooden Buckler", (9, 0, 0, 21, 0), wooden_buckler_surf),
         ("Iron Shield", (36, 0, 0, 36, 0), iron_shield_surf),
         ("Steel Shield", (120, 0, 0, 54, 0), steel_shield_surf),
         ("Light Barrier", (1260, 0, 0, 75, 0), light_barrier_surf),
         ("Flame Aegis", (3300, 0, 0, 96, 0), flame_aegis_surf),
         ("Turtle Shield", (8700, 0, 0, 126, 0), turtle_shield_surf),
         ("Golden Barrier", (12300, 0, 0, 174, 0), golden_barrier_surf),
         ("Rune Engraved", (24900, 0, 0, 240, 0), rune_engraved_surf),
         ("Holy Aegis", (36000, 0, 0, 330, 0), holy_aegis_surf),
         ("Crystal Tower", (54000, 0, 0, 495, 0), crystal_tower_surf),

         ("Rag suit", (0, 0, 0, 0, 60), rag_suit_surf),
         ("Linen Cloth", (12, 0, 0, 0, 80), linen_cloth_surf),
         ("Chain Shirt", (30, 0, 0, 0, 120), chain_shirt_surf),
         ("Steel Protector", (150, 0, 0, 0, 190), steel_protector_surf),
         ("Shadow Cloak", (1140, 0, 0, 0, 275), shadow_cloak_surf),
         ("Flame Safeguard", (2970, 0, 0, 0, 410), flame_safeguard_surf),
         ("Venom Chainmail", (7620, 0, 0, 0, 575), venom_chainmail_surf),
         ("Golden Mail", (13560, 0, 0, 0, 825), golden_mail_surf),
         ("Rune Armor", (19500, 0, 0, 0, 1100), rune_armor_surf),
         ("Holy Armor", (27000, 0, 0, 0, 1600), holy_armor_surf),
         ("Crystal Plate", (43500, 0, 0, 0, 2500), crystal_plate_surf))

wears = [gears[0], gears[11], gears[22]]

player_hp = wears[2][1][4]

spell_bleeding_surf = pygame.image.load("pictures/spell_bleeding.png")
spell_healing_surf = pygame.image.load("pictures/spell_healing.png")
spell_mirror_surf = pygame.image.load("pictures/spell_mirror.png")
spell_magic_shield_surf = pygame.image.load("pictures/spell_magic_shield.png")
spell_freezing_surf = pygame.image.load("pictures/spell_freezing.png")
spell_power_surf = pygame.image.load("pictures/spell_double_damage.png")
spell_death_surf = pygame.image.load("pictures/spell_death.png")
spell_pickpocket_surf = pygame.image.load("pictures/spell_pickpocket.png")
spell_speed_surf = pygame.image.load("pictures/spell_haste.png")
spells_inventory = {"BLEEDING": 0, "HEALING": 0, "MIRROR": 0, "MAGIC SHIELD": 0, "FREEZING": 0,
                    "POWER": 0, "DEATH": 0, "THIEF": 0, "SPEED": 0}

quests = (("Too many rats are here.", "rat", rat_surf),
          ("My pearls are rolled away.", "pearl", pearl_surf),
          ("This rooms are so cold.", "log", log_surf),
          ("The wind blow my notes.", "note", note_surf),
          ("My hen lays egg anywhere.", "egg", egg_surf),
          ("I would eat some fruit.", "pear", pear_surf),
          ("My quiver has run out.", "arrow", arrow_surf))

pygame.mixer.music.load("sounds/menu.wav")
grid_open_sound = pygame.mixer.Sound("sounds/grid_open.wav")
grid_slam_sound = pygame.mixer.Sound("sounds/grid_slam.wav")
step0_sound = pygame.mixer.Sound("sounds/step0.wav")
step1_sound = pygame.mixer.Sound("sounds/step1.wav")
coin_sound = pygame.mixer.Sound("sounds/coin.wav")
chest_sound = pygame.mixer.Sound("sounds/chest.wav")
health_sound = pygame.mixer.Sound("sounds/health.wav")
monster_sound = pygame.mixer.Sound("sounds/monster.wav")
boss1_sound = pygame.mixer.Sound("sounds/boss1.wav")
boss2_sound = pygame.mixer.Sound("sounds/boss2.wav")
boss3_sound = pygame.mixer.Sound("sounds/boss3.wav")
boss4_sound = pygame.mixer.Sound("sounds/boss4.wav")
boss5_sound = pygame.mixer.Sound("sounds/boss5.wav")
boss_sounds = (boss1_sound, boss2_sound, boss3_sound, boss4_sound, boss5_sound)
shop_sound = pygame.mixer.Sound("sounds/shop.wav")
new_level_sound = pygame.mixer.Sound("sounds/new_level.wav")
rat_sound = pygame.mixer.Sound("sounds/rat.wav")
chop_sound = pygame.mixer.Sound("sounds/chop.wav")
ouch_sound = pygame.mixer.Sound("sounds/ouch.wav")
monster_ah_sound = pygame.mixer.Sound("sounds/monster_ah.wav")
player_ah_sound = pygame.mixer.Sound("sounds/player_ah.wav")
block_sound = pygame.mixer.Sound("sounds/block.wav")
hit_sound = pygame.mixer.Sound("sounds/hit.wav")
win_sound = pygame.mixer.Sound("sounds/fanfare.wav")
lose_sound = pygame.mixer.Sound("sounds/lose.wav")
transit_sound = pygame.mixer.Sound("sounds/transit.wav")
wake_up_sound = pygame.mixer.Sound("sounds/wake-up.wav")
freeze_spell_sound = pygame.mixer.Sound("sounds/freeze_spell.wav")
well_sound = pygame.mixer.Sound("sounds/well.wav")
bleeding_sound = pygame.mixer.Sound("sounds/bleeding.wav")
mirror_sound = pygame.mixer.Sound("sounds/mirror.wav")
magic_shield_sound = pygame.mixer.Sound("sounds/magic_shield.wav")
power_sound = pygame.mixer.Sound("sounds/power.wav")
death_sound = pygame.mixer.Sound("sounds/death.wav")
speed_sound = pygame.mixer.Sound("sounds/speed.wav")
tick_sound = pygame.mixer.Sound("sounds/tick.wav")
source_sound = pygame.mixer.Sound("sounds/source.wav")
quest_success_sound = pygame.mixer.Sound("sounds/quest_success.wav")

font = "fonts/Kingthings Petrock.ttf"
small_font = pygame.font.Font(font, 20)
normal_font = pygame.font.Font(font, 22)
big_font = pygame.font.Font(font, 25)
giant_font = pygame.font.Font(font, 32)

monster_surfs = (monster1_surf, monster2_surf, monster3_surf, monster4_surf, monster5_surf,
                 monster6_surf, monster7_surf, monster8_surf, monster9_surf, monster10_surf)

boss_surfs = (boss1_surf, boss2_surf, boss3_surf, boss4_surf, boss5_surf,
              boss6_surf, boss7_surf, boss8_surf, boss9_surf, boss10_surf)

prologue_text = ("In the ancient land of Eldoria,",
                 "where magic and legends intertwine,",
                 "a shadow of darkness has cast over",
                 "the once-vibrant realm.",
                 "A man known as Valen is destined",
                 "to confront an evil born from fear itself.",
                 "After a haunting vision, Valen ventures",
                 "into the Maze of Fear,",
                 "where he must transcend the boundaries",
                 "of courage, facing his inner demons",
                 "and the dreaded danger lurking within.",
                 " ",
                 "As Valen steps into the maze,",
                 "reality warps around him, and challenges",
                 "arise from his deeply rooted fears.",
                 "Guided by an ancient prophecy,",
                 "Valen navigates",
                 "the perilous path of the maze,",
                 "aiming to free Eldoria",
                 "from the rising tide of darkness",
                 "and restore balance.")

poem_text = ("In the Maze of Fears, a strong hero,",
             "Where lies his fate, he want to know.",
             "With bright courage, he step on his way,",
             "A world to save, where hope gone away.",
             "Monsters roar with eyes of fire.",
             "Hero keeps on, he never tire.",
             "Sword in hand and heart so true,",
             "In darkness deep, he must break through.",
             "In maze of dread he must be brave,",
             "To raise the world from the monster's grave.",
             "Fighting with strength, in the darkest night,",
             "He banish the monsters, set things right.",
             "With a heart of gold and spirit true,",
             "He fight for me, he fight for you.",
             "In the Maze of Fear, he find the way,",
             "Guiding us all to the light of day.",
             "Monsters fell to the hero's might,",
             "Their roars becomes silent in the night.",
             "In the annals of history, his tale will be",
             "A legend of courage, for eternity.")
