from room import Room


class Hero:
    def __init__(self, name: str='DefaultHero', room: Room=Room()):
        self.__name = name
        self.__current_room = room
        self.__keys = []

    def display(self):
        print(self.__name + ' is in the room ' + self.current_room.name)

    def move(self, room: Room):
        self.__current_room = room

    def entry(self, room: Room):
        if room.verify_entry(self.__keys):
            self.move(room)
        else:
            print('You need a key to go here !')
            input('Press enter to continue...')

    def pick_key(self):
        if self.__current_room.key is not None:
            print('Object found:')
            print('You found the ' + self.__current_room.key.value + ' !')
            self.__keys.append(self.__current_room.key)

    @property
    def current_room(self):
        return self.__current_room

    @property
    def keys(self):
        return self.__keys
