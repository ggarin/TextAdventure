from room import Room


class Hero:
    def __init__(self, name='DefaultHero', room=Room()):
        self.name = name
        self.room = room
        self.keys = []

    def display(self):
        print(self.name + ' is in the room ' + self.room.get_name())

    def move(self, room):
        self.room = room

    def pick_key(self):
        if self.room.get_key() is not None:
            print('Key found:')
            print('You found the ' + self.room.get_key().value + ' !')
            self.keys.append(self.room.get_key())

    def get_room(self):
        return self.room

    def get_keys(self):
        return self.keys


def main():
    my_hero = Hero('ThT12', Room())
    my_hero.display()
    my_hero.move(Room("New_Room"))
    my_hero.display()


if __name__ == "__main__":
    main()
