from .directions import Direction
from .obj import Obj
from .enemy import Enemy


class Room:
    def __init__(self, name: str='Default Room', description: str='Default Description',
                 directions: [Direction]=None, obj_in_room: Obj=None, condition_to_enter: Obj=None,
                 is_win: bool=False, enemy: Enemy=None):
        if directions is None:
            directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        self.name = name
        self.description = description
        self.directions = directions
        self.obj_in_room = obj_in_room
        self.condition_to_enter = condition_to_enter
        self.enemy = enemy
        self.is_win = is_win

    def display(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(self.name)
        print('Description:')
        print(self.description)

    def action_room(self):
        print('Where do you want to go ?')
        for iDirection in self.directions:
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
            if direction_choose not in self.directions:
                valid_input = False
                print('You cannot go in this direction. Please, choose another direction!')
            else:
                valid_input = True
        return direction_choose

    def verify_entry(self, inventory: [Obj]):
        if self.condition_to_enter is None:
            return True
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('The door is closed.')
        if not inventory:
            print('You have nothing on you to open the door.')
            return False
        print('What do you want to use?')
        for iInv in range(len(inventory)):
            print(str(iInv+1) + ' - ' + inventory[iInv].value)
        while True:
            try:
                choice = inventory[int(input())-1]
                break
            except (ValueError, IndexError):
                print('Invalid object')
        if self.condition_to_enter == choice:
            print('You open the door with the ' + choice.value + '!')
            return True
        else:
            print('Nothing happen!')
            return False

    def delete_obj(self):
        self.obj_in_room = None

    def delete_enemy(self):
        self.enemy = None
