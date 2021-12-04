class Maze:
    def setmaze(self, xcoord, ycoord):
        """Responsible for generating a set size maze.

        Args:
            x: Width of the maze.
            y: Height of the maze.

        Returns:
            The base of the maze.
        """
        maze = []
        xlist = []
        for i in range(ycoord):
            for j in range(xcoord):
                xlist.append("o")
            maze.append(xlist)
            xlist = []
        return maze

    def printmaze(self, maze):
        """Responsible for printing the maze.

        Args:
            maze: The maze that will be printed out.

        Returns:
            True, after the printing is finished.
        """
        for line in maze:
            linestr = ""
            for char in line:
                linestr += " "
                linestr += char
            print(linestr)
        return True
