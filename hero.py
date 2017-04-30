from room import Room


class Hero:
    def __init__(self, name='DefaultHero', room=Room()):
        self.name = name
        self.room = room

    def display(self):
        print(self.name + ' is in the room ' + self.room.get_name())

    def move(self, room):
        self.room = room


def main():
    my_hero = Hero('ThT12', Room())
    my_hero.display()
    my_hero.move(Room("New_Room"))
    my_hero.display()


if __name__ == "__main__":
    main()
