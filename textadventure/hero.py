from .room import Room
from .keys import Keys


class Hero:
    def __init__(self, name: str='DefaultHero', room: Room=Room(), inventory=None):
        if inventory is None:
            inventory = []
        self.name = name
        self.current_room = room
        self.inventory = inventory
        self.status = True

    def display(self):
        print(self.name + ' is in the room ' + self.current_room.name)

    def move(self, room: Room):
        self.current_room = room

    def entry(self, room: Room):
        if room.verify_entry(self.inventory):
            self.move(room)
        else:
            input('Press enter to continue...')

    def action(self):
        self.meet_enemy()
        if not self.status:
            return None
        self.current_room.display()
        self.pick_key()
        return self.current_room.action_room()

    def pick_key(self):
        if self.current_room.key is not None:
            print('Object found:')
            print('You found the ' + self.current_room.key.value + '!')
            self.inventory.append(self.current_room.key)
            self.current_room.delete_key()

    def defeat_enemy(self):
        # TODO: Refactor with room.verify_entry
        print('What do you want to use to fight him?')
        for iInv in range(len(self.inventory)):
            print(str(iInv+1) + ' - ' + self.inventory[iInv].value)
        print(str(len(self.inventory) + 1) + ' - Punch')
        while True:
            try:
                choice = int(input()) - 1
                if choice == len(self.inventory):
                    choice = Keys.PUNCH
                else:
                    choice = self.inventory[choice]
                break
            except (ValueError, IndexError):
                print('Invalid object')
        return self.current_room.enemy.is_win_fight(choice)

    def meet_enemy(self):
        if self.current_room.enemy is None:
            return
        self.current_room.enemy.display()
        if self.defeat_enemy():
            print('You defeat the ' + self.current_room.enemy.name + '!')
            self.current_room.delete_enemy()
        else:
            print('You have been defeated by the ' + self.current_room.enemy.name + '!')
            print('You are dead!')
            self.status = False
