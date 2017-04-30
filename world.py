from room import Room
from hero import Hero
import numpy


class World:
    def __init__(self, name=None):
        self.room_table = numpy.matrix([[Room(), Room()], [Room(), Room()]], dtype=Room)
        self.hero = Hero(name, self.room_table[0, 0])

    def display(self):
            print('The world contains ' + str(len(self.room_table)) + ' rooms')


def main():
    my_world = World()
    my_world.display()

if __name__ == "__main__":
    main()
