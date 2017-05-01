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
        self.assertEqual(my_room.action_room(), Direction.NORTH)

    def test_verify_entry_no_key_needed(self):
        my_room = Room()
        keys = []
        self.assertTrue(my_room.verify_entry(keys))

    def test_verify_entry_key_needed_no_inventory(self):
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        keys = []
        self.assertFalse(my_room.verify_entry(keys))

    @patch('builtins.input')
    def test_verify_entry_key_needed_good_key_selected(self, mock_input):
        mock_input.return_value = 1
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        keys = [Keys.BATHROOM_KEY, Keys.RANDOM_KEY]
        self.assertTrue(my_room.verify_entry(keys))

    @patch('builtins.input')
    def test_verify_entry_key_needed_bad_key_selected(self, mock_input):
        mock_input.return_value = 2
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        keys = [Keys.BATHROOM_KEY, Keys.RANDOM_KEY]
        self.assertFalse(my_room.verify_entry(keys))

    @patch('builtins.input')
    def test_verify_entry_key_needed_good_key_selected_after_mistakes(self, mock_input):
        mock_input.side_effect = ['a', 12, 1]
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        keys = [Keys.BATHROOM_KEY, Keys.RANDOM_KEY]
        self.assertTrue(my_room.verify_entry(keys))

    def test_delete_key(self):
        my_room = Room('Init Room', 'des', Directions(), None, Keys.BATHROOM_KEY)
        my_room.delete_key()
        self.assertIsNone(my_room.key)