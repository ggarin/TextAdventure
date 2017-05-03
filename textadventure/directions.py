from enum import Enum


class Direction(str, Enum):
    NORTH = 'N - North'
    EAST = 'E - East'
    SOUTH = 'S - South'
    WEST = 'W - West'


class Directions:
    def __init__(self, directions: [Direction]=None):
        if directions is None:
            directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        self.__directions = directions

    def ask_direction(self):
        print('Where do you want to go ?')
        for iDirection in self.__directions:
            print(iDirection.value)
        valid_input = False
        direction_choose: Direction
        while not valid_input:
            user_chose = input()
            if user_chose in ['N', 'North']:
                direction_choose = Direction.NORTH
            elif user_chose in ['E', 'East']:
                direction_choose = Direction.EAST
            elif user_chose in ['S', 'South']:
                direction_choose = Direction.SOUTH
            elif user_chose in ['W', 'West']:
                direction_choose = Direction.WEST
            else:
                valid_input = False
                print('Unknown direction input. Please, try again!')
                continue
            if direction_choose not in self.__directions:
                valid_input = False
                print('You cannot go in this direction. Please, choose another direction!')
            else:
                valid_input = True
        return direction_choose


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
