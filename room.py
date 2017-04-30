class Room:
    # define a room
    def __init__(self, name='DefaultRoom'):
        self.name = name

    def display(self):
        print(self.name)

    def get_name(self):
        return self.name


def main():
    my_room = Room()
    my_room.display()


if __name__ == "__main__":
    main()
