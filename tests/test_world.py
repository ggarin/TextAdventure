from unittest import TestCase

from textadventure.world import World
from textadventure.directions import Direction


class TestWorld(TestCase):
    def setUp(self):
        self.my_world = World(init_x_pos=1, init_y_pos=2)

    def test_get_room_after_move_N(self):
        new_room = self.my_world.get_room_after_move(direction=Direction.NORTH)
        self.assertEqual(new_room, self.my_world.room_table[2, 2])

    def test_get_room_after_move_S(self):
        new_room = self.my_world.get_room_after_move(direction=Direction.SOUTH)
        self.assertEqual(new_room, self.my_world.room_table[0, 2])

    def test_get_room_after_move_E(self):
        new_room = self.my_world.get_room_after_move(direction=Direction.EAST)
        self.assertEqual(new_room, self.my_world.room_table[1, 3])

    def test_get_room_after_move_W(self):
        new_room = self.my_world.get_room_after_move(direction=Direction.WEST)
        self.assertEqual(new_room, self.my_world.room_table[1, 1])
