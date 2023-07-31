from maze_generator import *
from data import *
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + info_panel_height))
pygame.display.set_caption("Maze of fear")
clock = pygame.time.Clock()


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)


def draw_map():
    if not darkness:
        r1, r2, r3, r4 = 0, dimension, 0, dimension
    else:
        pygame.draw.rect(screen, "black", (0, info_panel_height, dimension * tile_size, dimension * tile_size))
        if player_position[0] < 4:
            h = - player_position[0]
        else:
            h = -4
        if player_position[0] > dimension - 5:
            i = dimension - 1 - player_position[0]
        else:
            i = 4
        if player_position[1] < 0:
            j = - player_position[1]
        else:
            j = -4
        if player_position[1] > dimension - 5:
            k = dimension - 1 - player_position[1]
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
                    screen.blit(monster_values[maze_level - 1][3], place)
                elif maze[x][y] == "boss":
                    screen.blit(boss_values[maze_level - 1][3], place)
                elif maze[x][y] == "coin":
                    screen.blit(coin_surf, place)
                elif maze[x][y] == "health":
                    screen.blit(health_surf, place)
                elif maze[x][y] == "well":
                    screen.blit(well_surf, place)
                elif maze[x][y] == "shop":
                    screen.blit(shop_surf, place)
                elif maze[x][y] == "rat":
                    screen.blit(rat_surf, place)
                elif maze[x][y] == "pearl":
                    screen.blit(pearl_surf, place)
                elif maze[x][y] == "log":
                    screen.blit(log_surf, place)
                elif maze[x][y] == "note":
                    screen.blit(note_surf, place)
                elif maze[x][y] == "egg":
                    screen.blit(egg_surf, place)


def update_map():
    draw_map()
    global player_hp, player_gold, boss_defeated, quest_item_quantity, quest_state
    x, y = player_position[0], player_position[1]
    if maze[x][y] == "monster":
        found_animation(monster_values[maze_level - 1][3], monster_sound)
        maze[x][y] = "room"
        monster_fight(monster_values[maze_level - 1][0], monster_values[maze_level - 1][1],
                      monster_values[maze_level - 1][2])
    elif maze[x][y] == "boss":
        found_animation(boss_values[maze_level - 1][3], boss_sound)
    elif maze[x][y] == "coin":
        player_gold += maze_level
        found_animation(coin_surf, coin_sound)
        maze[x][y] = "room"
    elif maze[x][y] == "health":
        found_animation(health_surf, health_sound)
        if player_hp < player_max_hp:
            player_hp += maze_level
            maze[x][y] = "room"
    elif maze[x][y] == "well":
        found_animation(well_surf, chest_sound)
        maze[x][y] = "room"
        update_map()
        draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                    wears[0][2], wears[1][2], wears[2][2], 1)
        chest()
    elif maze[x][y] == "shop":
        found_animation(shop_surf, shop_sound)
    elif maze[x][y] == "rat":
        found_animation(rat_surf, rat_sound)
        quest_item_quantity -= 1
        maze[x][y] = "room"
    elif maze[x][y] == "pearl":
        found_animation(pearl_surf, coin_sound)
        quest_item_quantity -= 1
        maze[x][y] = "room"
    elif maze[x][y] == "log":
        found_animation(log_surf, chop_sound)
        quest_item_quantity -= 1
        maze[x][y] = "room"
    elif maze[x][y] == "note":
        found_animation(note_surf, coin_sound)
        quest_item_quantity -= 1
        maze[x][y] = "room"
    elif maze[x][y] == "egg":
        found_animation(egg_surf, chop_sound)
        quest_item_quantity -= 1
        maze[x][y] = "room"
    if not quest_item_quantity and quest_state == "accepted":
        quest_state = "done"


