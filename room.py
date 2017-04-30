from directions import Directions


class Room:
    def __init__(self, name='Default Room', description='Default Description', directions=Directions(), key=None,
                 condition=None, is_win=False):
        self.name = name
        self.description = description
        self.directions = directions
        self.key = key
        self.condition = condition
        self.is_win = is_win

    def display(self):
        print(self.name)
        print('Description:')
        print(self.description)

    def action_room(self, hero):
        self.display()
        hero.pick_key()
        return self.directions.ask_direction()

    def verify_entry(self, keys):
        if self.condition is None:
            return True
        if self.condition in keys:
            print('You open the door with the ' + self.condition.value + '!')
            return True
        return False

    def get_key(self):
        return self.key

    def get_name(self):
        return self.name

    def get_is_win(self):
        return self.is_win
