from world import World


print('Welcome to Text Adventure Game - v0.1')
name = input('What is your name?')
print('Hi ' + name + ' A little girl have disappear! Can you find him in the manor ?')
input('Press enter to start your quest!')
my_world = World(name)
my_world.run_game()