def draw_player(position, r_hand, l_hand, body, size):
    x, y = position[0], position[1]
    player = player_surf
    if maze[player_position[0]][player_position[1]] == "entrance":
        x_dif, y_dif = -6, - 18
    elif maze[player_position[0]][player_position[1]] == "exit":
        x_dif, y_dif = 7, 7
        player = pygame.transform.chop(player_surf, (21, 21, 32, 32))
        r_hand = pygame.transform.chop(r_hand, (21, 21, 32, 32))
        l_hand = pygame.transform.chop(l_hand, (21, 21, 32, 32))
        body = pygame.transform.chop(body, (21, 21, 32, 32))
    else:
        x_dif, y_dif = 0, 0
    if size != 1:
        player = pygame.transform.scale(player, (32 * size, 32 * size))
        r_hand = pygame.transform.scale(r_hand, (32 * size, 32 * size))
        l_hand = pygame.transform.scale(l_hand, (32 * size, 32 * size))
        body = pygame.transform.scale(body, (32 * size, 32 * size))
    screen.blit(player, (x + x_dif, y + y_dif))
    screen.blit(body, (x + x_dif, y + y_dif))
    screen.blit(r_hand, (x + x_dif, y + y_dif))
    screen.blit(l_hand, (x + x_dif, y + y_dif))
    if darkness and size == 1:
        screen.blit(mask_surf, (x - 128, y - 128))


def info_panel():
    for i in range(dimension):
        screen.blit(wall_surf, (i * tile_size, 0))
    pygame.draw.rect(screen, "brown", (0, 0, WIDTH, info_panel_height), 3)
    if maze[player_position[0]][player_position[1]] == "boss":
        printer("Press SPACE to fight with boss", (10, tile_size), highlighted_font, "red")
    elif maze[player_position[0]][player_position[1]] == "shop" and outside:
        printer("Press SPACE to enter shop", (10, tile_size), highlighted_font, "purple")
    else:
        printer(f"Gold: {player_gold}     Health: {player_hp} / {player_max_hp}     Maze level: {maze_level}     "
                f"ATK: {player_attack}     DEF: {player_defense}", (10, tile_size), highlighted_font, "white")
    if quest_state in ("accepted", "done"):
        printer(f"{quest_item_quantity}", (WIDTH - 34, tile_size), highlighted_font, "white")
        screen.blit(quest[2], (WIDTH - 70, 0))


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
        draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                    wears[0][2], wears[1][2], wears[2][2], 1)
        screen.blit(big_surf, big_rect)
        info_panel()
        pygame.display.update()
        clock.tick(60)


def new_shop_list():
    list_elements = [gears[maze_level],
                     gears[11 + maze_level],
                     gears[22 + maze_level]]

    return list_elements


def shopping():
    global player_gold, maze, shop_list, quest_state, quest_item_quantity, quest, outside, player_hp
    outside = False
    selected = 0
    while not outside:
        for shop_event in pygame.event.get():
            if shop_event.type == pygame.QUIT:
                pygame.quit()
            shop_text = []
            if shop_event.type == pygame.KEYDOWN:
                if shop_event.key == pygame.K_SPACE:
                    if selected < 3 and player_gold >= shop_list[selected][1][0] \
                            and wears[selected] != shop_list[selected]:
                        wears[selected] = shop_list[selected]
                        update_attributes()
                        player_gold -= shop_list[selected][1][0]
                    elif selected == 3 and player_gold >= player_max_hp - player_hp:
                        player_hp = player_max_hp
                        player_gold -= player_max_hp - player_hp
                    elif selected == 4:
                        if quest_state == "not in progress":
                            quest_state = "accepted"
                            quest_item_placing(maze, quest_item_quantity, quest[1])
                        if quest_state == "done":
                            player_gold += maze_level * 15
                            coin_sound.play()
                            quest_state = "not in progress"
                            quest = choice(quests)
                            quest_item_quantity = int(randrange(2, 7) + maze_level * 2)
                    elif selected == 5:
                        shop_sound.play()
                        outside = True
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
            screen.blit(tile, (15 * tile_size, tile_size + info_panel_height))
            printer("Dear adventurer, welcome in my tiny shop.", (10, tile_size * 2), highlighted_font, "purple")
            if quest_state == "not in progress":
                quest_text = f"{quest[0]} Please bring {quest_item_quantity} {quest[1]}s / quest reward: " \
                             f"{maze_level * 15} gold"
            elif quest_state == "accepted":
                quest_text = f"{quest[0]} Please bring {quest_item_quantity} {quest[1]}s / Accepted"
            else:
                quest_text = f"Good job! Here is your {maze_level * 15} gold"
            for i in range(3):
                if wears[i] == shop_list[i]:
                    shop_text.append((f"You already bought {shop_list[i][0]}", (10, tile_size * (i + 3))))
                else:
                    shop_text.append((f"Buy {shop_list[i][0]} / {shop_list[i][1][0]} gold", (10, tile_size * (i + 3))))

            shop_text.append(
                (f"For a small fee, I can heal you / {player_max_hp - player_hp} gold", (10, tile_size * 6)))
            shop_text.append((quest_text, (10, tile_size * 7)))
            shop_text.append(("Good luck on your journey!", (10, tile_size * 8)))

            for number, item in enumerate(shop_text):
                if number == selected:
                    font, col = highlighted_font, "green"
                    if selected < 3 and (player_gold < shop_list[selected][1][0]
                                         or wears[selected] == shop_list[selected]) \
                            or selected == 3 and (player_gold < player_max_hp - player_hp
                                                  or player_hp == player_max_hp):
                        col = "red"
                else:
                    font, col = normal_font, "white"
                printer(item[0], item[1], font, col)
                r_hand_surf = wears[0][2]
                l_hand_surf = wears[1][2]
                body_surf = wears[2][2]
                if selected < 3:
                    if selected == 0:
                        r_hand_surf = shop_list[selected][2]
                    elif selected == 1:
                        l_hand_surf = shop_list[selected][2]
                    elif selected == 2:
                        body_surf = shop_list[selected][2]
                    screen.blit(tile, (11 * tile_size, 1 * tile_size + info_panel_height))
                    draw_player((11 * tile_size, 1 * tile_size + info_panel_height),
                                r_hand_surf, l_hand_surf, body_surf, 3)
            draw_player((15 * 32, 1 * tile_size + info_panel_height), wears[0][2], wears[1][2], wears[2][2], 3)
            pygame.display.update()
    clock.tick(60)


