from maze_generator import *
from data import *
from media_load import *
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + info_panel_height))
pygame.display.set_caption("Maze of fear")
clock = pygame.time.Clock()


def draw_map():
    if not darkness:
        r1, r2, r3, r4 = 0, dimension, 0, dimension
    else:
        for x in range(dimension):
            for y in range(dimension):
                place = (x * tile_size, y * tile_size + info_panel_height)
                screen.blit(black_surf, place)
        if player_position[0] == 0:
            h = 0
        elif player_position[0] == 1:
            h = -1
        elif player_position[0] == 2:
            h = -2
        elif player_position[0] == 3:
            h = -3
        else:
            h = -4
        if player_position[0] == dimension - 1:
            i = 0
        elif player_position[0] == dimension - 2:
            i = 1
        elif player_position[0] == dimension - 3:
            i = 2
        elif player_position[0] == dimension - 4:
            i = 3
        else:
            i = 4
        if player_position[1] == 0:
            j = 0
        elif player_position[1] == 1:
            j = -1
        elif player_position[1] == 2:
            j = -2
        elif player_position[1] == 3:
            j = -3
        else:
            j = -4
        if player_position[1] == dimension - 1:
            k = 0
        elif player_position[1] == dimension - 2:
            k = 1
        elif player_position[1] == dimension - 3:
            k = 2
        elif player_position[1] == dimension - 4:
            k = 3
        else:
            k = 4
        r1, r2, r3, r4 = h + player_position[0], i + player_position[0] + 1, \
            j + player_position[1], k + player_position[1] + 1
    for x in range(r1, r2):
        for y in range(r3, r4):
            place = (x * tile_size, y * tile_size + info_panel_height)
            if maze[x][y] == "wall":
                screen.blit(wall_surf, place)
            else:
                screen.blit(tile_surf, place)
                if maze[x][y] == "entrance":
                    screen.blit(entrance_surf, place)
                    if player_position != [x, y]:
                        screen.blit(grid_surf, place)
                elif maze[x][y] == "exit":
                    screen.blit(exit_surf, place)
                    if not boss_defeated:
                        screen.blit(grid_surf, place)
                elif maze[x][y] == "monster":
                    screen.blit(monster_surf, place)
                elif maze[x][y] == "boss":
                    screen.blit(boss_surf, place)
                elif maze[x][y] == "with_boss" and player_position != [x, y]:
                    if not boss_defeated:
                        maze[x][y] = "boss"
                    else:
                        maze[x][y] = "room"
                elif maze[x][y] == "coin":
                    screen.blit(coin_surf, place)
                elif maze[x][y] == "health":
                    screen.blit(health_surf, place)
                elif maze[x][y] == "treasure":
                    screen.blit(chest_surf, place)
                elif maze[x][y] == "shop":
                    screen.blit(shop_surf, place)
                elif maze[x][y] == "in_shop" and player_position != [x, y]:
                    screen.blit(shop_surf, place)
                    maze[x][y] = "shop"


def update_map():
    global player_hp, player_gold, boss_defeated
    x, y = player_position[0], player_position[1]
    if maze[x][y] == "monster":
        found_animation(monster_surf, monster_sound)
        maze[x][y] = "room"
    elif maze[x][y] == "boss":
        found_animation(boss_surf, boss_sound)
        maze[x][y] = "with_boss"
    elif maze[x][y] == "with_boss":
        screen.blit(tile_surf, (x * tile_size, y * tile_size + info_panel_height))
        screen.blit(boss_surf, (x * tile_size + 8, y * tile_size + info_panel_height))
        boss_defeated = True
        grid_open_sound.play()
    elif maze[x][y] == "coin":
        player_gold += maze_level
        found_animation(coin_surf, coin_sound)
        maze[x][y] = "room"
    elif maze[x][y] == "health":
        player_hp += maze_level
        found_animation(health_surf, health_sound)
        maze[x][y] = "room"
    elif maze[x][y] == "treasure":
        found_animation(chest_surf, chest_sound)
        maze[x][y] = "room"
    elif maze[x][y] == "shop":
        found_animation(shop_surf, shop_sound)
        maze[x][y] = "in_shop"
    elif maze[x][y] == "in_shop":
        screen.blit(shop_surf, (tile_size * player_position[0], tile_size * player_position[1] + info_panel_height))


