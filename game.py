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
        r1, r2, r3, r4 = h + player_position[0], i + player_position[0] + 1,\
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
                    screen.blit(monster_surfs[maze_level - 1], place)
                elif maze[x][y] == "boss":
                    screen.blit(boss_surfs[maze_level - 1], place)
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
    global player_hp, player_gold, quest_item_quantity, quest_state, player_position, darkness
    x, y = player_position[0], player_position[1]
    if maze[x][y] == "monster":
        found_animation(monster_surfs[maze_level - 1], monster_sound)
        fight_result = monster_fight()
        if fight_result == "win":
            maze[x][y] = "room"
        else:
            search = True
            while search:
                random_x = randrange(1, dimension - 1)
                random_y = randrange(1, dimension - 1)
                if maze[random_x][random_y] == "room":
                    player_position = [random_x, random_y]
                    search = False
            wake_up_sound.play()
            darkness = True
            for i in range(256):
                draw_map()
                draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                            wears[0][2], wears[1][2], wears[2][2], 1)
                draw_rect_alpha(screen, (0, 0, 0, 255 - i), (0, 0, WIDTH, HEIGHT + info_panel_height))
                pygame.display.update()
                clock.tick(60)
    elif maze[x][y] == "boss":
        found_animation(boss_surfs[maze_level - 1], choice(boss_sounds))
    elif maze[x][y] == "coin":
        player_gold += int(1.5 ** maze_level * 5)
        found_animation(coin_surf, coin_sound)
        maze[x][y] = "room"
    elif maze[x][y] == "health":
        found_animation(health_surf, health_sound)
        if player_hp < player_max_hp:
            if player_max_hp - player_hp >= maze_level * 5:
                player_hp += maze_level * 5
            else:
                player_hp = player_max_hp
            maze[x][y] = "room"
    elif maze[x][y] == "well":
        found_animation(well_surf, chest_sound)
        maze[x][y] = "room"
        update_map()
        draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                    wears[0][2], wears[1][2], wears[2][2], 1)
        well()
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
    elif maze[x][y] == "pear":
        found_animation(pear_surf, chop_sound)
        quest_item_quantity -= 1
        maze[x][y] = "room"
    elif maze[x][y] == "arrow":
        found_animation(arrow_surf, chop_sound)
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
    pygame.draw.rect(screen, "grey30", (0, 0, WIDTH, info_panel_height))
    pygame.draw.rect(screen, "black", (0, 0, WIDTH, info_panel_height), 3)
    if maze[player_position[0]][player_position[1]] == "boss":
        printer("Press SPACE to fight with boss", (WIDTH / 2, tile_size / 2), highlighted_font, "red", "center")
    elif maze[player_position[0]][player_position[1]] == "shop" and outside:
        printer("Press SPACE to enter shop", (WIDTH / 2, tile_size / 2), highlighted_font, "red", "center")
    else:
        printer(f"Maze LVL: {maze_level}    Gold: {player_gold}    HP: {player_hp} / {player_max_hp}    "
                f"ATK: {player_atk}    DMG: {player_dmg}    DEF: {player_def}",
                (WIDTH / 2, tile_size / 2), normal_font, "white", "center")
    if quest_state in ("accepted", "done"):
        pygame.draw.rect(screen, "grey30", (8 * tile_size, dimension * tile_size, 96, info_panel_height))
        pygame.draw.rect(screen, "black", (8 * tile_size, dimension * tile_size, 96, info_panel_height), 3)
        printer(f"{quest_item_quantity}", (WIDTH / 2 - 24, dimension * tile_size + 30), highlighted_font, "white")
        screen.blit(quest[2], (WIDTH / 2 + 8, dimension * tile_size))


