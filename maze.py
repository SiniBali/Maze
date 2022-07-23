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
coin_rate = 12
monster_counter = 0
coin_counter = 0
maze_level = 1
regen = False

field = Psg.Graph(
    canvas_size=(window_size, window_size),
    graph_bottom_left=(0, 0),
    graph_top_right=(window_size, window_size),
    background_color="Gray20")


def maze_generator():
    carving_directions = ("West", "North")
    matrix = []
    row = []
    for y in range(dimension):
        for x in range(dimension):
            row.append("wall")
        matrix.append(row)
        row = []
    for y in range(1, dimension - 1, 2):
        for x in range(1, dimension - 1, 2):
            matrix[y][x] = "room"
            if x == 1 and y != dimension - 2:
                matrix[y + 1][x] = "room"
            elif y == dimension - 2 and x != 1:
                matrix[y][x-1] = "room"
            elif x == 1 and y == dimension - 2:
                pass
            else:
                if choice(carving_directions) == "West":
                    matrix[y + 1][x] = "room"
                else:
                    matrix[y][x-1] = "room"
    matrix[entrance_point[1]][entrance_point[0]] = "entrance"
    matrix[exit_point[1]][exit_point[0]] = "exit"
    for y in range(1, dimension - 1):
        for x in range(1, dimension - 1):
            if matrix[y][x] == "room":
                if not randrange(int(100 / monster_rate)):
                    matrix[y][x] = "monster"
                elif not randrange(int(100 / coin_rate)):
                    matrix[y][x] = "coin"
    return matrix


def draw_map():
    for y in range(dimension):
        for x in range(dimension):
            field.DrawImage(filename="pictures/fog.png", location=(x * tile_size, (y + 1) * tile_size))  # displays fog
            # draw_tile(x, y)  # cells without fog


def draw_tile(x, y):
    if updated_maze[y][x] == "wall":
        field.DrawImage(filename="pictures/wall.png", location=(x * tile_size, (y + 1) * tile_size))
    else:
        field.DrawImage(filename="pictures/tile.png", location=(x * tile_size, (y + 1) * tile_size))
        if updated_maze[y][x] == "entrance":
            field.DrawImage(filename="pictures/door_closed.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "exit":
            field.DrawImage(filename="pictures/door_opened.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "W":
            field.DrawImage(filename="pictures/player_west.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "N":
            field.DrawImage(filename="pictures/player_north.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "E":
            field.DrawImage(filename="pictures/player_east.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "S":
            field.DrawImage(filename="pictures/player_south.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "coin":
            field.DrawImage(filename="pictures/coin.png", location=(x * tile_size, (y + 1) * tile_size))
        elif updated_maze[y][x] == "monster":
            field.DrawImage(filename="pictures/spider.png", location=(x * tile_size, (y + 1) * tile_size))


def update_map():
    global monster_counter, coin_counter
    if generated_maze[player_position[1]][player_position[0]] == "monster":
        monster_counter += 1
        window["-MONSTERS-"].update(f"Monsters = {monster_counter}")
        generated_maze[player_position[1]][player_position[0]] = "room"
    if generated_maze[player_position[1]][player_position[0]] == "coin":
        coin_counter += 1
        window["-COINS-"].update(f"Coins = {coin_counter}")
        generated_maze[player_position[1]][player_position[0]] = "room"
    draw_tile(player_position[0], player_position[1])
    draw_tile(player_position[0], player_position[1] + 1)
    draw_tile(player_position[0], player_position[1] - 1)
    if player_position[0] == 0:
        draw_tile(player_position[0] + 1, player_position[1])
        draw_tile(player_position[0] + 1, player_position[1] + 1)
        draw_tile(player_position[0] + 1, player_position[1] - 1)
    elif player_position[0] == dimension - 1:
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


generated_maze = maze_generator()
updated_maze = [a[:] for a in generated_maze]  # deepcopy
updated_maze[player_position[1]][player_position[0]] = compass[player_direction]

layout = [[field],
          [Psg.Text(f"Coins = {coin_counter}", key="-COINS-")],
          [Psg.Text(f"Monsters = {monster_counter}", key="-MONSTERS-")],
          [Psg.Text(f"Maze level = {maze_level}", key="-LEVEL-")]]
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
                generated_maze[player_position[1] + 1][player_position[0]] in ("room", "coin", "monster"):
            player_position[1] += 1
        elif compass[player_direction] == "W" and \
                generated_maze[player_position[1]][player_position[0] - 1] in ("room", "coin", "monster"):
            player_position[0] -= 1
        elif compass[player_direction] == "S" and \
                generated_maze[player_position[1] - 1][player_position[0]] in ("room", "coin", "monster"):
            player_position[1] -= 1
        elif compass[player_direction] == "E":
            if player_position[0] + 1 == dimension:
                player_position = list(entrance_point)
                player_direction = 2
                generated_maze = maze_generator()
                regen = True
                maze_level += 1
                window["-LEVEL-"].update(f"Maze level = {maze_level}")
            elif generated_maze[player_position[1]][player_position[0] + 1] \
                    in ("room", "coin", "monster", "exit"):
                player_position[0] += 1

    updated_maze = [a[:] for a in generated_maze]  # deepcopy
    updated_maze[player_position[1]][player_position[0]] = compass[player_direction]
    if regen:
        draw_map()
        update_map()
        regen = False
    else:
        update_map()

window.close()