def printer(text, pos, font, col):
    surf = font.render(text, True, col)
    rect = surf.get_rect(bottomleft=(pos[0], pos[1] - 4))
    screen.blit(surf, rect)


def update_attributes():
    global player_attack, player_defense, player_max_hp
    player_attack, player_defense, player_max_hp = 0, 0, 0
    for item in wears:
        player_attack += item[1][1]
        player_defense += item[1][2]
        player_max_hp += item[1][3]


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


def quest_item_placing(maze, number, type):
    counter = 0
    while counter != number:
        random_x = randrange(1, dimension - 1)
        random_y = randrange(1, dimension - 1)
        if maze[random_x][random_y] == "room":
            maze[random_x][random_y] = type
            counter += 1


def monster_fight(monster_attack, monster_defense, monster_health):
    global player_hp
    if maze[player_position[0]][player_position[1]] == "boss":
        opponent_surface = boss_values[maze_level - 1][3]
    else:
        opponent_surface = monster_values[maze_level - 1][3]
    monster_max_health = monster_health
    state = "attack"
    while True:
        fight_stage()
        printer("Space", (tile_size * player_position[0] - 5, tile_size * player_position[1] + 92), normal_font,
                "white")
        draw_player(((player_position[0] - 1) * tile_size, player_position[1] * tile_size + info_panel_height),
                    wears[0][2], wears[1][2], wears[2][2], 1)
        screen.blit(opponent_surface, ((tile_size * (player_position[0] + 1)),
                                       tile_size * (player_position[1]) + info_panel_height))
        pygame.draw.rect(screen, "black", (tile_size * (player_position[0] - 1) + 4,
                                           tile_size * (player_position[1] - 1) + 30 + info_panel_height, 28, 3))
        pygame.draw.rect(screen, "red", (tile_size * (player_position[0] - 1) + 4,
                                         tile_size * (player_position[1] - 1) + 30 + info_panel_height,
                                         28 * (player_hp / player_max_hp), 3))
        pygame.draw.rect(screen, "black", (tile_size * (player_position[0] - 1) + 64,
                                           tile_size * (player_position[1] - 1) + 30 + info_panel_height, 28, 3))
        pygame.draw.rect(screen, "red", (tile_size * (player_position[0] - 1) + 64,
                                         tile_size * (player_position[1] - 1) + 30 + info_panel_height,
                                         28 * (monster_health / monster_max_health), 3))
        printer(str(player_hp), (tile_size * (player_position[0] - 1) + 6, tile_size * (player_position[1] - 1) + 33
                                 + info_panel_height), normal_font, "white")
        printer(str(monster_health), (tile_size * (player_position[0] - 1) + 66, tile_size * (player_position[1] - 1)
                                      + 33 + info_panel_height), normal_font, "white")
        for fight_event in pygame.event.get():
            if fight_event.type == pygame.QUIT:
                pygame.quit()
            if fight_event.type == pygame.KEYDOWN:
                if fight_event.key == pygame.K_SPACE:
                    if state == "attack":
                        if choice(range(0, 100)) < 50 + 3 * (player_attack - monster_defense):
                            damage = int(player_attack * attack("player", "hit"))
                            printer(str(-damage), (tile_size * (player_position[0] - 1) + 66,
                                                   tile_size * (player_position[1] - 1) + 33 + info_panel_height),
                                    highlighted_font, "white")
                            pygame.display.update()
                            pygame.time.wait(1000)
                            monster_health -= damage
                            if monster_health <= 0:
                                print("win")
                                return "win"
                            else:
                                state = "defense"
                        else:
                            attack("player", "block")
                            state = "defense"
                    elif state == "defense":
                        if choice(range(0, 100)) < 50 + 3 * (monster_attack - player_defense):
                            damage = int(monster_attack * (1 - attack("monster", "hit")))
                            printer(str(-damage), (tile_size * (player_position[0] - 1) + 6,
                                                   tile_size * (player_position[1] - 1) + 33 + info_panel_height),
                                    highlighted_font, "white")
                            pygame.display.update()
                            pygame.time.wait(1000)
                            player_hp -= damage
                            if player_hp <= 0:
                                print("defeated")
                                player_hp = player_max_hp
                                return "defeated"
                            else:
                                state = "attack"
                        else:
                            attack("monster", "block")
                            state = "attack"
        info_panel()
        pygame.display.update()
        clock.tick(60)


