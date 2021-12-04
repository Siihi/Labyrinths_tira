import random
from datetime import datetime
import maze

class AldousBroder:
    def __init__(self, xcoord, ycoord):
        """Responsible for initiating all the needed components for the Aldous-Broder algorithm.

        Args:
            xcoord: Width of the maze
            ycoord: Height of the maze
        """
        self.ycoord = ycoord
        self.xcoord = xcoord

        self.generate_maze()

        coords = self.randomized_start()
        self.generate_start(coords[0], coords[1])

        self.aldous_broder()

    def generate_maze(self):
        """Responsible for generating the base of the maze with the use of Maze().
        """
        self.commands = maze.Maze()

        self.maze = self.commands.setmaze(self.xcoord, self.ycoord)
        self.mazeleft = (self.xcoord)*(self.ycoord) * 100

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
        """Responsible for marking the starting point in the maze.

        Args:
            start_y: y-coordinate
            start_x: x-coordinate
        """
        self.maze[start_y][start_x] = "x"
        self.start = [start_y, start_x]

    def make_walls(self, wall):
        """Responsible for marking nearby walls.

        Args:
            wall: The coordinates of the current cell.
        """
        if self.maze[wall[0]-1][wall[1]] == "o":
            self.maze[wall[0]-1][wall[1]] = "|"
        if self.maze[wall[0]+1][wall[1]] == "o":
            self.maze[wall[0]+1][wall[1]] = "|"
        if self.maze[wall[0]][wall[1]-1] == "o":
            self.maze[wall[0]][wall[1]-1] = "|"
        if self.maze[wall[0]][wall[1]+1] == "o":
            self.maze[wall[0]][wall[1]+1] = "|"

    def aldous_broder(self):
        """Responsible for generating the maze using the Aldous-Broder algorithm."""
        start_time = datetime.now()
        nextwall = self.start
        directions = ["up", "right", "left", "down"]

        while self.mazeleft >= 0:
            nextdir = random.choice(directions)

            if nextdir == "up":
                if nextwall[0]-2 != -1 and nextwall[0]-1 != 0:
                    if self.maze[nextwall[0]-2][nextwall[1]] != "x" and self.maze[nextwall[0]-1][nextwall[1]-1] != "x" and self.maze[nextwall[0]-1][nextwall[1]+1] != "x":
                        nextwall = [nextwall[0]-1, nextwall[1]]
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.make_walls(nextwall)
                        self.mazeleft -= 1
                    elif self.maze[nextwall[0]-1][nextwall[1]] == "x":
                        nextwall = [nextwall[0]-1, nextwall[1]]

            elif nextdir == "down":
                if nextwall[0]+2 != self.ycoord and nextwall[0]+1 != self.ycoord-1:
                    if self.maze[nextwall[0]+2][nextwall[1]] != "x" and self.maze[nextwall[0]+1][nextwall[1]-1] != "x" and self.maze[nextwall[0]+1][nextwall[1]+1] != "x":
                        nextwall = [nextwall[0]+1, nextwall[1]]
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.make_walls(nextwall)
                        self.mazeleft -= 1
                    elif self.maze[nextwall[0]+1][nextwall[1]] == "x":
                        nextwall = [nextwall[0]+1, nextwall[1]]

            elif nextdir == "left":
                if nextwall[1]-2 != -1 and nextwall[1]-1 != 0:
                    if self.maze[nextwall[0]][nextwall[1]-2] != "x" and self.maze[nextwall[0]-1][nextwall[1]-1] != "x" and self.maze[nextwall[0]+1][nextwall[1]-1] != "x":
                        nextwall = [nextwall[0], nextwall[1]-1]
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.make_walls(nextwall)
                        self.mazeleft -= 1
                    elif self.maze[nextwall[0]][nextwall[1]-1] == "x":
                        nextwall = [nextwall[0], nextwall[1]-1]

            elif nextdir == "right":
                if nextwall[1]+2 != self.xcoord and nextwall[1]+1 != self.xcoord-1:
                    if self.maze[nextwall[0]][nextwall[1]+2] != "x" and self.maze[nextwall[0]-1][nextwall[1]+1] != "x" and self.maze[nextwall[0]+1][nextwall[1]+1] != "x":
                        nextwall = [nextwall[0], nextwall[1]+1]
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.make_walls(nextwall)
                        self.mazeleft -= 1
                    elif self.maze[nextwall[0]][nextwall[1]+1] == "x":
                        nextwall = [nextwall[0], nextwall[1]+1]

        for i in range(0, self.ycoord):
            for j in range(0, self.xcoord):
                if self.maze[i][j] == "o":
                    self.maze[i][j] = "|"

        stop_time = datetime.now()
        self.time_taken = (stop_time - start_time).total_seconds()

        self.commands.printmaze(self.maze)
        return True

    def __str__(self):
        """Responsible for returning the time taken for the maze to be generated.

        Returns:
            Time taken for generating the maze.
        """
        return str(self.time_taken)
