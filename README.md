# Simple Maze Solver
This simple program attempts to solve simple mazes. The walls are defined by the character "#", the start position is given by "o" the end position by "x". 

To run the program:

python3 maze.py "#####\
\#o  #\
\#  x#\
\#####

(the number of cols should match-up the narkup doesn't show it).

There is a test program:

test_maze.py that can be run with pytest:

pytest test_maze.py

that should run tests with example mazes.