def found_animation(item, sound):
    x = player_position[0] * tile_size
    y = player_position[1] * tile_size + info_panel_height
    sound.play()
    draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                wears[0][2], wears[1][2], wears[2][2], 1)
    for i in range(10):
        scale_x = tile_size + tile_size * (i / 3)
        scale_y = tile_size + tile_size * (i / 3)
        big_surf = pygame.transform.scale(item, (scale_x, scale_y))
        big_rect = big_surf.get_rect(center=(x + tile_size / 2, y + tile_size / 2))
        big_surf.set_alpha(int(255 - 255 * (i / 9)))
        screen.blit(big_surf, big_rect)
        info_panel()
        pygame.display.update()
        clock.tick(40)


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
                            player_gold += 2**maze_level * 40
                            coin_sound.play()
                            quest_state = "not in progress"
                            quest = choice(quests)
                            quest_item_quantity = int(randrange(4, 7) + maze_level)
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
            pygame.draw.rect(screen, "grey30", (0, tile_size, WIDTH, 7 * tile_size))
            pygame.draw.rect(screen, "black", (0, tile_size, WIDTH, 7 * tile_size), 3)
            printer("Dear adventurer, welcome in my tiny shop.", (WIDTH / 2, tile_size + 18),
                    prologue_font, "black", "center")
            if quest_state == "not in progress":
                quest_text = f"{quest[0]} Please bring {quest_item_quantity} {quest[1]}s / quest reward: " \
                             f"{2**maze_level * 40} gold"
            elif quest_state == "accepted":
                quest_text = f"{quest[0]} Please bring {quest_item_quantity} {quest[1]}s / Accepted"
            else:
                quest_text = f"Good job! Here is your {2**maze_level * 40} gold"
            for i in range(3):
                if wears[i] == shop_list[i]:
                    shop_text.append((f"You already bought {shop_list[i][0]}", (WIDTH / 2, tile_size * (i + 3) - 13)))
                else:
                    shop_text.append((f"Buy {shop_list[i][0]} / {shop_list[i][1][0]} gold",
                                      (WIDTH / 2, tile_size * (i + 3) - 13)))
            shop_text.append(
                (f"For a small fee, I can heal you / {player_max_hp - player_hp} gold",
                 (WIDTH / 2, tile_size * 6 - 13)))
            shop_text.append((quest_text, (WIDTH / 2, tile_size * 7 - 13)))
            shop_text.append(("Good luck on your journey!", (WIDTH / 2, tile_size * 8 - 13)))

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
                printer(item[0], item[1], font, col, "center")
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
                    draw_player((15 * tile_size, 1 * tile_size + info_panel_height),
                                r_hand_surf, l_hand_surf, body_surf, 3)
            draw_player((32, 1 * tile_size + info_panel_height), wears[0][2], wears[1][2], wears[2][2], 3)
            pygame.display.update()
    clock.tick(60)


def printer(text, pos, font, col, align="bottomleft"):
    surf = font.render(text, True, col)
    if align == "bottomleft":
        rect = surf.get_rect(bottomleft=(pos[0], pos[1] - 4))
    elif align == "center":
        rect = surf.get_rect(center=(pos[0], pos[1]))
    screen.blit(surf, rect)


def update_attributes():
    global player_atk, player_dmg, player_def, player_max_hp
    player_atk, player_dmg, player_def, player_max_hp = 0, 0, 0, 0
    for item in wears:
        player_atk += item[1][1]
        player_dmg += item[1][2]
        player_def += item[1][3]
        player_max_hp += item[1][4]


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
    pygame.mixer.music.load("sounds/menu.wav")
    pygame.mixer.music.play(-1)
    menu = True
    counter = 0
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
        gate_rect = gate_surf.get_rect(topleft=(0, 4 * tile_size))
        game_name_rect = maze_surf.get_rect(center=(WIDTH / 2, 70))
        info_surf = menu_font.render("Press SPACE to start", True, "black")
        info_rect = info_surf.get_rect(center=(WIDTH / 2, 562))
        screen.blit(gate_surf, gate_rect)
        for number, sentence in enumerate(prologue_text):
            printer(sentence, (70, 530 - int(counter) + 35 * number), prologue_font, "black")
            printer(sentence, (68, 528 - int(counter) + 35 * number), prologue_font, "darkred")
        for x in range(dimension):
            for y in range(4):
                place = (x * tile_size, y * tile_size)
                screen.blit(tile_surf, place)
        for x in range(dimension):
            for y in range(15, 20):
                place = (x * tile_size, y * tile_size)
                screen.blit(tile_surf, place)
        screen.blit(maze_surf, game_name_rect)
        screen.blit(info_surf, info_rect)
        pygame.display.update()
        counter += 0.25
        if counter > 1500:
            counter = 0
        clock.tick(60)


def quest_item_placing(maze, number, item):
    counter = 0
    while counter != number:
        random_x = randrange(1, dimension - 1)
        random_y = randrange(1, dimension - 1)
        if maze[random_x][random_y] == "room":
            maze[random_x][random_y] = item
            counter += 1


