from abc import ABC

#For idx 3 and 4 the first number is used when the cog's rank is 1, second number otherwise
cogDefense = [-2, -5, -10, [-12, -15], [-15, -20], -25, -30, -40, -45, -50, -55]
cogs = ["Flunky", "Pencil Pusher", "Yesman", "Micro-manager", "Downsizer", "Head Hunter", "Corporate Raider", "The Big Cheese", #Boss bots
        "Bottom Feeder", "Bloodsucker", "Double Talker", "Ambulance Chaser", "Back Stabber", "Spin Doctor", "Legal Eagle", "Big Wig", #Law bots
        "Short Change", "Penny Pincher", "Tightwad", "Bean Counter", "Number Cruncher", "Money Bags", "Loan Shark", "Robber Baron", #Cash bots
        "Cold Caller", "Tele-marketer", "Name Dropper", "Glad Hander", "Mover & Shaker", "Two-Face", "The Mingler", "Mr. Hollywood"] #Sell bots

class Cog (ABC):
    def __init__(self, name, level):
        self.name = name
        for i,v in enumerate(cogs):
            if name == v:
                self.rank = (i % 8) + 1
                self.type = int(i / 8)

        if (self.rank + 4 < level) or (self.rank > level):
            raise Exception("Invalid level for cog type.")
    
        match self.type:
            case 0:
                self.type = "Bossbot"
            case 1:
                self.type = "Lawbot"
            case 2:
                self.type = "Cashbot"
            case 3:
                self.type = "Sellbot"
        self.level = level
        if level != 12:
            self.maxHealth = (level + 1) * (level + 2)
        else:
            self.maxHealth = 200