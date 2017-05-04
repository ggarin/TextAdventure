from .keys import Keys


class Enemy:
    def __init__(self, name: str='Enemy', kill_by: Keys=Keys.GUN, context: str='I\'m the monster!'):
        self.name = name
        self.kill_by = kill_by
        self.context = context

    def is_win_fight(self, keys: Keys):
        return self.kill_by == keys

    def display(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You meet the ' + self.name + '!')
        print(self.context)
