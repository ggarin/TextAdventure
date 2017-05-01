from unittest import TestCase

from sample.enemy import Enemy
from sample.keys import Keys


class TestEnemy(TestCase):
    def test_win_fight(self):
        my_enemy = Enemy(kill_by=Keys.GUN)
        self.assertTrue(my_enemy.is_win_fight(Keys.GUN))

    def test_loose_fight(self):
        my_enemy = Enemy(kill_by=Keys.GUN)
        self.assertFalse(my_enemy.is_win_fight(Keys.RANDOM_KEY))