def draw_player(position, r_hand, l_hand, size):
    x, y = position[0], position[1]
    player = player_surf
    if position[0] == 0:
        x_dif, y_dif = -6, - 18
    elif position[0] == dimension - 1:
        x_dif, y_dif = 7, 7
        player = pygame.transform.chop(player_surf, (21, 21, 32, 32))
        r_hand = pygame.transform.chop(r_hand, (21, 21, 32, 32))
        l_hand = pygame.transform.chop(l_hand, (21, 21, 32, 32))
    elif maze[x][y] == "with_boss":
        x_dif, y_dif = -8, 0
    else:
        x_dif, y_dif = 0, 0
    if size != 1:
        player = pygame.transform.scale(player, (32 * size, 32 * size))
        r_hand = pygame.transform.scale(r_hand, (32 * size, 32 * size))
        l_hand = pygame.transform.scale(l_hand, (32 * size, 32 * size))
    screen.blit(player, (x * tile_size + x_dif, y * tile_size + info_panel_height + y_dif))
    screen.blit(r_hand, (x * tile_size + x_dif, y * tile_size + info_panel_height + y_dif))
    screen.blit(l_hand, (x * tile_size + x_dif, y * tile_size + info_panel_height + y_dif))
    if darkness:
        screen.blit(mask_surf, (x * tile_size - 128, y * tile_size + info_panel_height - 128))


def info_panel():
    for i in range(dimension):
        screen.blit(wall_surf, (i * tile_size, 0))
    pygame.draw.rect(screen, "brown", (0, 0, WIDTH, info_panel_height), 3)
    if maze[player_position[0]][player_position[1]] == "with_boss":
        printer("Press SPACE to fight with boss", (10, tile_size), highlighted_font, "red")
    elif maze[player_position[0]][player_position[1]] == "in_shop":
        printer("Press SPACE to enter shop", (10, tile_size), highlighted_font, "lightblue")
    else:
        screen.blit(coin_surf, (20, -3))
        screen.blit(health_surf, (95, -3))
        info_surf = normal_font.render("Maze LVL            ATK           DEF", True, "grey50")
        info_rect = info_surf.get_rect(topleft=(175, 7))
        screen.blit(info_surf, info_rect)
        info_coin_surf = normal_font.render(str(player_gold), True, FONT_COLOR)
        info_coin_rect = info_coin_surf.get_rect(topleft=(50, 7))
        screen.blit(info_coin_surf, info_coin_rect)
        info_health_surf = normal_font.render(str(player_hp), True, FONT_COLOR)
        info_health_rect = info_health_surf.get_rect(topleft=(125, 7))
        screen.blit(info_health_surf, info_health_rect)
        info_maze_surf = normal_font.render(str(maze_level), True, FONT_COLOR)
        info_maze_rect = info_maze_surf.get_rect(topleft=(265, 7))
        screen.blit(info_maze_surf, info_maze_rect)
        info_attack_surf = normal_font.render(str(player_attack), True, FONT_COLOR)
        info_attack_rect = info_attack_surf.get_rect(topleft=(350, 7))
        screen.blit(info_attack_surf, info_attack_rect)
        info_defense_surf = normal_font.render(str(player_defense), True, FONT_COLOR)
        info_defense_rect = info_defense_surf.get_rect(topleft=(425, 7))
        screen.blit(info_defense_surf, info_defense_rect)


def found_animation(item, sound):
    x = player_position[0] * tile_size
    y = player_position[1] * tile_size + info_panel_height
    sound.play()
    for i in range(10):
        scale_x = tile_size + tile_size * (i / 5)
        scale_y = tile_size + tile_size * (i / 5)
        big_surf = pygame.transform.scale(item, (scale_x, scale_y))
        big_rect = big_surf.get_rect(center=(x + tile_size / 2, y + tile_size / 2))
        big_surf.set_alpha(int(255 - 255 * (i / 9)))
        draw_player((player_position[0], player_position[1]), wooden_buckler_surf, rusty_dagger_surf, 1)
        screen.blit(big_surf, big_rect)
        pygame.display.update()
        clock.tick(60)


def new_shop_list():
    list_elements = []
    while len(list_elements) != 3:
        element = choice(gears)
        if element not in list_elements:
            list_elements.append(element)
    print(list_elements)
    return list_elements


