from room import Room


class Hero:
    def __init__(self):
        self.name = 'DefaultHero'
        self.room = Room()

    def display(self):
        print(self.name + ' is in the room ' + self.room.get_name())


def main():
    my_hero = Hero()
    my_hero.display()


if __name__ == "__main__":
    main()
