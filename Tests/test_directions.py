from unittest import TestCase
from unittest.mock import patch
from directions import Direction, Directions


class TestDirections(TestCase):

    def setUp(self):
        self.my_direction = Directions()

    @patch('builtins.input', lambda: 'N')
    def test_ask_direction_N(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.NORTH)

    @patch('builtins.input', lambda: 'North')
    def test_ask_direction_North(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.NORTH)

    @patch('builtins.input', lambda: 'S')
    def test_ask_direction_S(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.SOUTH)

    @patch('builtins.input', lambda: 'South')
    def test_ask_direction_South(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.SOUTH)

    @patch('builtins.input', lambda: 'E')
    def test_ask_direction_E(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.EAST)

    @patch('builtins.input', lambda: 'East')
    def test_ask_direction_East(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.EAST)

    @patch('builtins.input', lambda: 'W')
    def test_ask_direction_W(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.WEST)

    @patch('builtins.input', lambda: 'West')
    def test_ask_direction_West(self):
        self.assertEqual(self.my_direction.ask_direction(), Direction.WEST)


class ExceptionTest(TestCase):

    def setUp(self):
        self.my_direction = Directions([Direction.WEST, Direction.NORTH])

    @patch('builtins.input', lambda: 'B')
    def test_ask_direction_unknown_direction(self):
        self.assertRaises(ValueError, self.my_direction.ask_direction)

    @patch('builtins.input', lambda: 'S')
    def test_ask_direction_impossible_direction(self):
        self.assertRaises(ValueError, self.my_direction.ask_direction)
