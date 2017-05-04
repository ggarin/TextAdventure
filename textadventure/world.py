import numpy

from .directions import Direction
from .hero import Hero
from .obj import Obj
from .room import Room
from .enemy import Enemy


class World:
    def __init__(self, name: str=None):
        room3 = Room('Start', 'You just enter into a manor! You are in a big room with a nice carpet. The door '
                              'behind you close itself. You now have to choose in three direction.',
                     [Direction.WEST, Direction.NORTH, Direction.EAST])
        room2 = Room('Kitchen', 'You enter into a kitchen. Some meal are under preparation but no one is here. You see '
                                'a door in front of you or you can just go back.',
                     [Direction.WEST, Direction.EAST])
        room1 = Room('Closet', 'You found a closet with a lot of cooking stuff. You have to go back',
                     [Direction.EAST], obj_in_room=Obj.DOM_ROOM_KEY)
        room4 = Room('Domestic Chamber', 'You enter into a small chamber with a simple bed and a piece of furniture and'
                                         ' a small window. There is a book on a chair close to the bed.',
                     [Direction.WEST], obj_in_room=Obj.GUN, condition_to_enter=Obj.DOM_ROOM_KEY)
        room7 = Room('Living room', 'This is the first part of the living room. There is shelf on the wall  with a lot '
                                    'of books. You can explore the living room in two directions',
                     [Direction.NORTH, Direction.EAST, Direction.SOUTH])
        room8 = Room('Living room', 'This is another part of the living room. There is a big table with some plates and'
                                    ' cutlery ready for eating.',
                     [Direction.WEST, Direction.NORTH])
        room12 = Room('Living room', 'This is another part of the living room. There is a sofa and a coffee table. You '
                                     'can see three half empty glasses. You see a close chest under the windows.',
                      [Direction.WEST, Direction.NORTH, Direction.SOUTH])
        room16 = Room('Chest', 'You open the chest and found bottles of alcohol.',
                      [Direction.SOUTH], obj_in_room=Obj.BATHROOM_KEY)
        room11 = Room('Living room', 'This is another part of the living room. You can see a stair going down in North '
                                     'and a long hallway in the West.',
                      [Direction.WEST, Direction.NORTH, Direction.EAST, Direction.SOUTH])
        room15 = Room('Stairs', 'Some dark stairs are going down to a toilet.',
                      [Direction.SOUTH])
        room10 = Room('Hallway', 'A simple hallway with chandelier give access to two rooms.',
                      [Direction.WEST, Direction.NORTH, Direction.EAST],
                      enemy=Enemy('Zombie', Obj.GUN, 'A Zombie come from the North and jump on you!'))
        room14 = Room('Children Chamber', 'An empty children chamber with a lot of toys on the floor.',
                      [Direction.SOUTH])
        room9 = Room('Adults Chamber', 'A big room with a double bed. You can see a light passing though a door in '
                                       'the south.',
                     [Direction.EAST, Direction.SOUTH])
        room5 = Room('Bathroom', 'You open the door and find a bathroom. You discover the girl afraid and crying! You '
                                 'saved her!',
                     [Direction.EAST, Direction.SOUTH], condition_to_enter=Obj.BATHROOM_KEY, is_win=True)
        self.room_table = numpy.matrix([[room1, room2, room3, room4], [room5, Room(), room7, room8],
                                        [room9, room10, room11, room12], [Room(), room14, room15, room16]],
                                       dtype=Room)
        self.hero = Hero(name, self.room_table[0, 2])

    def display(self):
        room_shape = self.room_table.shape
        print('The world contains ' + str(room_shape[0]*room_shape[1]) + ' rooms')

    def run_game(self):
        while not self.hero.current_room.is_win:
            direction = self.hero.action()
            if direction is None:
                break
            loc_room: tuple = numpy.where(self.room_table == self.hero.current_room)
            new_loc_room = move(direction, loc_room)
            new_room: Room = self.room_table.item(new_loc_room[0][0], new_loc_room[1][0])
            self.hero.entry(new_room)
        if self.hero.status:
            self.hero.current_room.display()
            print('You Win!')
        else:
            print('You Loose!')


def move(direction: Direction, location: tuple):
    new_location = ()
    if direction == Direction.NORTH:
        new_location = (location[0] + 1, location[1])
    elif direction == Direction.EAST:
        new_location = (location[0], location[1] + 1)
    elif direction == Direction.SOUTH:
        new_location = (location[0] - 1, location[1])
    elif direction == Direction.WEST:
        new_location = (location[0], location[1] - 1)
    return new_location