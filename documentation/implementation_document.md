# Implementation document

## Datastructures

The main data structure used is a matrix, which determines the paths and walls of the maze. For this I have made a list of lists, each of which contain cells. The "x"-cells denote paths, "o"-cells unvisited cells and "|"-cells walls. The idea is to go through the matrix starting at a random point and advancing through the maze using random neighbouring cells.

## Randomized Prim's algorithm

When a new cell is chosen in randomized Prim's algorithm, the two cells that the chosen cell divides are checked and if only one of them is visited the wall is made into a passage and the unvisited cell is marked as a part of the maze. Its neighboring cells are added to the neighboring cells list and the next cell is chosen.


## Aldous-Broder algorithm

TBC

## Comparison

The time complexity of randomized Prim's algorithm is O(|V|²). It takes about 0.4 seconds to make a 100 x 100 maze utilizing it.

## Flaws and improvements

Randomized Prim's algorithm could be made faster with the use of a binary heap or a fibonacci heap.
