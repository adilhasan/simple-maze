#!/usr/bin/env python
"""
Module to find the solution to a maze
"""
import argparse

def get_maze(input_maze):
    """
    input_maze: string containing the maze diagram.
    Splits the maze into lines and returns the list of lines
    """

    maze_lines = input_maze.split("\n")
    return maze_lines


def is_island(maze):
    """
    maze: list containing the maze diagram.
    Checks each row for characters not connected to the walls
    """

    island = False
    valid_char = ["#", "o", "x"]
    for row in maze:
        for index, col in enumerate(row):
            if col in valid_char and index > 0 and index < len(row) - 1:
                island = row[index - 1] == " " and row[index + 1] == " "
                if island:
                    break
        if island:
            break
    return island


def get_start(maze):
    """
    maze: list containing a valid maze diagram
    Finds the coords for the start position
    """
    start = "o"
    row_index = -1
    col_index = -1
    for row_index in range(0, len(maze)):
        if start in maze[row_index]:
            col_index = maze[row_index].index(start)
            break

    return (row_index, col_index)


def move(coord, maze, direction):
    """
    coord: the col, row coords of the start position
    maze: the list containing the maze diagram
    direction: in which to move: up, down, left, right
    From the coord start position move as many steps as possible
    in the direction specified.
    """
    next_coord = (-1, -1)
    if direction == "up":
        next_coord = advance_vertical(coord, maze, step=-1)
    elif direction == "down":
        next_coord = advance_vertical(coord, maze, step=+1)
    elif direction == "right":
        next_coord = advance_horizontal(coord, maze, step=+1)
    elif direction == "left":
        next_coord = advance_horizontal(coord, maze, step=-1)
    return next_coord

def advance_vertical(coord, maze, step=0):
    """
    coord: the col, row coords of the start position
    maze: the list containing the maze diagram
    step: the direction +1 is to the right and -1 to the left
    From the coord start move as many steps as possible
    up while keeping the left hand on the wall
    """
    new_pos = coord[0]
    final_coord = (-1, -1)
    stop_symbols = ["#", "o", "x"]
    while 1:
        new_pos = new_pos + step
        if maze[new_pos][coord[1]] in stop_symbols:
            break
        if maze[new_pos][coord[1] + step] == " ":
            break

    if maze[new_pos][coord[1]] == stop_symbols[2]:
        final_coord = (new_pos, coord[1])
    else:
        final_coord = (new_pos - step, coord[1])
    return final_coord


def advance_horizontal(coord, maze, step=0):
    """
    coord: the col, row coords of the start position
    maze: the list containing the maze diagram
    step: the direction in which to move +1 to the right and -1 to the left
    From the coord start position move as many steps
    as possible to the left while keeping the left hand on
    the wall
    """
    new_pos = coord[1]
    final_coord = (-1, -1)
    stop_symbols = ["#", "o", "x"]
    while 1:
        new_pos = new_pos + step
        if maze[coord[0]][new_pos] in stop_symbols:
            break
        if maze[coord[0]-step][new_pos] == " ":
            break

    if maze[coord[0]][new_pos] == stop_symbols[2]:
        final_coord = (coord[0], new_pos)
    else:
        final_coord = (coord[0], new_pos - step)
    return final_coord


def solve(maze):
    """
    maze: list containing a valid maze diagram
    Steps through the maze starting at the starting point and
    trying to move along the row from left to right. If that is
    not possible then down. If not possible then right to left, if
    that is not possible then up.
    """
    end = "x"
    end_found = False
    insoluble = False
    print("\n".join(maze))
    coord = get_start(maze)
    old_path = []
    direction = ["right", "down", "left", "up"]
    while 1:
        path = []
        for adir in direction:
            coord = move(coord, maze, adir)
            if maze[coord[0]][coord[1]] == end:
                end_found = True
                break
            path.append(coord)
        if path == old_path:
            insoluble = True
            break
        old_path = path
        if end_found:
            break
    return coord, insoluble


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find the solution to a maze.")
    parser.add_argument("maze", metavar="M", type=str, help="The maze diagram")

    args = parser.parse_args()
    maze_list = get_maze(args.maze)
    if not is_island(maze_list):
        coord, insoluble  = solve(maze_list)
        if insoluble:
            print("Maze is insoluble")
        else:
            print("Found exit at coords: ", coord)
    else:
        print("Maze is not allowed")
