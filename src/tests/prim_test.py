# pylint: skip-file

import unittest
import prim

class TestPrim(unittest.TestCase):
    def setUp(self):
        self.prim = prim.Prim(5,5)

    def test_maze_y_correct(self):
        self.assertEqual(self.prim.y, 5)
    def test_maze_x_correct(self):
        self.assertEqual(self.prim.x, 5)

    def test_start_y_inside_range(self):
        randstart = self.prim.randomized_start()
        self.assertLess(randstart[0], 6)
        self.assertGreater(randstart[0], -1)

    def test_start_x_inside_range(self):
        randstart = self.prim.randomized_start()
        self.assertLess(randstart[1], 6)
        self.assertGreater(randstart[1], -1)

    def test_maze_has_walls(self):
        self.assertIn("|", self.prim.maze[0])
    
    def test_maze_has_maze(self):
        self.assertIn("x", self.prim.maze[1])

    def test_maze_has_no_unvisited(self):
        self.assertNotIn("o", self.prim.maze[0])
        self.assertNotIn("o", self.prim.maze[1])
        self.assertNotIn("o", self.prim.maze[2])
        self.assertNotIn("o", self.prim.maze[3])
        self.assertNotIn("o", self.prim.maze[4])