from unittest import TestCase
from unittest.mock import patch
from directions import Direction, Directions


class TestDirections(TestCase):
    @patch('builtins.input', lambda: 'N')
    def test_ask_direction(self):
        my_direction = Directions()
        self.assertEqual(my_direction.ask_direction(), Direction.NORTH)