def monster_fight():
    global player_hp, boss_hp, player_gold
    if maze[player_position[0]][player_position[1]] == "boss fight":
        opponent_surface = boss_surfs[maze_level - 1]
        opponent_atk, opponent_dmg, opponent_def, opponent_hp = boss_atk, boss_dmg, boss_def, boss_hp
        opponent_max_hp = boss_max_hp
    else:
        opponent_surface = monster_surfs[maze_level - 1]
        opponent_atk, opponent_dmg, opponent_def, opponent_hp = monster_atk, monster_dmg, monster_def, monster_hp
        opponent_max_hp = monster_hp
    opponent_surface = pygame.transform.scale(opponent_surface, (64, 64))
    state = "attack"
    fight_stage(start=True)
    while True:
        fight_stage()
        printer("SPACE", (WIDTH / 2 - 25, HEIGHT / 2 + 90), highlighted_font, "white")
        draw_player((WIDTH / 2 - 96, HEIGHT / 2), wears[0][2], wears[1][2], wears[2][2], 2)
        screen.blit(opponent_surface, (WIDTH / 2 + 32, HEIGHT / 2))
        pygame.draw.rect(screen, "black", (WIDTH / 2 - 90, HEIGHT / 2 - 8, 56, 5))
        pygame.draw.rect(screen, "red", (WIDTH / 2 - 90, HEIGHT / 2 - 8, 56 * (player_hp / player_max_hp), 5))
        pygame.draw.rect(screen, "black", (WIDTH / 2 + 38, HEIGHT / 2 - 8, 56, 5))
        pygame.draw.rect(screen, "red", (WIDTH / 2 + 38, HEIGHT / 2 - 8, 56 * (opponent_hp / opponent_max_hp), 5))
        printer(str(player_hp), (WIDTH / 2 - 90, HEIGHT / 2 - 8), normal_font, "white")
        printer(str(opponent_hp), (WIDTH / 2 + 38, HEIGHT / 2 - 8), normal_font, "white")
        for fight_event in pygame.event.get():
            if fight_event.type == pygame.QUIT:
                pygame.quit()
            if fight_event.type == pygame.KEYDOWN:
                if fight_event.key == pygame.K_SPACE:
                    if state == "attack":
                        if choice(range(0, 100)) < 50 * (player_atk / opponent_def):
                            damage = int(player_dmg * attack("player", "hit"))
                            if maze[player_position[0]][player_position[1]] == "boss fight":
                                boss_hp -= damage
                            printer(str(-damage), (WIDTH / 2 + 45, HEIGHT / 2 - 70), highlighted_font, "red")
                            pygame.display.update()
                            monster_ah_sound.play()
                            pygame.time.wait(1000)
                            opponent_hp -= damage
                            if opponent_hp <= 0:
                                pygame.draw.rect(screen, "black", (WIDTH / 2 - 98, HEIGHT / 2 + 64, 194, 24))
                                printer(f"You win, and found {int(1.8 ** maze_level * 6)} gold",
                                        (WIDTH / 2, HEIGHT / 2 + 80), highlighted_font, "white", "center")
                                win_sound.play()
                                pygame.display.update()
                                pygame.time.wait(2000)
                                player_gold += int(1.8 ** maze_level * 6)
                                coin_sound.play()
                                return "win"
                            else:
                                state = "defense"
                        else:
                            attack("player", "block")
                            state = "defense"
                    elif state == "defense":
                        if choice(range(0, 100)) < 50 * (opponent_atk / player_def):
                            damage = int(opponent_dmg * (1 - attack("monster", "hit")))
                            printer(str(-damage), (WIDTH / 2 - 78, HEIGHT / 2 - 70), highlighted_font, "red")
                            pygame.display.update()
                            player_ah_sound.play()
                            pygame.time.wait(1000)
                            player_hp -= damage
                            if player_hp <= 0:
                                pygame.draw.rect(screen, "black", (WIDTH / 2 - 98, HEIGHT / 2 + 64, 194, 24))
                                printer("You've been knocked out", (WIDTH / 2 - 90, HEIGHT / 2 + 90), highlighted_font,
                                        "red")
                                lose_sound.play()
                                for i in range(256):
                                    draw_rect_alpha(screen, (0, 0, 0, 1), (0, 0, WIDTH, HEIGHT + info_panel_height))
                                    pygame.display.update()
                                    clock.tick(90)
                                player_hp = int(player_max_hp * 0.33)
                                return "defeated"
                            else:
                                state = "attack"
                        else:
                            attack("monster", "block")
                            state = "attack"
        info_panel()
        pygame.display.update()
        clock.tick(60)