def fight_stage():
    for i in range(-1, 2):
        for j in range(-1, 2):
            screen.blit(tile_surf, (tile_size * (player_position[0] + i),
                                    tile_size * (player_position[1] + j) + info_panel_height))
    pygame.draw.rect(screen, "black ", (tile_size * (player_position[0] - 1),
                                        tile_size * (player_position[1] - 1) + info_panel_height,
                                        3 * tile_size, 3 * tile_size), 3)


def attack(who, action):
    if maze[player_position[0]][player_position[1]] == "boss":
        opponent_surface = boss_values[maze_level - 1][3]
    else:
        opponent_surface = monster_values[maze_level - 1][3]
    if action == "hit":
        surf, text = hit_surf, "strike"
        wait = True
    elif action == "block":
        surf, text = block_surf, "block"
        wait = False
    if who == "player":
        for i in range(40):
            fight_stage()
            draw_player(((player_position[0] - 1) * tile_size + i, player_position[1] * tile_size + info_panel_height),
                        wears[0][2], wears[1][2], wears[2][2], 1)
            screen.blit(opponent_surface, ((tile_size * (player_position[0] + 1)),
                                           tile_size * (player_position[1]) + info_panel_height))
            info_panel()
            clock.tick(180)
            pygame.display.update()
        fight_stage()
        draw_player(((player_position[0] - 1) * tile_size + 40, player_position[1] * tile_size + info_panel_height),
                    wears[0][2], wears[1][2], wears[2][2], 1)
        screen.blit(opponent_surface, ((tile_size * (player_position[0] + 1)),
                                       tile_size * (player_position[1]) + info_panel_height))
        screen.blit(surf, ((tile_size * (player_position[0] + 1)),
                           tile_size * (player_position[1]) - 32 + info_panel_height))
        printer(text, (tile_size * player_position[0] - 4,
                       tile_size * player_position[1] + 92), normal_font, "white")
        info_panel()
        clock.tick(60)
        pygame.display.update()
        pygame.time.wait(600)
    elif who == "monster":
        for i in range(40):
            fight_stage()
            draw_player(((player_position[0] - 1) * tile_size, player_position[1] * tile_size + info_panel_height),
                        wears[0][2], wears[1][2], wears[2][2], 1)
            screen.blit(opponent_surface, ((tile_size * (player_position[0] + 1) - i),
                                           tile_size * (player_position[1]) + info_panel_height))
            info_panel()
            clock.tick(180)
            pygame.display.update()
        fight_stage()
        draw_player(((player_position[0] - 1) * tile_size, player_position[1] * tile_size + info_panel_height),
                    wears[0][2], wears[1][2], wears[2][2], 1)
        screen.blit(opponent_surface, ((tile_size * (player_position[0] + 1) - 40),
                                       tile_size * (player_position[1]) + info_panel_height))
        screen.blit(surf, (((player_position[0] - 1) * tile_size,
                            player_position[1] * tile_size - 32 + info_panel_height)))
        printer(text, (tile_size * player_position[0] - 4,
                       tile_size * player_position[1] + 92), normal_font, "white")
        info_panel()
        clock.tick(60)
        pygame.display.update()
        pygame.time.wait(600)
    value = 1
    counter = 0
    while wait:
        if counter == 60:
            counter = 0
            value = 1
        value = (value * 1.1)
        counter += 1

        if action == "hit":
            if who == "player":
                text, rgb = "ATK power", (255, 0, 0, 100)
            else:
                text, rgb = "DEF power ", (0, 255, 0, 100)
            for i in range(-1, 2):
                screen.blit(tile_surf, (tile_size * (player_position[0] + i),
                                        tile_size * (player_position[1] + 1) + info_panel_height))
            printer(text, (tile_size * player_position[0] - 24,
                           tile_size * player_position[1] + 92), normal_font, "white")
            draw_rect_alpha(screen, rgb, ((tile_size * (player_position[0] - 1),
                                           tile_size * (player_position[1] - 1) + info_panel_height + 64,
                                           (value / 304) * 3 * tile_size, 32)))
            pygame.draw.rect(screen, "black ", (tile_size * (player_position[0] - 1),
                                                tile_size * (player_position[1] - 1) + info_panel_height,
                                                3 * tile_size, 3 * tile_size), 3)
            info_panel()
            clock.tick(60)
            pygame.display.update()

            for fight_event in pygame.event.get():
                if fight_event.type == pygame.QUIT:
                    pygame.quit()
                if fight_event.type == pygame.KEYDOWN:
                    if fight_event.key == pygame.K_SPACE:
                        if action == "hit":
                            return value / 304  # factor (between 0 - 1)


