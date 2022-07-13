from random import choice, randrange
import PySimpleGUI as Psg

Psg.theme("DarkGray1")
dimension = 15  # must be odd!
entrance_point = (0, dimension - 2)
exit_point = (dimension - 1, 1)
compass = ("W", "N", "E", "S")
player_position = list(entrance_point)
player_direction = 2  # compass - "E"
tile_size = 25
window_size = dimension * tile_size
monster_rate = 10
coin_rate = 4
monster_counter = 0
coin_counter = 0
regen = False

field = Psg.Graph(
    canvas_size=(window_size, window_size),
    graph_bottom_left=(0, 0),
    graph_top_right=(window_size, window_size),
    background_color="Gray20")


def labyrinth_generation():
    matrix = []
    row = []
    for y in range(dimension):
        for x in range(dimension):
            row.append("wall")
        matrix.append(row)
        row = []

    matrix[entrance_point[1]][entrance_point[0]] = "room"
    matrix[exit_point[1]][exit_point[0]] = "room"

    start_point = (entrance_point[0] + 1, entrance_point[1])
    moves = ["up", "down", "left", "right"]
    current_point = list(start_point)
    while matrix[start_point[1]][start_point[0]] != "room":
        possible_moves = list(moves)

        if current_point[1] == 1:  # upper edge check
            possible_moves.remove("up")
        elif matrix[current_point[1] - 2][current_point[0]] != "wall":
            possible_moves.remove("up")

        if current_point[1] == dimension - 2:  # lower edge heck
            possible_moves.remove("down")
        elif matrix[current_point[1] + 2][current_point[0]] != "wall":
            possible_moves.remove("down")

        if current_point[0] == 1:  # left edge check
            possible_moves.remove("left")
        elif matrix[current_point[1]][current_point[0] - 2] != "wall":
            possible_moves.remove("left")

        if current_point[0] == dimension - 2:  # right edge check
            possible_moves.remove("right")
        elif matrix[current_point[1]][current_point[0] + 2] != "wall":
            possible_moves.remove("right")

        if not possible_moves:
            matrix[current_point[1]][current_point[0]] = "room"
            if matrix[current_point[1] - 1][current_point[0]] == "visited":
                matrix[current_point[1] - 1][current_point[0]] = "room"
                current_point[1] -= 2
            elif matrix[current_point[1] + 1][current_point[0]] == "visited":
                matrix[current_point[1] + 1][current_point[0]] = "room"
                current_point[1] += 2
            elif matrix[current_point[1]][current_point[0] - 1] == "visited":
                matrix[current_point[1]][current_point[0] - 1] = "room"
                current_point[0] -= 2
            elif matrix[current_point[1]][current_point[0] + 1] == "visited":
                matrix[current_point[1]][current_point[0] + 1] = "room"
                current_point[0] += 2
        else:
            matrix[current_point[1]][current_point[0]] = "visited"
            direction = choice(possible_moves)
            if direction == "up":
                matrix[current_point[1] - 1][current_point[0]] = "visited"
                current_point[1] -= 2
            if direction == "down":
                matrix[current_point[1] + 1][current_point[0]] = "visited"
                current_point[1] += 2
            if direction == "left":
                matrix[current_point[1]][current_point[0] - 1] = "visited"
                current_point[0] -= 2
            if direction == "right":
                matrix[current_point[1]][current_point[0] + 1] = "visited"
                current_point[0] += 2
    for y in range(1, dimension-1):
        for x in range(1, dimension-1):
            if matrix[y][x] == "room":
                if not randrange(int(100/monster_rate)):
                    matrix[y][x] = "monster"
                elif not randrange(int(100 / coin_rate)):
                    matrix[y][x] = "coin"
    matrix[entrance_point[1]][entrance_point[0]] = "entrance"
    matrix[exit_point[1]][exit_point[0]] = "exit"

    return matrix


def draw_map():
    for y in range(dimension):
        for x in range(dimension):
            field.DrawImage(filename="pictures/fog.png", location=(x * tile_size, (y + 1) * tile_size))


