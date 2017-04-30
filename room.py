from directions import Directions


class Room:
    def __init__(self, name='Default Room', description='Default Description', directions=Directions(), is_win=False):
        self.name = name
        self.description = description
        self.directions = directions
        self.is_win = is_win

    def display(self):
        print(self.name)
        print('Description:')
        print(self.description)

    def action_room(self):
        self.display()
        return self.directions.ask_direction()

    def get_name(self):
        return self.name

    def get_is_win(self):
        return self.is_win


def main():
    my_room = Room()
    print(my_room.action_room().value)


if __name__ == "__main__":
    main()
