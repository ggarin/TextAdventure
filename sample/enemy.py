from .keys import Keys


class Enemy:
    def __init__(self, name: str='Enemy', kill_by: Keys=Keys.GUN):
        self.__name = name
        self.__kill_by = kill_by

    def is_win_fight(self, keys: Keys):
        return self.__kill_by == keys

    def display(self):
        print('You meet the ' + self.__name + '!')

    @property
    def name(self):
        return self.__name
