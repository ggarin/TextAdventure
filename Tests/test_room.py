from unittest import TestCase
from unittest.mock import patch
from room import Room
from hero import Hero
from directions import Direction, Directions
from keys import Keys


class TestRoom(TestCase):
    @patch('builtins.input', lambda: 'N')
    def test_action_room(self):
        my_room = Room('Init Room', 'des', Directions(), Keys.BATHROOM_KEY)
        my_hero = Hero('TU', my_room)
        self.assertEqual(my_room.action_room(my_hero), Direction.NORTH)
        self.assertTrue(Keys.BATHROOM_KEY in my_hero.keys)

    def test_verify_entry_no_key(self):
        my_room = Room()
        keys = []
        self.assertTrue(my_room.verify_entry(keys))

    def test_verify_entry_good_key(self):
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        keys = [Keys.BATHROOM_KEY, Keys.RANDOM_KEY]
        self.assertTrue(my_room.verify_entry(keys))

    def test_verify_entry_bad_key(self):
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        keys = [Keys.RANDOM_KEY]
        self.assertFalse(my_room.verify_entry(keys))