def shopping():
    global player_gold, maze, shop_list, quest_state
    maze[player_position[0]][player_position[1]] = "shop"
    in_shop = True
    selected = 0
    while in_shop:
        for shop_event in pygame.event.get():
            if shop_event.type == pygame.QUIT:
                pygame.quit()
            if shop_event.type == pygame.KEYDOWN:
                if shop_event.key == pygame.K_SPACE:
                    if selected < 3 and player_gold > shop_list[selected][1][0]:
                        body_place = shop_list[selected][1][3]
                        """wore = gears.index(wears[body_place])
                        print(wore)"""
                        update_attributes()
                        player_gold -= shop_list[selected][1][0]
                    elif selected == 3 and player_gold >= 30:
                        shop_list = new_shop_list()
                        player_gold -= 30
                    elif selected == 4:
                        if quest_state == "not in progress":
                            quest_state = "accepted"
                    elif selected == 5:
                        in_shop = False
                        shop_sound.play()
                if shop_event.key == pygame.K_DOWN:
                    if selected < 5:
                        selected += 1
                if shop_event.key == pygame.K_UP:
                    if selected > 0:
                        selected -= 1
            info_panel()
            for x in range(dimension):
                for y in range(7):
                    screen.blit(wall_surf, (x * tile_size, (y + 1) * tile_size))
            pygame.draw.rect(screen, "brown", (0, tile_size, WIDTH, 7 * tile_size), 3)
            tile = pygame.transform.scale(tile_surf, (32 * 3, 32 * 3))
            screen.blit(tile, (12 * tile_size, tile_size + info_panel_height))
            screen.blit(tile, (15 * tile_size, tile_size + info_panel_height))
            printer("Dear adventurer, welcome in my tiny shop. Please select (SPACE):", (10, tile_size * 2),
                    highlighted_font, "lightblue")
            if quest_state == "not in progress":
                quest_text = f"{quest} / reward: {maze_level * 15} gold"
            elif quest_state == "accepted":
                quest_text = f"{quest} / Accepted"
            else:
                quest_text = f"Good job! Here is your {maze_level * 15} gold"
                player_gold += maze_level * 15
                coin_sound.play()
            shop_items = [(f"Buy {shop_list[0][0]} / {shop_list[0][1][0]} gold", (10, tile_size * 3)),
                          (f"Buy {shop_list[1][0]} / {shop_list[1][1][0]} gold", (10, tile_size * 4)),
                          (f"Buy {shop_list[2][0]} / {shop_list[2][1][0]} gold", (10, tile_size * 5)),
                          (f"For a small fee, I can show you new goods / {maze_level * 10} gold", (10, tile_size * 6)),
                          (quest_text, (10, tile_size * 7)),
                          ("You leave my shop. Good luck on your journey!", (10, tile_size * 8))]
            for number, item in enumerate(shop_items):
                if number == selected:
                    font, col = highlighted_font, "green"
                    if selected < 3 and player_gold < shop_list[selected][1][0] or\
                            selected == 3 and player_gold < 30:
                        col = "red"
                else:
                    font, col = normal_font, "white"
                printer(item[0], item[1], font, col)
                for index, element in enumerate(gears):
                    if element[0] == wears[0]:
                        r_hand_surf = right_hand[index]
                    if element[0] == wears[0]:
                        l_hand_surf = left_hand[index]
                if selected < 3:
                    for index, element in enumerate(gears):
                        if element[0] == shop_list[selected][0]:
                            if shop_list[selected][1][3] == 0:
                                new_r_hand_surf = right_hand[index]
                                new_l_hand_surf = l_hand_surf
                            elif shop_list[selected][1][3] == 1:
                                new_r_hand_surf = r_hand_surf
                                new_l_hand_surf = left_hand[index - 12]
                            break
            draw_player((11, 1), new_r_hand_surf, new_l_hand_surf, 3)
            draw_player((15, 1), r_hand_surf, l_hand_surf, 3)
            pygame.display.update()
            """
            elif confirmation == "n":
                in_shop = False            
                selected = int(input()) - 1
                body_place = shop_list[selected][1][4]
                wore = gears[wears[body_place]]
                print(f"{shop_list[selected][0]} ({wears[body_place]}). Buy(y/n)?")
                print(f"Attack {shop_list[selected][1][1]} ({wore[1]})")
                print(f"Defense {shop_list[selected][1][2]} ({wore[2]})")
                print(f"Health {shop_list[selected][1][3]} ({wore[3]})")"""
    clock.tick(60)


