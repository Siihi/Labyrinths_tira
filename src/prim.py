import random
from datetime import datetime
import maze

class Prim:
    def __init__(self, xcoord, ycoord):
        """Responsible for initiating all the needed components for Prim's algorithm.

        Args:
            xcoord: Width of the maze
            ycoord: Height of the maze
        """
        self.ycoord = ycoord
        self.xcoord = xcoord

        self.generate_maze()

        coords = self.randomized_start()
        self.generate_start(coords[0], coords[1])

        #Start of Prim's algorithm.
        self.prims_algorithm()

    def generate_maze(self):
        """Responsible for generating the base of the maze with the use of Maze().
        """
        self.commands = maze.Maze()

        self.maze = self.commands.setmaze(self.xcoord, self.ycoord)
        self.walls = []

    def randomized_start(self):
        """Responsible for randomizing the starting point of the maze.

        Returns:
            The starting coordinates.
        """
        start_y = random.randint(0, self.ycoord-1)
        start_x = random.randint(0, self.xcoord-1)

        if start_y == 0:
            start_y += 1
        if start_y == self.ycoord-1:
            start_y -= 1

        if start_x == 0:
            start_x += 1
        if start_x == self.xcoord-1:
            start_x -= 1
        return (start_y, start_x)


    def generate_start(self, start_y, start_x):
        """Responsible for marking the starting point and the first neighbours.

        Args:
            start_y: y-coordinate
            start_x: x-coordinate
        """
        self.maze[start_y][start_x] = "x"

        self.walls.append([start_y-1, start_x])
        self.maze[start_y-1][start_x] = "|"

        self.walls.append([start_y+1, start_x])
        self.maze[start_y+1][start_x] = "|"

        self.walls.append([start_y, start_x-1])
        self.maze[start_y][start_x-1] = "|"

        self.walls.append([start_y, start_x+1])
        self.maze[start_y][start_x+1] = "|"

    def nearby_maze(self, wall):
        """Responsible for marking the amount of nearby paths.

        Args:
            wall: The current cell.

        Returns:
            The amount of nearby paths.
        """
        n_maze = 0
        if self.maze[wall[0]-1][wall[1]] == "x":
            n_maze += 1
        if self.maze[wall[0]+1][wall[1]] == "x":
            n_maze += 1
        if self.maze[wall[0]][wall[1]-1] == "x":
            n_maze += 1
        if self.maze[wall[0]][wall[1]+1] == "x":
            n_maze += 1
        return n_maze

    def new_walls(self, wall):
        """Responsible for adding new neighbours to the list.

        Args:
            wall: The current cell.
        """
        #Up
        if wall[0] != 0:
            if self.maze[wall[0]-1][wall[1]] != "x":
                self.maze[wall[0]-1][wall[1]] = "|"
            if [wall[0]-1, wall[1]] not in self.walls:
                self.walls.append([wall[0]-1, wall[1]])
        #Down
        if wall[0] != self.ycoord-1:
            if self.maze[wall[0]+1][wall[1]] != "x":
                self.maze[wall[0]+1][wall[1]] = "|"
            if [wall[0]+1, wall[1]] not in self.walls:
                self.walls.append([wall[0]+1, wall[1]])
        #Right
        if wall[1] != self.xcoord-1:
            if self.maze[wall[0]][wall[1]+1] != "x":
                self.maze[wall[0]][wall[1]+1] = "|"
            if [wall[0], wall[1]+1] not in self.walls:
                self.walls.append([wall[0], wall[1]+1])
        #Left
        if wall[1] != 0:
            if self.maze[wall[0]][wall[1]-1] != "x":
                self.maze[wall[0]][wall[1]-1] = "|"
            if [wall[0], wall[1]-1] not in self.walls:
                self.walls.append([wall[0], wall[1]-1])

    def delete_walls(self, wall):
        """Responsible for deleting a cell from the neighbours list.

        Args:
            wall: The cell being removed.

        Returns:
            True if the cell was found, otherwise False.
        """
        for i in self.walls:
            if i[0] == wall[0] and i[1] == wall[1]:
                self.walls.remove(i)
                return True
        return False

    def prims_algorithm(self):
        """Responsible for generating the maze with the use of Prim's algorithm."""
        #Checking if there's walls left and picking one of the walls at random.
        start_time = datetime.now()
        while self.walls:
            wall = self.walls[(random.randint(0, len(self.walls)))-1]

            #Checking that picked wall is applicable.
            #Checking for an upper wall.
            if wall[0] != 0:
                if self.maze[wall[0]-1][wall[1]] == "o" and self.maze[wall[0]+1][wall[1]] == "x":
                    n_maze = self.nearby_maze(wall)
                    if n_maze < 2:
                        self.maze[wall[0]][wall[1]] = "x"
                        self.new_walls(wall)
                        self.delete_walls(wall)

            #Checking for a bottom wall.
            if wall[0] != self.ycoord-1:
                if self.maze[wall[0]+1][wall[1]] == "o" and self.maze[wall[0]-1][wall[1]] == "x":
                    n_maze = self.nearby_maze(wall)
                    if n_maze < 2:
                        self.maze[wall[0]][wall[1]] = "x"
                        self.new_walls(wall)
                        self.delete_walls(wall)

            #Checking for a left wall.
            if wall[1] != 0:
                if self.maze[wall[0]][wall[1]-1] == "o" and self.maze[wall[0]][wall[1]+1] == "x":
                    n_maze = self.nearby_maze(wall)
                    if n_maze < 2:
                        self.maze[wall[0]][wall[1]] = "x"
                        self.new_walls(wall)
                        self.delete_walls(wall)

            #Checking for a right wall.
            if wall[1] != self.xcoord-1:
                if self.maze[wall[0]][wall[1]+1] == "o" and self.maze[wall[0]][wall[1]-1] == "x":
                    n_maze = self.nearby_maze(wall)
                    if n_maze < 2:
                        self.maze[wall[0]][wall[1]] = "x"
                        self.new_walls(wall)
                        self.delete_walls(wall)

            #Delete wall.
            self.delete_walls(wall)

        #Marking remaining "o" as walls.
        for i in range(0, self.ycoord):
            for j in range(0, self.xcoord):
                if self.maze[i][j] == "o":
                    self.maze[i][j] = "|"

        stop_time = datetime.now()
        self.time_taken = (stop_time - start_time).total_seconds()

        self.commands.printmaze(self.maze)
        return self.maze

    def __str__(self):
        """Responsible for returning the time taken for the maze to be generated.

        Returns:
            Time taken for generating the maze.
        """
        return str(self.time_taken)