def fight_stage(start=False):
    if start:
        for i in range(31):
            pygame.draw.rect(screen, "black", (0, info_panel_height, WIDTH, HEIGHT))
            transition_surf = pygame.transform.scale(fight_stage_surf, (160 * (1 + i / 30), 64 * (1 + i / 30)))
            transition_rect = transition_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            screen.blit(transition_surf, transition_rect)
            pygame.display.update()
            clock.tick(180)
    pygame.draw.rect(screen, "black", (0, info_panel_height, WIDTH, HEIGHT))
    surf = pygame.transform.scale(fight_stage_surf, (320, 128))
    rect = surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(surf, rect)


def attack(who, action):
    if maze[player_position[0]][player_position[1]] == "boss fight":
        opponent_surface = boss_surfs[maze_level - 1]
    else:
        opponent_surface = monster_surfs[maze_level - 1]
    opponent_surface = pygame.transform.scale(opponent_surface, (64, 64))
    if action == "hit":
        surf, text = pygame.transform.scale(hit_surf, (64, 64)), "STRIKE"
        hit_sound.play()
        wait = True
    elif action == "block":
        surf, text = pygame.transform.scale(block_surf, (64, 64)), "BLOCK"
        wait = False
    if who == "player":
        for i in range(40):
            fight_stage()
            draw_player((WIDTH / 2 + i * 2 - 96, HEIGHT / 2 - 20 + abs(20-i)), wears[0][2], wears[1][2], wears[2][2], 2)
            screen.blit(opponent_surface, (WIDTH / 2 + 32, HEIGHT / 2))
            info_panel()
            clock.tick(180)
            pygame.display.update()
        screen.blit(surf, (WIDTH / 2 + 32, HEIGHT / 2 - 64))
        printer(text, (WIDTH / 2 - 25, HEIGHT / 2 + 90), highlighted_font, "white")
        info_panel()
        pygame.display.update()
        if action == "block":
            block_sound.play()
        pygame.time.wait(600)
    elif who == "monster":
        for i in range(40):
            fight_stage()
            draw_player((WIDTH / 2 - 96, HEIGHT / 2), wears[0][2], wears[1][2], wears[2][2], 2)
            screen.blit(opponent_surface, (WIDTH / 2 - i * 2 + 32, HEIGHT / 2 - 20 + abs(20-i)))
            info_panel()
            clock.tick(180)
            pygame.display.update()
        screen.blit(surf, (WIDTH / 2 - 96, HEIGHT / 2 - 64))
        printer(text, (WIDTH / 2 - 25, HEIGHT / 2 + 90), highlighted_font, "white")
        info_panel()
        clock.tick(60)
        pygame.display.update()
        if action == "block":
            block_sound.play()
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
                text, rgb = "ATK power", (192, 0, 0)
            else:
                text, rgb = "DEF power ", (0, 192, 0)
            pygame.draw.rect(screen, "black", (WIDTH / 2 - 96, HEIGHT / 2 + 64, 192, 24))
            pygame.draw.rect(screen, rgb, (WIDTH / 2 - 1, HEIGHT / 2 + 64, (value / 304) * 96, 24))
            pygame.draw.rect(screen, rgb, (WIDTH / 2 - (value / 304) * 96, HEIGHT / 2 + 64, (value / 304) * 96, 24))
            printer(text, (WIDTH / 2 - 45, HEIGHT / 2 + 90), highlighted_font, "white")
            pygame.draw.rect(screen, rgb, (WIDTH / 2 - 96, HEIGHT / 2 + 64, 192, 24), 2)
            clock.tick(60)
            pygame.display.update()

            for fight_event in pygame.event.get():
                if fight_event.type == pygame.QUIT:
                    pygame.quit()
                if fight_event.type == pygame.KEYDOWN:
                    if fight_event.key == pygame.K_SPACE:
                        if action == "hit":
                            return value / 304  # factor (between 0 - 1)


