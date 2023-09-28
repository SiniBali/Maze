from random import choice, randrange
from data import *


def maze_generator():
    entrance_door_position = (0, randrange(1, dimension - 1, 2))
    exit_door_position = (dimension - 1, randrange(1, dimension - 1, 2))
    matrix = []
    row = []
    for x in range(dimension):
        for y in range(dimension):
            row.append("wall")  # walls everywhere
        matrix.append(row)
        row = []
    starting_cell_x = entrance_door_position[0] + 1
    starting_cell_y = entrance_door_position[1]
    adjacent = [(starting_cell_x + 2, starting_cell_y)]
    if starting_cell_y != 1:
        adjacent.append((starting_cell_x, starting_cell_y - 2))
    if starting_cell_y != dimension - 2:
        adjacent.append((starting_cell_x, starting_cell_y + 2))
    matrix[starting_cell_x][starting_cell_y] = "room"
    while adjacent:
        new_room = choice(adjacent)
        matrix[new_room[0]][new_room[1]] = "room"
        neighbor_rooms = []
        if new_room[1] < dimension - 2:
            if matrix[new_room[0]][new_room[1] + 2] == "room":
                neighbor_rooms.append("up")
        if new_room[1] > 1:
            if matrix[new_room[0]][new_room[1] - 2] == "room":
                neighbor_rooms.append("down")
        if new_room[0] > 1:
            if matrix[new_room[0] - 2][new_room[1]] == "room":
                neighbor_rooms.append("left")
        if new_room[0] < dimension - 2:
            if matrix[new_room[0] + 2][new_room[1]] == "room":
                neighbor_rooms.append("right")
        if neighbor_rooms:
            carving_direction = choice(neighbor_rooms)
            if carving_direction == "up":
                matrix[new_room[0]][new_room[1] + 1] = "room"
            elif carving_direction == "down":
                matrix[new_room[0]][new_room[1] - 1] = "room"
            elif carving_direction == "left":
                matrix[new_room[0] - 1][new_room[1]] = "room"
            elif carving_direction == "right":
                matrix[new_room[0] + 1][new_room[1]] = "room"
        adjacent.remove((new_room[0], new_room[1]))
        if new_room[1] < dimension - 2:
            if matrix[new_room[0]][new_room[1] + 2] == "wall" and (new_room[0], new_room[1] + 2) not in adjacent:
                adjacent.append((new_room[0], new_room[1] + 2))
        if new_room[1] > 1:
            if matrix[new_room[0]][new_room[1] - 2] == "wall" and (new_room[0], new_room[1] - 2) not in adjacent:
                adjacent.append((new_room[0], new_room[1] - 2))
        if new_room[0] > 1:
            if matrix[new_room[0] - 2][new_room[1]] == "wall" and (new_room[0] - 2, new_room[1]) not in adjacent:
                adjacent.append((new_room[0] - 2, new_room[1]))
        if new_room[0] < dimension - 2:
            if matrix[new_room[0] + 2][new_room[1]] == "wall" and (new_room[0] + 2, new_room[1]) not in adjacent:
                adjacent.append((new_room[0] + 2, new_room[1]))
    matrix[entrance_door_position[0]][entrance_door_position[1]] = "entrance"
    matrix[exit_door_position[0]][exit_door_position[1]] = "exit"

    return matrix
