from unittest import TestCase
from unittest.mock import patch
from hero import Hero
from room import Room
from directions import Directions
from keys import Keys


class TestHero(TestCase):
    def test_move(self):
        my_hero = Hero('UT', Room('Init Room'))
        move_room = Room('Move room')
        my_hero.move(move_room)
        self.assertEqual(move_room, my_hero.current_room)

    @patch.object(Room, "verify_entry")
    def test_entry_allowed(self, mock_verify_entry):
        mock_verify_entry.return_value = True
        my_hero = Hero('UT', Room('Init Room'))
        move_room = Room('Move room')
        my_hero.entry(move_room)
        self.assertEqual(my_hero.current_room, move_room)

    @patch.object(Room, "verify_entry")
    @patch('builtins.input')
    def test_entry_not_allowed(self, mock_verify_entry, mock_input):
        mock_verify_entry.return_value = False
        mock_input.return_value = None
        init_room = Room('Init Room')
        my_hero = Hero('UT', init_room)
        move_room = Room('Move room')
        my_hero.entry(move_room)
        self.assertEqual(my_hero.current_room, init_room)

    def test_pick_key_with_key(self):
        my_hero = Hero('UT', Room('Init Room', 'des', Directions(), Keys.BATHROOM_KEY))
        self.assertNotIn(Keys.BATHROOM_KEY, my_hero.keys)
        my_hero.pick_key()
        self.assertIn(Keys.BATHROOM_KEY, my_hero.keys)

    def test_pick_key_without_key(self):
        my_hero = Hero('UT', Room('Init Room', 'des', Directions(), None))
        self.assertNotIn(Keys.BATHROOM_KEY, my_hero.keys)
        my_hero.pick_key()
        self.assertNotIn(Keys.BATHROOM_KEY, my_hero.keys)


