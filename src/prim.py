import maze
import random

class Prim:
    def __init__(self, x, y):
        """Responsible for initiating all the needed components for Prim's algorithm.

        Args:
            x: Width of the maze
            y: Height of the maze
        """
        self.y = y
        self.x = x

        #Starting points are randomised and checked so that they are not on the edges.
        self.start_y = random.randint(0, y-1)
        self.start_x = random.randint(0, x-1)

        if self.start_y == 0:
            self.start_y += 1
        if self.start_y == y-1:
            self.start_y -= 1

        if self.start_x == 0:
            self.start_x += 1
        if self.start_x == x-1:
            self.start_x -= 1

        #The base of the maze is generated with the use of Maze().
        self.commands = maze.Maze()
    
        self.maze = self.commands.setmaze(x, y)
        self.walls = []

        #The start point of the maze is marked as part of the routes and the tiles next to it are marked as walls temporarily.
        self.maze[self.start_y][self.start_x] = "x"

        self.walls.append([self.start_y-1, self.start_x])
        self.maze[self.start_y-1][self.start_x] = "|"

        self.walls.append([self.start_y+1, self.start_x])
        self.maze[self.start_y+1][self.start_x] = "|"
        
        self.walls.append([self.start_y, self.start_x-1])
        self.maze[self.start_y][self.start_x-1] = "|"

        self.walls.append([self.start_y, self.start_x+1])
        self.maze[self.start_y][self.start_x+1] = "|"
        

    def prims_algorithm(self):
        """Responsible for generating the maze with the use of Prim's algorithm."""
        #Checking if there's walls left and picking one of the walls at random.
        while self.walls is True:
            wall = self.walls[(random.randint(0, len(self.walls)))-1]

            #Checking that picked wall is applicable.
            if wall[0] != 0:
                if self.maze[wall[0]-1][wall[1]] == "o" and self.maze[wall[0]+1][wall[1]+1] == "x":
                    pass

            if wall[0] != self.y-1:
                if self.maze[wall[0]+1][wall[1]] == "o" and self.maze[wall[0]-1][wall[1]] == "x":
                    pass

            if wall[1] != 0:
                if self.maze[wall[0]][wall[1]-1] == "o" and self.maze[wall[0]][wall[1]+1] == "x":
                    pass

            if wall[1] != self.x-1:
                if self.maze[wall[0]][wall[1]+1] == "o" and self.maze[wall[0]][wall[1]-1] == "x":
                    pass