def draw_tile(x, y):
    if updated_labyrinth[y][x] == "wall":
        field.DrawImage(filename="pictures/wall.png", location=(x * tile_size, (y + 1) * tile_size))
    else:
        field.DrawImage(filename="pictures/tile.png", location=(x * tile_size, (y + 1) * tile_size))
        if updated_labyrinth[y][x] == "entrance":
            field.DrawImage(filename="pictures/door_closed.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "exit":
            field.DrawImage(filename="pictures/door_opened.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "W":
            field.DrawImage(filename="pictures/player_west.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "N":
            field.DrawImage(filename="pictures/player_north.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "E":
            field.DrawImage(filename="pictures/player_east.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "S":
            field.DrawImage(filename="pictures/player_south.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "coin":
            field.DrawImage(filename="pictures/coin.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_labyrinth[y][x] == "monster":
            field.DrawImage(filename="pictures/spider.png", location=(x * tile_size, (y + 1) * tile_size))


def update_map():
    global monster_counter, coin_counter
    if generated_labyrinth[player_position[1]][player_position[0]] == "monster":
        monster_counter += 1
        window["-MONSTERS-"].update(f"Monsters = {monster_counter}")
        generated_labyrinth[player_position[1]][player_position[0]] = "room"
    if generated_labyrinth[player_position[1]][player_position[0]] == "coin":
        coin_counter += 1
        window["-COINS-"].update(f"Coins = {coin_counter}")
        generated_labyrinth[player_position[1]][player_position[0]] = "room"
    draw_tile(player_position[0], player_position[1])
    draw_tile(player_position[0], player_position[1] + 1)
    draw_tile(player_position[0], player_position[1] - 1)
    if player_position[0] == 0:
        draw_tile(player_position[0] + 1, player_position[1])
        draw_tile(player_position[0] + 1, player_position[1] + 1)
        draw_tile(player_position[0] + 1, player_position[1] - 1)
    elif player_position[0] == dimension-1:
        draw_tile(player_position[0], player_position[1])
        draw_tile(player_position[0] - 1, player_position[1])
    else:
        draw_tile(player_position[0], player_position[1])
        draw_tile(player_position[0], player_position[1] + 1)
        draw_tile(player_position[0], player_position[1] - 1)
        draw_tile(player_position[0] + 1, player_position[1])
        draw_tile(player_position[0] + 1, player_position[1] + 1)
        draw_tile(player_position[0] + 1, player_position[1] - 1)
        draw_tile(player_position[0] - 1, player_position[1])
        draw_tile(player_position[0] - 1, player_position[1] + 1)
        draw_tile(player_position[0] - 1, player_position[1] - 1)


generated_labyrinth = labyrinth_generation()
updated_labyrinth = [a[:] for a in generated_labyrinth]  # deepcopy
updated_labyrinth[player_position[1]][player_position[0]] = compass[player_direction]

layout = [[field],
          [Psg.Text(f"Coins = {coin_counter}", key="-COINS-")],
          [Psg.Text(f"Monsters = {monster_counter}", key="-MONSTERS-")]]
window = Psg.Window("Maze", layout, font="Courier", return_keyboard_events=True)
timeout = 10

while True:
    event, values = window.read(timeout=timeout)
    if timeout:
        draw_map()
        update_map()
        timeout = None

    if event == Psg.WIN_CLOSED:
        break

    if event == "Left:37":
        player_direction -= 1
        if player_direction == -1:
            player_direction = 3
    if event == "Right:39":
        player_direction += 1
        if player_direction == 4:
            player_direction = 0
    if event == "Up:38":
        if compass[player_direction] == "N" and \
                generated_labyrinth[player_position[1]+1][player_position[0]] in ("room", "coin", "monster"):
            player_position[1] += 1
        elif compass[player_direction] == "W" and \
                generated_labyrinth[player_position[1]][player_position[0]-1] in ("room", "coin", "monster"):
            player_position[0] -= 1
        elif compass[player_direction] == "S" and \
                generated_labyrinth[player_position[1]-1][player_position[0]] in ("room", "coin", "monster"):
            player_position[1] -= 1
        elif compass[player_direction] == "E":
            if player_position[0] + 1 == dimension:
                player_position = list(entrance_point)
                player_direction = 2
                generated_labyrinth = labyrinth_generation()
                regen = True
            elif generated_labyrinth[player_position[1]][player_position[0]+1] \
                    in ("room", "coin", "monster", "exit"):
                player_position[0] += 1

    updated_labyrinth = [a[:] for a in generated_labyrinth]  # deepcopy
    updated_labyrinth[player_position[1]][player_position[0]] = compass[player_direction]
    if regen:
        draw_map()
        update_map()
        regen = False
    else:
        update_map()

window.close()