def chest():
    global darkness, player_hp, player_gold
    chest_text = ("The map of this level",
                  "Heal for full health",
                  f"A purse with {int(2.1 ** maze_level) * 10} gold")
    done = False
    selected = 0
    while not done:
        info_panel()
        for x in range(dimension):
            for y in range(4):
                screen.blit(wall_surf, (x * tile_size, (y + 1) * tile_size))
        printer("I am a Wishing Well. Please tell me what you want:", (10, tile_size * 2), highlighted_font, "purple")
        for count, text in enumerate(chest_text):
            if count == selected:
                font, col = highlighted_font, "green"
            else:
                font, col = normal_font, "white"
            printer(text, (10, tile_size * (3 + count)), font, col)
        pygame.draw.rect(screen, "brown", (0, tile_size, WIDTH, 4 * tile_size), 3)
        for chest_event in pygame.event.get():
            if chest_event.type == pygame.QUIT:
                pygame.quit()
            if chest_event.type == pygame.KEYDOWN:
                if chest_event.key == pygame.K_DOWN:
                    if selected < 2:
                        selected += 1
                if chest_event.key == pygame.K_UP:
                    if selected > 0:
                        selected -= 1
                if chest_event.key == pygame.K_SPACE:
                    if selected == 0:
                        darkness = False
                    elif selected == 1:
                        player_hp = player_max_hp
                    else:
                        player_gold += int(2.1 ** maze_level) * 10
                    done = True
        pygame.display.update()


quest = choice(quests)
quest_item_quantity = int(randrange(2, 7) + maze_level * 2)
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
            if event.key == pygame.K_9:
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
                    darkness = True
                    maze_level += 1
                    maze_fade_in()
                    boss_defeated = False
                    quest_state = "not in progress"
                    quest = choice(quests)
                    quest_item_quantity = int(randrange(2, 7) + maze_level * 2)
                    shop_list = new_shop_list()
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
            elif event.key == pygame.K_SPACE and maze[player_position[0]][player_position[1]] == "shop":
                shopping()
            elif event.key == pygame.K_SPACE and maze[player_position[0]][player_position[1]] == "boss":
                result = monster_fight(boss_values[maze_level - 1][0], boss_values[maze_level - 1][1],
                                       boss_values[maze_level - 1][2])
                if result == "win":
                    boss_defeated = True
                    maze[player_position[0]][player_position[1]] = "room"
                    grid_open_sound.play()
            update_map()

    draw_map()
    draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                wears[0][2], wears[1][2], wears[2][2], 1)
    info_panel()
    update_attributes()
    pygame.display.update()
    clock.tick(60)
