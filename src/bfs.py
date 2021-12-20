from maze import Maze

class BreadthFirstSearch:
    def __init__(self, maze):
        """Responsible for initiating all the needed components for breadth-first search.

        Args:
            maze: The maze that will be checked
        """
        self.amount = 0
        self.nearby = []
        self.visited = []
        self.compare = maze
        self.compamount = 0
        for row in range(len(maze)):
            for cell in range(len(maze[1])):
                if self.compare[row][cell] == "x":
                    self.compamount += 1

        self.bfs()

    def select_start(self, start_y, start_x):
        """Responsible for selecting a starting point in the maze.

        Args:
            start_y: y-coordinate
            start_x: x-coordinate
        """
        if self.compare[start_y][start_x] == "|":
            start_y += 1
            start_x += 1
        else:
            self.nearby.append((start_y, start_x))

    def find_nearby(self, cell):
        """Responsible for finding nearby cells that have not been visited.

        Args:
            cell: The coordinates of the current cell.
        """
        if cell[0] != 0:
            if self.compare[cell[0]-1][cell[1]] == "x":
                if (cell[0]-1,cell[1]) not in self.visited and (cell[0]-1,cell[1]) not in self.nearby:
                    self.nearby.append((cell[0]-1,cell[1]))

        if cell[0] != len(self.compare)-1:
            if self.compare[cell[0]+1][cell[1]] == "x":
                if (cell[0]+1,cell[1]) not in self.visited and (cell[0]+1,cell[1]) not in self.nearby:
                    self.nearby.append((cell[0]+1,cell[1]))

        if cell[1] != 0:
            if self.compare[cell[0]][cell[1]-1] == "x":
                if (cell[0],cell[1]-1) not in self.visited and (cell[0],cell[1]-1) not in self.nearby:
                    self.nearby.append((cell[0],cell[1]-1))

        if cell[1] != len(self.compare[0])-1:
            if self.compare[cell[0]][cell[1]+1] == "x":
                if (cell[0],cell[1]+1) not in self.visited and (cell[0],cell[1]+1) not in self.nearby:
                    self.nearby.append((cell[0],cell[1]+1))


    def bfs(self):
        """Responsible for checking the integrity of a maze using breadth-first search."""
        self.select_start(1,1)
        if len(self.nearby) == 0:
            self.select_start(2,1)
        while True:
            if self.amount == self.compamount:
                print("Checked!")
                break
            if len(self.nearby) == 0:
                print("Wrong!")
                break
            cell = self.nearby.pop(0)
            self.visited.append(cell)
            self.amount += 1
            self.find_nearby(cell)

