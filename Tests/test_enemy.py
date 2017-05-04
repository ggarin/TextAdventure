from unittest import TestCase

from textadventure.enemy import Enemy
from textadventure.obj import Obj


class TestEnemy(TestCase):
    def test_win_fight(self):
        my_enemy = Enemy(kill_by=Obj.GUN)
        self.assertTrue(my_enemy.is_win_fight(Obj.GUN))

    def test_loose_fight(self):
        my_enemy = Enemy(kill_by=Obj.GUN)
        self.assertFalse(my_enemy.is_win_fight(Obj.RANDOM_KEY))