def printer(text, pos, font, col):
    surf = font.render(text, True, col)
    rect = surf.get_rect(bottomleft=(pos[0], pos[1] - 4))
    screen.blit(surf, rect)


def update_attributes():
    global player_attack, player_defense, additional_hp
    player_attack, player_defense, additional_hp = 0, 0, 0
    for item in wears:
        pass
        """player_attack += gears[item][1]
        player_defense += gears[item][2]
        additional_hp += gears[item][3]"""


def maze_fade_in():
    tiles = []
    for x in range(dimension):
        for y in range(dimension):
            tiles.append((x, y))
    random.shuffle(tiles)
    for tile in tiles:
        if darkness:
            screen.blit(black_surf, (tile[0] * tile_size, tile[1] * tile_size + info_panel_height))
        else:
            if maze[tile[0]][tile[1]] == "wall":
                screen.blit(wall_surf, (tile[0] * tile_size, tile[1] * tile_size + info_panel_height))
            else:
                screen.blit(tile_surf, (tile[0] * tile_size, tile[1] * tile_size + info_panel_height))
        pygame.display.update()
        clock.tick(1000)


def maze_fade_out():
    tiles = []
    for x in range(dimension):
        for y in range(dimension):
            tiles.append((x, y))
    random.shuffle(tiles)
    for tile in tiles:
        screen.blit(black_surf, (tile[0] * tile_size, tile[1] * tile_size + info_panel_height))
        pygame.display.update()
        clock.tick(1000)


def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
        for x in range(dimension):
            for y in range(dimension + 1):
                place = (x * tile_size, y * tile_size)
                screen.blit(tile_surf, place)
        game_name_rect = maze_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(maze_surf, game_name_rect)
        info_surf = menu_font.render("Press SPACE to start", True, "black")
        info_rect = info_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 190))
        screen.blit(info_surf, info_rect)
        pygame.display.update()
        clock.tick(60)


def quest_checker(number):
    pass


quest = choice(quests)
shop_list = new_shop_list()
pygame.mixer.music.play(-1)
main_menu()
pygame.mixer.music.load("sounds/bg_sound.wav")
pygame.mixer.music.play(-1)
maze = maze_generator()
maze_fade_in()
for y in range(1, dimension - 1, 2):
    if maze[0][y] == "entrance":
        player_position = [0, y]
        break
pygame.mixer.music.play(-1)
new_level_sound.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                darkness = not darkness
            if event.key == pygame.K_LEFT and maze[player_position[0]][player_position[1]] != "entrance" \
                    and maze[player_position[0] - 1][player_position[1]] not in ("wall", "entrance"):
                player_position[0] -= 1
                steps_sound.play()
            elif event.key == pygame.K_RIGHT:
                if maze[player_position[0]][player_position[1]] == "entrance":
                    grid_slam_sound.play()
                if maze[player_position[0]][player_position[1]] == "exit":
                    new_level_sound.play()
                    maze_fade_out()
                    maze = maze_generator()
                    maze_level += 1
                    maze_fade_in()
                    boss_defeated = False
                    for y in range(1, dimension - 1, 2):
                        if maze[0][y] == "entrance":
                            player_position = [0, y]
                            break
                elif maze[player_position[0] + 1][player_position[1]] not in ("wall", "exit"):
                    player_position[0] += 1
                    steps_sound.play()
                elif maze[player_position[0] + 1][player_position[1]] == "exit" and boss_defeated:
                    player_position[0] += 1
                    steps_sound.play()
            elif event.key == pygame.K_UP and maze[player_position[0]][player_position[1] - 1] != "wall":
                player_position[1] -= 1
                steps_sound.play()
            elif event.key == pygame.K_DOWN and maze[player_position[0]][player_position[1] + 1] != "wall":
                player_position[1] += 1
                steps_sound.play()
            elif event.key == pygame.K_SPACE and maze[player_position[0]][player_position[1]] == "in_shop":
                shopping()

    draw_map()
    update_map()
    draw_player(player_position, wooden_buckler_surf, rusty_dagger_surf, 1)
    info_panel()
    update_attributes()
    pygame.display.update()

    clock.tick(60)
