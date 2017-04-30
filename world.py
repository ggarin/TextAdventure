from room import Room
from hero import Hero
from directions import move
import numpy


class World:
    def __init__(self, name=None):
        self.room_table = numpy.matrix([[Room(), Room()], [Room(), Room()]], dtype=Room)
        self.hero = Hero(name, self.room_table[0, 0])

    def display(self):
        room_shape = self.room_table.shape
        print('The world contains ' + str(room_shape[0]*room_shape[1]) + ' rooms')

    def run_game(self):
        while not self.hero.get_room().get_is_win():
            direction = self.hero.get_room().action_room()
            loc_room = numpy.where(self.room_table == self.hero.get_room())
            new_loc_room = move(direction, loc_room)
            self.hero.move(self.room_table.item(new_loc_room[0][0],new_loc_room[1][0]))


def main():
    my_world = World()
    my_world.display()

if __name__ == "__main__":
    main()
