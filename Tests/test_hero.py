from unittest import TestCase
from unittest.mock import patch

from textadventure.directions import Direction
from textadventure.hero import Hero
from textadventure.keys import Keys
from textadventure.room import Room
from textadventure.enemy import Enemy


class TestHero(TestCase):
    def test_move(self):
        my_hero = Hero(room=Room('Init Room'))
        move_room = Room('Move room')
        my_hero.move(move_room)
        self.assertEqual(move_room, my_hero.current_room)

    @patch.object(Room, "verify_entry")
    def test_entry_allowed(self, mock_verify_entry):
        mock_verify_entry.return_value = True
        my_hero = Hero(room=Room('Init Room'))
        move_room = Room('Move room')
        my_hero.entry(move_room)
        self.assertEqual(my_hero.current_room, move_room)

    @patch.object(Room, "verify_entry")
    @patch('builtins.input')
    def test_entry_not_allowed(self, mock_verify_entry, mock_input):
        mock_verify_entry.return_value = False
        mock_input.return_value = None
        init_room = Room('Init Room')
        my_hero = Hero(room=init_room)
        move_room = Room('Move room')
        my_hero.entry(move_room)
        self.assertEqual(my_hero.current_room, init_room)

    @patch('builtins.input')
    def test_action_not_dead(self, mock_input):
        mock_input.return_value = 'N'
        my_hero = Hero(room=Room(key=Keys.BATHROOM_KEY))
        self.assertEqual(Direction.NORTH, my_hero.action())
        self.assertIn(Keys.BATHROOM_KEY, my_hero.inventory)

    def test_action_dead(self):
        my_hero = Hero(room=Room(key=Keys.BATHROOM_KEY))
        my_hero.status = False
        self.assertIsNone(my_hero.action())

    def test_pick_key_with_key(self):
        my_hero = Hero(room=Room(key=Keys.BATHROOM_KEY))
        self.assertNotIn(Keys.BATHROOM_KEY, my_hero.inventory)
        my_hero.pick_key()
        self.assertIn(Keys.BATHROOM_KEY, my_hero.inventory)
        self.assertIsNone(my_hero.current_room.key)

    def test_pick_key_without_key(self):
        my_hero = Hero(room=Room(key=None))
        self.assertNotIn(Keys.BATHROOM_KEY, my_hero.inventory)
        my_hero.pick_key()
        self.assertNotIn(Keys.BATHROOM_KEY, my_hero.inventory)

    @patch('builtins.input')
    def test_defeat_enemy_when_enemy(self, mock_input):
        mock_input.return_value = 1
        my_hero = Hero(room=Room(enemy=Enemy(kill_by=Keys.GUN)), inventory=[Keys.GUN])
        self.assertTrue(my_hero.defeat_enemy())

    @patch('builtins.input')
    def test_defeat_enemy_when_enemy_no_inventory(self, mock_input):
        mock_input.return_value = 1
        my_hero = Hero(room=Room(enemy=Enemy(kill_by=Keys.GUN)), inventory=[])
        self.assertFalse(my_hero.defeat_enemy())

    @patch('builtins.input')
    def test_defeat_enemy_when_enemy_bad_inventory(self, mock_input):
        mock_input.return_value = 1
        my_hero = Hero(room=Room(enemy=Enemy(kill_by=Keys.GUN)), inventory=[Keys.RANDOM_KEY])
        self.assertFalse(my_hero.defeat_enemy())

    @patch('builtins.input')
    def test_defeat_enemy_when_enemy_bad_choice(self, mock_input):
        mock_input.side_effect = [12, 1]
        my_hero = Hero(room=Room(enemy=Enemy(kill_by=Keys.GUN)), inventory=[Keys.GUN])
        self.assertTrue(my_hero.defeat_enemy())

    def test_meet_enemy_when_no_enemy(self):
        my_hero = Hero(room=Room(enemy=None))
        self.assertIsNone(my_hero.meet_enemy())

    @patch.object(Hero, "defeat_enemy")
    def test_meet_enemy_when_win_fight(self, mock_defeat_enemy):
        mock_defeat_enemy.return_value = True
        my_hero = Hero(room=Room(enemy=Enemy(kill_by=Keys.GUN)))
        my_hero.meet_enemy()
        self.assertTrue(my_hero.status)
        self.assertIsNone(my_hero.current_room.enemy)

    @patch.object(Hero, "defeat_enemy")
    def test_meet_enemy_when_loose_fight(self, mock_defeat_enemy):
        mock_defeat_enemy.return_value = False
        my_hero = Hero(room=Room(enemy=Enemy(kill_by=Keys.GUN)))
        my_hero.meet_enemy()
        self.assertFalse(my_hero.status)
        self.assertIsNotNone(my_hero.current_room.enemy)
