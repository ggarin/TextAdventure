from room import Room


class Hero:
    def __init__(self, name: str='DefaultHero', room: Room=Room()):
        self.__name = name
        self.__current_room = room
        self.__inventory = []

    def display(self):
        print(self.__name + ' is in the room ' + self.current_room.name)

    def move(self, room: Room):
        self.__current_room = room

    def entry(self, room: Room):
        if room.verify_entry(self.__inventory):
            self.move(room)
        else:
            input('Press enter to continue...')

    def pick_key(self):
        if self.__current_room.key is not None:
            print('Object found:')
            print('You found the ' + self.__current_room.key.value + ' !')
            self.__inventory.append(self.__current_room.key)
            # TODO: delete key in room

    @property
    def current_room(self):
        return self.__current_room

    @property
    def keys(self):
        return self.__inventory
