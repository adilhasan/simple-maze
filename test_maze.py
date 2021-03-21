import unittest
import maze


def test_read_maze():
    """
    GIVEN an a maze string as input
    WHEN the maze is read in
    THEN the list of maze lines is returned
    """
    input_maze = "#####\n#o #\n#  ##\n#  x#\n#####"
    maze_lines = ["#####","#o #", "#  ##", "#  x#", "#####"]
    lines = maze.get_maze(input_maze)
    assert lines == maze_lines


def test_maze_island():
    """
    GIVEN a maze string as input
    WHEN the maze is read in and contains an island
    THEN the program returns false
    """
    input_maze = ["#####", "# #o#", "# x #", "##  #", "#####"]
    assert maze.is_island(input_maze)


def test_start():
    """
    GIVEN a maze as input
    WHEN we find the 'o' character
    THEN we return the start row and column
    """
    start = (1, 3)
    input_maze = ["#####", "# #o#", "#  x#", "##  #", "#####"]
    start_coords = maze.get_start(input_maze)
    assert start_coords == start


def test_move_left_valid():
    """
    GIVEN a maze as input
    WHEN there are valid moves left
    THEN advance the coords to the left as far as possible
    """
    maze_list = ["##   #", "######"]
    input_coord = (0, 5)
    coord = maze.advance_horizontal(input_coord, maze_list, step=-1)
    assert coord == (0, 2)


def test_move_right_valid():
    """
    GIVEN a maze as input
    WHEN there are valid moves right
    THEN advance the coords to the right as far as possible
    """
    maze_list = ["######", "##   #"]
    input_coord = (1, 2)
    coord = maze.advance_horizontal(input_coord, maze_list, step=+1)
    assert coord == (1, 4)


def test_move_up_valid():
    """
    GIVEN a maze as input
    WHEN there is a valid move up
    THEN advance the coords up as far as possible
    """
    maze_list = ["##", "# ", "# ", "# ", "##"]
    input_coord = (3, 1)
    coord = maze.advance_vertical(input_coord, maze_list, step=-1)
    assert coord == (1,1)


def test_move_down():
    """
    GIVEN a maze as input
    WHEN there is a valid move down
    THEN advance the coords down as far as possible
    """
    maze_list = ["##", " #", " #", " #", " #", " #", "##"]
    input_coord = (1, 0)
    coord = maze.advance_vertical(input_coord, maze_list, step=+1)
    assert coord == (5, 0)


def test_solve_maze():
    """
    GIVEN a maze as input
    WHEN there is a valid move
    THEN advance until the exit is reached
    """
    input_maze = ["#####", "#o  #", "### #", "#x  #", "#####"]
    coord, dummy = maze.solve(input_maze)
    assert coord == (3, 1)


def test_no_solution_maze():
    """
    GIVEN a maze as input
    WHEN there is no valid move
    THEN respond that it's insoluble
    """
    input_maze = ["#####", "#o  #", "#####", "#x  #", "#####"]
    dummy, insoluble = maze.solve(input_maze)
    assert insoluble