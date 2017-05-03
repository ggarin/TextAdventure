from unittest import TestCase
from unittest.mock import patch

from textadventure.directions import Direction, Directions


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


class TestDirectionsTwice(TestCase):

    def setUp(self):
        self.my_direction = Directions([Direction.WEST, Direction.NORTH])

    @patch('builtins.input')
    def test_ask_direction_unknown_direction(self, mock_input):
        mock_input.side_effect = ['B', 'N']
        self.assertEqual(self.my_direction.ask_direction(), Direction.NORTH)

    @patch('builtins.input')
    def test_ask_direction_blocked_direction(self, mock_input):
        mock_input.side_effect = ['E', 'N']
        self.assertEqual(self.my_direction.ask_direction(), Direction.NORTH)

    @patch('builtins.input')
    def test_ask_direction_first_direction(self, mock_input):
        mock_input.side_effect = ['W', 'N']
        self.assertEqual(self.my_direction.ask_direction(), Direction.WEST)
