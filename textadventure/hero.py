from .room import Room
from .obj import Obj


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

    def entry(self, room: Room):
        if self.verify_entry(room):
            self.current_room = room
        else:
            input('Press enter to continue...')

    def verify_entry(self, room: Room):
        if room.condition_to_enter is None:
            return True
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('The door is closed.')
        if not self.inventory:
            print('You have nothing on you to open the door.')
            return False
        print('What do you want to use?')
        obj_used = self.use_obj_inv(is_punch=False)
        if room.condition_to_enter == obj_used:
            print('You open the door with the ' + obj_used.value + '!')
            return True
        else:
            print('Nothing happen!')
            return False

    def action(self):
        self.meet_enemy()
        if not self.status:
            return None
        self.current_room.display()
        self.pick_obj()
        return self.current_room.action_room()

    def pick_obj(self):
        if self.current_room.obj_in_room is not None:
            print('Object found:')
            print('You found the ' + self.current_room.obj_in_room.value + '!')
            self.inventory.append(self.current_room.obj_in_room)
            self.current_room.delete_obj()

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

    def defeat_enemy(self):
        print('What do you want to use to fight him?')
        obj_used = self.use_obj_inv(is_punch=True)
        return self.current_room.enemy.is_win_fight(obj_used)

    def use_obj_inv(self, is_punch: bool = False):
        for iInv in range(len(self.inventory)):
            print(str(iInv+1) + ' - ' + self.inventory[iInv].value)
        if is_punch:
            print(str(len(self.inventory) + 1) + ' - Punch')
        while True:
            try:
                choice = int(input()) - 1
                if is_punch & choice == len(self.inventory):
                    choice = Obj.PUNCH
                else:
                    choice = self.inventory[choice]
                break
            except (ValueError, IndexError):
                print('Invalid object')
        return choice
