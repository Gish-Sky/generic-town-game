import player
import random

class Vending:
    def __init__(self, choco: int, colas: int, popsicles: int):
        self.chocolate_bars = choco
        self.colas = colas
        self.popsicles = popsicles
        
    def getCola(self, player: player):
        if self.colas==0:
            player.pay(1)
            return "The vending machine rattles a bit, before a sad beeping noise escapes from a chute. Glancing inside, you realize that the vending machine has no colas."
        else:
            self.colas-=1
            player.pay(1)
            player.add("Cola")
            return "The vending machine excitedly beeps, before a cola slides out. Excitedly grabbing the can, you realize its eerily warm.\n Wait a second... and its flat? That's disappointing."

    def getChoco(self, player: player):
        if self.chocolate_bars==0:
            player.pay(1)
            return "The vending machine rattles a bit, before a sad beeping noise escapes from a chute. Glancing inside, you realize that the vending machine has no chocolate bars."
        else:
            self.chocolate_bars-=1
            player.pay(1)
            player.add("Chocolate")
            return "The vending machine excitedly beeps, before a chocolate bar tumbles into the chute. Excitedly grabbing the bar of candy, you realize its eerily warm.\n Wait a second... and its white chocolate? That's disappointing."

    def getPopsicle(self, player: player):
        if self.popsicles==0:
            player.pay(1)
            player.add("Token")
            return "The vending machine rattles a bit, before it begins to rapidly beep. Glancing around, you realize something's wrong with the machine. Before you run away, you hear a clattering noise and a silver coin falls out of the chute. Quickly grabbing it, you sprint away from the machine, not wanting to be blamed for another mishap."
        else:
            self.popsicles-=1
            player.pay(1)
            player.add("Popsicle")
            return "The vending machine beeps three times, before it dispenses a single popsicle. Reaching into the chute, you take out the popsicle. Its cherry flavored. Dang it, that's your least favorite flavor."
        
    def shake(self, player: player):
        player.pay(1)
        skibidi = random.randint(1, 2)
        if skibidi==2:
            return "The machine is firmly rooted into the ground. As you shake the machine, the machine angrily honks at you. Footsteps slowly grow louder and louder. Turning around, you see the policeman. He glares at you, before snatching the dollar bill out of your hand. He mutters something about some sort of Great Awakening, and how the town's better off with less kids. Strange."
        else:
            player.add("Token")
            return "The machine angrily beeps. Sadly, no chocolates, colas or popsicles fall, but a strange clinking noise fills the air. Glancing around, you poke your head into the chute and discover a strange silver coin. Taking it, you walk away from the machine, inspecting the token in your hand."
            