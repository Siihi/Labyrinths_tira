# pylint: skip-file

import unittest
import maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = maze.Maze()

    def test_maze_formed_correctly(self):
        self.assertEqual(self.maze.setmaze(2,2), [['o', 'o'], ['o', 'o']])

    def test_maze_printed_correctly(self):
        a = self.maze.setmaze(2,2)
        self.assertEqual(self.maze.printmaze(a), True)
