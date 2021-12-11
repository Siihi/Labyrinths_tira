# Implementation document

## Datastructures

The main data structure used is a matrix, which determines the paths and walls of the maze. For this I have made a list of lists, each of which contain cells. The "x"-cells denote paths, "o"-cells unvisited cells and "|"-cells walls. The idea is to go through the matrix starting at a random point and advancing through the maze using random neighbouring cells.

## Randomized Prim's algorithm

When a new cell is chosen in randomized Prim's algorithm, the two cells that the chosen cell divides are checked and if only one of them is visited the wall is made into a passage and the unvisited cell is marked as a part of the maze. Its neighboring cells are added to the neighboring cells list and the next cell is chosen.


## Aldous-Broder algorithm

When a new cell is chosen in the Aldous-Broder algorithm, one of the adjacent cells are chosen and if it and the cells next to it aren't visited, it is made the current cell and added to the maze as a passage. If the adjacent cell or the cells next to it have been visited, the next adjacent cell is chosen.

## Comparison

![Time comparison](https://github.com/Siihi/Labyrinths_tira/blob/main/documentation/pictures/time_comparison.jpg)

In smaller mazes the time taken is similar in both mazes. At size 50 x 50 the Aldous-Broder clearly takes a longer time at 3,3 seconds and with each increase in size, requires substantially more time with 53,2 seconds for a 200 x 200 maze.
In randomized Prim's algorithm the time taken doesn't fluctuate much compared to the Aldous-Broder, with a time of 2,3 seconds for a 200 x 200 maze. 

Thus it can be stated that the randomized Prim's algorithm is clearly the faster algorithm.

## Flaws and improvements

Randomized Prim's algorithm could be made faster with the use of a binary heap or a fibonacci heap.

Aldous-Broder algorithm cannot be made faster and it is known as one of slowest and most inefficient maze generating algorithms there is.