def well():
    global darkness, player_hp, player_gold
    chest_text = (f"A map, in cost of {int(player_hp * 0.9)}HP. If you lost a fight, the map will disappear.",
                  f"Heal for full HP (+{player_max_hp - player_hp}HP).",
                  f"A purse with {int(2.2 ** maze_level) * 15} gold.")
    done = False
    selected = 0
    while not done:
        info_panel()
        pygame.draw.rect(screen, "grey30", (0, tile_size, WIDTH, 4 * tile_size))
        pygame.draw.rect(screen, "black", (0, tile_size, WIDTH, 4 * tile_size), 3)
        printer("I am a Wishing Well. Tell me what you desire:", (WIDTH / 2, tile_size * 2 - 13),
                prologue_font, "black", "center")
        for count, text in enumerate(chest_text):
            if count == selected:
                font, col = highlighted_font, "green"
            else:
                font, col = normal_font, "white"
            printer(text, (WIDTH / 2, tile_size * (3 + count) - 13), font, col, "center")
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
                        win_sound.play()
                        darkness = False
                        player_hp -= int(player_hp * 0.9)
                    elif selected == 1:
                        player_hp = player_max_hp
                        health_sound.play()
                    else:
                        player_gold += int(2.1 ** maze_level) * 30
                        coin_sound.play()
                    done = True
        pygame.display.update()


def transition():
    transit_sound.play()
    text = (poem_text[2 * maze_level - 2], poem_text[2 * maze_level - 1])
    for i in range(256):
        pygame.draw.rect(screen, "black", (0, 0, WIDTH, HEIGHT + info_panel_height))
        for number, sentence in enumerate(text):
            printer(sentence, (WIDTH / 2 + 2, HEIGHT / 2 + 55 * number ), menu_font, (i/2, i/2, i/2), "center")
            printer(sentence, (WIDTH / 2, HEIGHT / 2 + 55 * number), menu_font, (i, 0, 0), "center")
        pygame.display.update()
        clock.tick(35)


