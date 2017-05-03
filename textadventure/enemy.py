from .keys import Keys


class Enemy:
    def __init__(self, name: str='Enemy', kill_by: Keys=Keys.GUN, context: str='I\'m the monster!'):
        self.__name = name
        self.__kill_by = kill_by
        self.__context = context

    def is_win_fight(self, keys: Keys):
        return self.__kill_by == keys

    def display(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You meet the ' + self.__name + '!')
        print(self.__context)

    @property
    def name(self):
        return self.__name
