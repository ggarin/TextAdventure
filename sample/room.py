from .directions import Directions
from .keys import Keys


class Room:
    def __init__(self, name: str='Default Room', description: str='Default Description',
                 directions: Directions=Directions(), key: Keys=None, condition: Keys=None, is_win: bool=False):
        self.__name = name
        self.__description = description
        self.__directions = directions
        self.__key = key
        self.__condition = condition
        self.__is_win = is_win

    def display(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(self.__name)
        print('Description:')
        print(self.__description)

    def action_room(self):
        return self.__directions.ask_direction()

    def verify_entry(self, inventory: [Keys]):
        if self.__condition is None:
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
        if self.__condition == choice:
            print('You open the door with the ' + choice.value + '!')
            return True
        else:
            print('Nothing happen!')
            return False

    def delete_key(self):
        self.__key = None

    @property
    def key(self):
        return self.__key

    @property
    def name(self):
        return self.__name

    @property
    def is_win(self):
        return self.__is_win