def finish():
    pygame.mixer.music.load("sounds/ending.wav")
    pygame.mixer.music.play(-1)
    length = len(poem_text)
    run = True
    counter = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
        for x in range(dimension):
            for y in range(dimension + 1):
                place = (x * tile_size, y * tile_size)
                screen.blit(tile_surf, place)
        finish_rect = finish_surf.get_rect(topleft=(0, 4 * tile_size))
        info_surf = menu_font.render("Press SPACE to end", True, "black")
        info_rect = info_surf.get_rect(center=(WIDTH / 2, 562))
        screen.blit(finish_surf, finish_rect)
        for i in range(length):
            printer(poem_text[i], (40, 510 - int(counter) + 35 * (i + i // 4)), prologue_font, "black")
            printer(poem_text[i], (37, 508 - int(counter) + 35 * (i + i // 4)), prologue_font, "red")
        for x in range(dimension):
            for y in range(4):
                place = (x * tile_size, y * tile_size)
                screen.blit(tile_surf, place)
        for x in range(dimension):
            for y in range(15, 20):
                place = (x * tile_size, y * tile_size)
                screen.blit(tile_surf, place)
        screen.blit(info_surf, info_rect)
        pygame.display.update()
        counter += 0.2
        if counter > 1500:
            counter = 1500
        clock.tick(60)
    pygame.draw.rect(screen, "black", (0, 0, WIDTH, HEIGHT + info_panel_height))
    pygame.display.update()
    pygame.mixer_music.fadeout(2000)
    pygame.time.wait(2000)


main_menu()

maze = maze_generator()
quest = choice(quests)
quest_item_quantity = int(randrange(4, 7) + maze_level)
shop_list = new_shop_list()
monster_atk = int(gears[maze_level + 10][1][3] * 0.85)  # 85% of player DEF (when not bought new gear yet in the shop)
monster_def = int(gears[maze_level - 1][1][1] * 0.85)  # 85% of player ATK
monster_dmg = int(gears[maze_level + 21][1][4] * 0.35)  # 35% of player HP
monster_hp = int(gears[maze_level - 1][1][2] * 0.85)  # 85% of player DMG (one good hit can kill)
boss_atk = gears[maze_level + 11][1][3]  # equal with player DEF (when already bought new gear in the shop)
boss_def = gears[maze_level][1][1]  # equal with player ATK
boss_dmg = int(gears[maze_level + 22][1][4] * 0.45)  # 45 of player HP
boss_max_hp = int(gears[maze_level][1][2] * 2.2)  # 220% of player DMG (min 3 good hit to defeat boss)
boss_hp = boss_max_hp
pygame.mixer.music.load("sounds/bg_sound.wav")
pygame.mixer.music.play(-1)
update_attributes()
for y in range(1, dimension - 1, 2):
    if maze[0][y] == "entrance":
        player_position = [0, y]
        break
transition()
new_level_sound.play()
maze_fade_in()

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
                choice((step0_sound, step1_sound)).play()
            elif event.key == pygame.K_RIGHT:
                if maze[player_position[0]][player_position[1]] == "entrance":
                    grid_slam_sound.play()
                if maze[player_position[0]][player_position[1]] == "exit":
                    maze_fade_out()
                    maze_level += 1
                    if maze_level == 11:
                        maze_level = 1
                        finish()
                        main_menu()
                        pygame.mixer.music.load("sounds/bg_sound.wav")
                        pygame.mixer.music.play(-1)
                    transition()
                    maze = maze_generator()
                    darkness = True
                    new_level_sound.play()
                    maze_fade_in()
                    boss_defeated = False
                    quest_state = "not in progress"
                    quest = choice(quests)
                    quest_item_quantity = int(randrange(4, 7) + maze_level)
                    shop_list = new_shop_list()
                    monster_atk = int(gears[maze_level + 10][1][3] * 0.85)
                    monster_def = int(gears[maze_level - 1][1][1] * 0.85)
                    monster_dmg = int(gears[maze_level + 21][1][4] * 0.35)
                    monster_hp = int(gears[maze_level - 1][1][2] * 0.85)
                    boss_atk = gears[maze_level + 11][1][3]
                    boss_def = gears[maze_level][1][1]
                    boss_dmg = int(gears[maze_level + 22][1][4] * 0.45)
                    boss_max_hp = int(gears[maze_level][1][2] * 2.2)
                    boss_hp = boss_max_hp
                    for y in range(1, dimension - 1, 2):
                        if maze[0][y] == "entrance":
                            player_position = [0, y]
                            break
                elif maze[player_position[0] + 1][player_position[1]] not in ("wall", "exit"):
                    player_position[0] += 1
                    choice((step0_sound, step1_sound)).play()
                elif maze[player_position[0] + 1][player_position[1]] == "exit" and boss_defeated:
                    player_position[0] += 1
                    choice((step0_sound, step1_sound)).play()
            elif event.key == pygame.K_UP and maze[player_position[0]][player_position[1] - 1] != "wall":
                player_position[1] -= 1
                choice((step0_sound, step1_sound)).play()
            elif event.key == pygame.K_DOWN and maze[player_position[0]][player_position[1] + 1] != "wall":
                player_position[1] += 1
                choice((step0_sound, step1_sound)).play()
            elif event.key == pygame.K_SPACE and maze[player_position[0]][player_position[1]] == "shop":
                shopping()
            elif event.key == pygame.K_SPACE and maze[player_position[0]][player_position[1]] == "boss":
                maze[player_position[0]][player_position[1]] = "boss fight"
                result = monster_fight()
                if result == "win":
                    boss_defeated = True
                    maze[player_position[0]][player_position[1]] = "room"
                    grid_open_sound.play()
                else:
                    maze[player_position[0]][player_position[1]] = "boss"
                    darkness = True
                    search = True
                    while search:
                        random_x = randrange(1, dimension - 1)
                        random_y = randrange(1, dimension - 1)
                        if maze[random_x][random_y] == "room":
                            player_position = [random_x, random_y]
                            search = False
                    wake_up_sound.play()
                    for i in range(256):
                        draw_map()
                        draw_player(
                            (player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                            wears[0][2], wears[1][2], wears[2][2], 1)
                        draw_rect_alpha(screen, (0, 0, 0, 255 - i), (0, 0, WIDTH, HEIGHT + info_panel_height))
                        pygame.display.update()
                        clock.tick(60)
            update_map()

    draw_map()
    draw_player((player_position[0] * tile_size, player_position[1] * tile_size + info_panel_height),
                wears[0][2], wears[1][2], wears[2][2], 1)
    info_panel()
    update_attributes()
    pygame.display.update()
    clock.tick(60)
