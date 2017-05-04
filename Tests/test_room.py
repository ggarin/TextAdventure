from unittest import TestCase
from unittest.mock import patch

from textadventure.directions import Direction
from textadventure.obj import Obj
from textadventure.room import Room
from textadventure.enemy import Enemy


class TestActionRoom(TestCase):
    def setUp(self):
        self.my_room = Room()

    @patch('builtins.input', lambda: 'N')
    def test_action_room_N(self):
        self.assertEqual(self.my_room.action_room(), Direction.NORTH)

    @patch('builtins.input', lambda: 'North')
    def test_action_room_North(self):
        self.assertEqual(self.my_room.action_room(), Direction.NORTH)

    @patch('builtins.input', lambda: 'S')
    def test_action_room_S(self):
        self.assertEqual(self.my_room.action_room(), Direction.SOUTH)

    @patch('builtins.input', lambda: 'South')
    def test_action_room_South(self):
        self.assertEqual(self.my_room.action_room(), Direction.SOUTH)

    @patch('builtins.input', lambda: 'E')
    def test_action_room_E(self):
        self.assertEqual(self.my_room.action_room(), Direction.EAST)

    @patch('builtins.input', lambda: 'East')
    def test_action_room_East(self):
        self.assertEqual(self.my_room.action_room(), Direction.EAST)

    @patch('builtins.input', lambda: 'W')
    def test_action_room_W(self):
        self.assertEqual(self.my_room.action_room(), Direction.WEST)

    @patch('builtins.input', lambda: 'West')
    def test_action_room_West(self):
        self.assertEqual(self.my_room.action_room(), Direction.WEST)


class TestActionRoomTwice(TestCase):

    def setUp(self):
        self.my_room = Room(directions=[Direction.WEST, Direction.NORTH])

    @patch('builtins.input')
    def test_ask_direction_unknown_direction(self, mock_input):
        mock_input.side_effect = ['B', 'N']
        self.assertEqual(self.my_room.action_room(), Direction.NORTH)

    @patch('builtins.input')
    def test_ask_direction_blocked_direction(self, mock_input):
        mock_input.side_effect = ['E', 'N']
        self.assertEqual(self.my_room.action_room(), Direction.NORTH)

    @patch('builtins.input')
    def test_ask_direction_first_direction(self, mock_input):
        mock_input.side_effect = ['W', 'N']
        self.assertEqual(self.my_room.action_room(), Direction.WEST)


class TestRoom(TestCase):
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
