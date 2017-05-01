import numpy

from .directions import Direction, Directions, move
from .hero import Hero
from .keys import Keys
from .room import Room


class World:
    def __init__(self, name: str=None):
        room3 = Room('Start', 'You just enter into a manor ! You are in a big room with a nice carpet. The door '
                              'behind you close itself. You now have to choose in three direction.',
                     Directions([Direction.WEST, Direction.NORTH, Direction.EAST]))
        room2 = Room('Kitchen', 'You enter into a kitchen. Some meal are under preparation but no one is here. You see '
                                'a door in front of you or you can just go back.',
                     Directions([Direction.WEST, Direction.EAST]))
        room1 = Room('Closet', 'You found a closet with a lot of cooking stuff. You have to go back',
                     Directions([Direction.EAST]), Keys.DOM_ROOM_KEY)
        room4 = Room('Domestic Chamber', 'You enter into a small chamber with a simple bed and a piece of furniture and'
                                         ' a small window. There is a book on a chair close to the bed.',
                     Directions([Direction.WEST]), Keys.GUN, Keys.DOM_ROOM_KEY)
        room7 = Room('Living room', 'This is the first part of the living room. There is shelf on the wall  with a lot '
                                    'of books. You can explore the living room in two directions',
                     Directions([Direction.NORTH, Direction.EAST, Direction.SOUTH]))
        room8 = Room('Living room', 'This is another part of the living room. There is a big table with some plates and'
                                    ' cutlery ready for eating.',
                     Directions([Direction.WEST, Direction.NORTH]))
        room12 = Room('Living room', 'This is another part of the living room. There is a sofa and a coffee table. You '
                                     'can see three half empty glasses. You see a close chest under the windows.',
                      Directions([Direction.WEST, Direction.NORTH, Direction.SOUTH]))
        room16 = Room('Chest', 'You open the chest and found bottles of alcohol.',
                      Directions([Direction.SOUTH]), Keys.BATHROOM_KEY)
        room11 = Room('Living room', 'This is another part of the living room. You can see a stair going down in North '
                                     'and a long hallway in the West.',
                      Directions([Direction.WEST, Direction.NORTH, Direction.EAST, Direction.SOUTH]))
        room15 = Room('Stairs', 'Some dark stairs are going down to a toilet.',
                      Directions([Direction.SOUTH]))
        room10 = Room('Hallway', 'A simple hallway with chandelier give access to two rooms.',
                      Directions([Direction.WEST, Direction.NORTH, Direction.EAST]))
        room14 = Room('Children Chamber', 'An empty children chamber with a lot of toys on the floor.',
                      Directions([Direction.SOUTH]))
        room9 = Room('Adults Chamber', 'A big room with a double bed. You can see a light passing though a door in '
                                       'the south.',
                     Directions([Direction.EAST, Direction.SOUTH]))
        room5 = Room('Bathroom', 'You open the door and find a bathroom. You discover the girl afraid and crying ! You '
                                 'saved her!',
                     Directions([Direction.EAST, Direction.SOUTH]), None, Keys.BATHROOM_KEY, True)
        self.__room_table = numpy.matrix([[room1, room2, room3, room4], [room5, Room(), room7, room8],
                                          [room9, room10, room11, room12], [Room(), room14, room15, room16]],
                                         dtype=Room)
        self.__hero = Hero(name, self.__room_table[0, 2])

    def display(self):
        room_shape = self.__room_table.shape
        print('The world contains ' + str(room_shape[0]*room_shape[1]) + ' rooms')

    def run_game(self):
        while not self.__hero.current_room.is_win:
            direction = self.__hero.action()
            loc_room: tuple = numpy.where(self.__room_table == self.__hero.current_room)
            new_loc_room = move(direction, loc_room)
            new_room: Room = self.__room_table.item(new_loc_room[0][0], new_loc_room[1][0])
            self.__hero.entry(new_room)
        self.__hero.current_room.display()
        print('You Win !')
