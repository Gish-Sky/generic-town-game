from player import Player
from vending import Vending
import random
from chores import Chores

print("Welcome to the vending machine game! Today, you'll be a kid who wants a lot of snacks from the vending machine.")
print("Unfortunately, it costs money to get stuff from the vending machine, but your mom has allowed you to do a few chores to get more money for more snacks!")
print("Let's get started!")

name = input("What's your name? ")

# Setup
the_player = Player(name)
chores = Chores()
lst = []
for i in range(0, 3):
    lst.append(random.randint(1, 4))
vending_machine = Vending(lst[0], lst[1], lst[2])

print("Welcome " + name + "!")
print("Please select from the following options:")
print("[1] Visit the vending machine!")
print("[2] Do a chore to earn more money!")
print("[3] Exit the game. (We'll miss you!)")
the_input = '1'
while the_input in ['1', '2', '3', '4']:
    the_input = input("What would you like to do?\n [1] - Visiting the vending machine\n [2] - Do a chore\n [3] - Leave\n [4] - View Inventory\n")
    match the_input:
        case '1':
            print("The vending machine waves hello. Or rather, it makes some pleasant beeping noises, as if it was glad to see you again.")
            if the_player.funds<=0:
                print("Looking into your pocket, you sigh. Looks like you're out of money. Making a sad noise, you trot away from the vending machine, disappointed.")
                print("Even the vending machine seems sad too.")
            else:
                print("What would you like from the vending machine?")
                options = input("[1] For chocolate\n [2] For cola\n [3] For popsicle\n [4] Sur... surprise me?\n")
                match options:
                    case "1":
                        print(vending_machine.getChoco(the_player))
                    case "2":
                        print(vending_machine.getCola(the_player))
                    case "3":
                        print(vending_machine.getPopsicle(the_player))
                    case _:
                        print(vending_machine.shake(the_player))
        case '2':
            print("Walking home, you open the door. Its quiet, as always. Things just haven't been the same, since the mayor bombed the town hall.")
            print("Anyways, you want snacks. Glancing around, you find...")
            chores.doChore(the_player)
        case '3':
            print("Glancing around, you decide to leave town. Slinging your backpack over your shoulder, you follow the dirt path that leads to the town's entrance.")
            print("Strangely enough, it leads to a forest this time... You don't remember the forest being there.")
            print("Oh well, you follow the trail...")
            break
        case '4':
            the_player.getInventory()
        
print("So... you tried to leave or do something weird. Unfortunately, as you step into the forest, following the dirt path, you hear the familiar hum of the carpenter's saw.")
print("Following that noise... You enter town... Again?")
print("Thank you for playing!")