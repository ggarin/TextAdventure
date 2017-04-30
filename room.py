from directions import Directions
from keys import Keys


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

    def action_room(self, hero):
        self.display()
        hero.pick_key()
        return self.__directions.ask_direction()

    def verify_entry(self, keys: [Keys]):
        if self.__condition is None:
            return True
        if self.__condition in keys:
            print('You open the door with the ' + self.__condition.value + '!')
            return True
        return False

    @property
    def key(self):
        return self.__key

    @property
    def name(self):
        return self.__name

    @property
    def is_win(self):
        return self.__is_win
