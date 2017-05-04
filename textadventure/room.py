from .directions import Directions
from .keys import Keys
from .enemy import Enemy


class Room:
    def __init__(self, name: str='Default Room', description: str='Default Description',
                 directions: Directions=Directions(), key: Keys=None, condition: Keys=None, is_win: bool=False,
                 enemy: Enemy=None):
        self.name = name
        self.description = description
        self.directions = directions
        self.key = key
        self.condition = condition
        self.enemy = enemy
        self.is_win = is_win

    def display(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(self.name)
        print('Description:')
        print(self.description)

    def action_room(self):
        return self.directions.ask_direction()

    def verify_entry(self, inventory: [Keys]):
        if self.condition is None:
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
        if self.condition == choice:
            print('You open the door with the ' + choice.value + '!')
            return True
        else:
            print('Nothing happen!')
            return False

    def delete_key(self):
        self.key = None

    def delete_enemy(self):
        self.enemy = None
