from unittest import TestCase
from unittest.mock import patch

from textadventure.directions import Direction, Directions
from textadventure.obj import Obj
from textadventure.room import Room
from textadventure.enemy import Enemy


class TestRoom(TestCase):
    @patch('builtins.input', lambda: 'N')
    def test_action_room(self):
        my_room = Room(directions=Directions())
        self.assertEqual(my_room.action_room(), Direction.NORTH)

    def test_verify_entry_no_key_needed(self):
        my_room = Room(obj_in_room=None)
        keys = []
        self.assertTrue(my_room.verify_entry(keys))

    def test_verify_entry_key_needed_no_inventory(self):
        my_room = Room(condition_to_enter=Obj.BATHROOM_KEY)
        keys = []
        self.assertFalse(my_room.verify_entry(keys))

    @patch('builtins.input')
    def test_verify_entry_key_needed_good_key_selected(self, mock_input):
        mock_input.return_value = 1
        my_room = Room(condition_to_enter=Obj.BATHROOM_KEY)
        keys = [Obj.BATHROOM_KEY, Obj.RANDOM_KEY]
        self.assertTrue(my_room.verify_entry(keys))

    @patch('builtins.input')
    def test_verify_entry_key_needed_bad_key_selected(self, mock_input):
        mock_input.return_value = 2
        my_room = Room(condition_to_enter=Obj.BATHROOM_KEY)
        keys = [Obj.BATHROOM_KEY, Obj.RANDOM_KEY]
        self.assertFalse(my_room.verify_entry(keys))

    @patch('builtins.input')
    def test_verify_entry_key_needed_good_key_selected_after_mistakes(self, mock_input):
        mock_input.side_effect = ['a', 12, 1]
        my_room = Room(condition_to_enter=Obj.BATHROOM_KEY)
        keys = [Obj.BATHROOM_KEY, Obj.RANDOM_KEY]
        self.assertTrue(my_room.verify_entry(keys))

    def test_delete_key(self):
        my_room = Room(obj_in_room=Obj.BATHROOM_KEY)
        my_room.delete_obj()
        self.assertIsNone(my_room.obj_in_room)

    def test_delete_enemy(self):
        my_room = Room(enemy=Enemy())
        my_room.delete_enemy()
        self.assertIsNone(my_room.enemy)
