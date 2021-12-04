# pylint: skip-file

import unittest
import aldous_broder

class TestAldousBroder(unittest.TestCase):
    def setUp(self):
        self.maze = aldous_broder.AldousBroder(5,5)

    def test_maze_y_correct(self):
        self.assertEqual(self.maze.ycoord, 5)
    def test_maze_x_correct(self):
        self.assertEqual(self.maze.xcoord, 5)

    def test_start_y_inside_range(self):
        randstart = self.maze.randomized_start()
        self.assertLess(randstart[0], 6)
        self.assertGreater(randstart[0], -1)

    def test_start_x_inside_range(self):
        randstart = self.maze.randomized_start()
        self.assertLess(randstart[1], 6)
        self.assertGreater(randstart[1], -1)

    def test_maze_has_walls(self):
        self.assertIn("|", self.maze.maze[0])
    
    def test_maze_has_maze(self):
        self.assertIn("x", self.maze.maze[1])

    def test_maze_has_no_unvisited(self):
        self.assertNotIn("o", self.maze.maze[0])
        self.assertNotIn("o", self.maze.maze[1])
        self.assertNotIn("o", self.maze.maze[2])
        self.assertNotIn("o", self.maze.maze[3])
        self.assertNotIn("o", self.maze.maze[4])