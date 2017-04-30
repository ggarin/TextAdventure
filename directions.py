from enum import Enum


class Direction(Enum):
    NORTH = 'North (N)'
    EAST = 'East (E)'
    SOUTH = 'South (S)'
    WEST = 'West (W)'


class Directions:
    def __init__(self, directions=None):
        if directions is None:
            directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        self.directions = directions

    def ask_direction(self):
        print('Where do you want to go ?')
        first = True
        for iDirection in self.directions:
            if first:
                first = False
                print(iDirection.value)
            else:
                print('or ' + iDirection.value)
        user_chose = input()
        if user_chose == 'N' or user_chose == 'North':
            direction_choose = Direction.NORTH
        elif user_chose == 'E' or user_chose == 'East':
            direction_choose = Direction.EAST
        elif user_chose == 'S' or user_chose == 'South':
            direction_choose = Direction.SOUTH
        elif user_chose == 'W' or user_chose == 'West':
            direction_choose = Direction.WEST
        else:
            raise ValueError('Bad direction')
        if direction_choose not in self.directions:
            raise ValueError('Impossible direction')
        return direction_choose


def move(direction, location):
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


def main():
    my_directions = Directions([Direction.NORTH, Direction.EAST])
    direction = my_directions.ask_direction()
    print(direction.value)

if __name__ == "__main__":
    main()
