import random
import maze

class AldousBroder:
    def __init__(self, xcoord, ycoord):
        self.ycoord = ycoord
        self.xcoord = xcoord

        self.generate_maze()

        coords = self.randomized_start()
        self.generate_start(coords[0], coords[1])

        self.aldous_broder()

    def generate_maze(self):
        #The base of the maze is generated with the use of Maze().
        self.commands = maze.Maze()

        self.maze = self.commands.setmaze(self.xcoord, self.ycoord)
        self.mazeleft = (self.xcoord-1)*(self.ycoord-1) -1

    def randomized_start(self):
        start_y = random.randint(0, self.ycoord-1)
        start_x = random.randint(0, self.xcoord-1)

        if start_y == 0:
            start_y += 1
            if start_y % 2 == 0:
                start_y +=1
        if start_y == self.ycoord-1:
            start_y -= 1
            if start_y % 2 == 0:
                start_y -=1

        if start_x == 0:
            start_x += 1
            if start_x % 2 == 0:
                start_x +=1
        if start_x == self.xcoord-1:
            start_x -= 1
            if start_x % 2 == 0:
                start_x -=1


        return (start_y, start_x)

    def generate_start(self, start_y, start_x):
        #The start point of the maze is marked as part of the routes
        #and the tiles next to it are marked as walls temporarily.
        self.maze[start_y][start_x] = "x"
        self.start = [start_y, start_x]

    def aldous_broder(self):
        nextwall = self.start
        directions = ["up", "right", "left", "down"]

        while self.mazeleft >= 0:
            nextdir = random.choice(directions)

            if nextdir == "up":
                if nextwall[0]-2 != 0 and nextwall[0]-1 != 0:
                    nextwall = [nextwall[0]-2, nextwall[1]]
                    if self.maze[nextwall[0]][nextwall[1]] == "o":
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.maze[nextwall[0]+1][nextwall[1]] = "x"
                        self.mazeleft -= 1

            elif nextdir == "down":
                if nextwall[0]+2 != self.ycoord-1 and nextwall[0]+1 != self.ycoord-1:
                    nextwall = [nextwall[0]+2, nextwall[1]]
                    if self.maze[nextwall[0]][nextwall[1]] == "o":
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.maze[nextwall[0]-1][nextwall[1]] = "x"
                        self.mazeleft -= 1

            elif nextdir == "left":
                if nextwall[1]-2 != 0 and nextwall[1]-1 != 0:
                    nextwall = [nextwall[0], nextwall[1]-2]
                    if self.maze[nextwall[0]][nextwall[1]] == "o":
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.maze[nextwall[0]][nextwall[1]+1] = "x"
                        self.mazeleft -= 1

            elif nextdir == "right":
                if nextwall[1]+2 != self.xcoord-1 and nextwall[1]+1 != self.xcoord-1:
                    nextwall = [nextwall[0], nextwall[1]+2]
                    if self.maze[nextwall[0]][nextwall[1]] == "o":
                        self.maze[nextwall[0]][nextwall[1]] = "x"
                        self.maze[nextwall[0]][nextwall[1]-1] = "x"
                        self.mazeleft -= 1

            else:
                continue

        self.commands.printmaze(self.maze)
        return True

if __name__ == "__main__":
    AldousBroder(10,10)
