# Testing document

The testing is done with automated tests using unittest.

The newest testing coverage information can be found in Codecov.

The integrity of the mazes is checked with a breadth-first search, found [here](https://github.com/Siihi/Labyrinths_tira/blob/main/src/bfs.py).

The code has a pylint score of 9.67.

## maze.py

100% tested using automated tests.

## prim.py

96% tested using automated tests.

The input used is Prim(5,5) meaning a 5 x 5 maze using randomized Prim's algorithm is generated and used for testing.

Using a breadth-first search, all the cells in the maze are accessible.

## aldous_broder.py

96% tested using automated tests.

The input used is AldousBroder(5,5) meaning a 5 x 5 maze using the Aldous-Broder algorithm is generated and used for testing.

Using a breadth-first search, all the cells in the maze are accessible.

## Testing report

The testing report can be found in codecov.

[![codecov](https://codecov.io/gh/Siihi/Labyrinths_tira/branch/main/graph/badge.svg?token=5YRqisc03R)](https://codecov.io/gh/Siihi/Labyrinths_tira)
