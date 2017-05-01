from .room import Room
from .keys import Keys


class Hero:
    def __init__(self, name: str='DefaultHero', room: Room=Room(), inventory=None):
        if inventory is None:
            inventory = []
        self.__name = name
        self.__current_room = room
        self.__inventory = inventory
        self.__status = True

    def display(self):
        print(self.__name + ' is in the room ' + self.current_room.name)

    def move(self, room: Room):
        self.__current_room = room

    def entry(self, room: Room):
        if room.verify_entry(self.__inventory):
            self.move(room)
        else:
            input('Press enter to continue...')

    def action(self):
        self.meet_enemy()
        if not self.__status:
            return None
        self.current_room.display()
        self.pick_key()
        return self.current_room.action_room()

    def pick_key(self):
        if self.__current_room.key is not None:
            print('Object found:')
            print('You found the ' + self.__current_room.key.value + ' !')
            self.__inventory.append(self.__current_room.key)
            self.__current_room.delete_key()

    def defeat_enemy(self):
        # TODO: Refactor with room.verify_entry
        for iInv in range(len(self.__inventory)):
            print(str(iInv+1) + ' - ' + self.__inventory[iInv].value)
        print(str(len(self.__inventory)+1) + ' - Punch')
        while True:
            try:
                choice = int(input()) - 1
                if choice == len(self.__inventory):
                    choice = Keys.PUNCH
                else:
                    choice = self.__inventory[choice]
                break
            except (ValueError, IndexError):
                print('Invalid object')
        return self.__current_room.enemy.is_win_fight(choice)

    def meet_enemy(self):
        if self.__current_room.enemy is None:
            return
        self.__current_room.enemy.display()
        if self.defeat_enemy():
            print('You defeat the ' + self.__current_room.enemy.name + '!')
            self.__current_room.delete_enemy()
        else:
            print('You have been defeated by the ' + self.__current_room.enemy.name + '!')
            print('You are dead !')
            self.__status = False

    @property
    def current_room(self):
        return self.__current_room

    @property
    def keys(self):
        return self.__inventory

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: bool):
        self.__status = status
