class Room:
    # define a room
    def __init__(self, name='DefaultRoom', description='DefaultDescription', is_win=False):
        self.name = name
        self.description = description
        self.is_win = is_win

    def display(self):
        print(self.name)
        print('Description:')
        print(self.description)

    def get_name(self):
        return self.name

    def get_is_win(self):
        return self.is_win


def main():
    my_room = Room()
    my_room.display()


if __name__ == "__main__":
    main()
