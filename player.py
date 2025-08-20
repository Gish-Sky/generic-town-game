class Player:
    def __init__(self, name):
        self.name = name
        self.funds = 5
        self.inventory = {}
    
    def pay(self, val):
        self.funds-=val
        if self.funds<0:
            self.funds=0
            
    def add(self, item):
        if item in self.inventory.keys():
            self.inventory[item]+=1
        else:
            self.inventory[item] = 1
    
    def getInventory(self):
        print("\n" + self.name + "'s inventory!")
        print("You have $" + str(self.funds) + ".00\n")
        if self.inventory.keys():
            for i in self.inventory.keys():
                print(i + ": " + str(self.inventory[i]))
    
    def finishChore(self):
        self.funds+=1