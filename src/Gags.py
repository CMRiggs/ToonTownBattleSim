

toonUpMilestones = [20, 200, 800, 2000, 6000]
trapMilestones = [20, 100, 800, 2000, 6000]
lureMilestones = [20, 100, 800, 2000, 6000]
soundMilestones = [40, 200, 1000, 2500, 7500]
throwMilestones = [10, 50, 400, 2000, 6000]
squirtMilestones = [10, 50, 400, 2000, 6000]
dropMilestones = [20, 100, 500, 2000, 6000]

class Gags:
    def __init__(self, name, exp, organic):
        """If gag track isn't owned set exp as -1"""
        self.name = name
        self.exp = exp
        self.organic = organic
