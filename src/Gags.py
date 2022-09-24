from abc import ABC

class Gags(ABC):
    def __init__(self, exp, expMilestones, damages, accuracy, target, type):
        """If gag track isn't owned set exp as -1"""
        self.exp = exp
        self.expMilestones = expMilestones
        self.damages = damages
        self.accuracy = accuracy
        self.target = target
        self.type = type

class ToonUp(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            # Each array represents the min and max damage of a gag. The lowest level gag is index 0.
            toonUpDamages = [[8, 10],[15, 18],[27, 30],[40, 45],[50, 60],[75, 105],[210, 210]]
        else:
            toonUpDamages = [[11, 11],[19, 19],[33, 33],[49, 49],[55, 66],[82, 115],[231, 231]]
        
        toonUpAccuracy = [70, 70, 70, 70, 70, 70, 95]

        # sToon means single toon, gToon means group of toons
        toonUpTargets = ["sToon", "gToon", "sToon", "gToon", "sToon", "gToon", "gToon"]

        toonUpExpMilestones = [0, 20, 200, 800, 2000, 6000, 10000]
        super().__init__(exp, toonUpExpMilestones, toonUpDamages, toonUpAccuracy, toonUpTargets, "Toon-Up")

class Trap(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            # Each array represents the min and max damage of a gag. The lowest level gag is index 0.
            trapDamages = [[10, 12],[18, 20],[30, 35],[45, 50],[75, 85],[90, 180],[200, 200]]
        else:
            trapDamages = [[11, 13],[19, 22],[33, 38],[49, 55],[83, 93],[99, 198],[220, 220]]

        trapAccuracy = [0, 0, 0, 0, 0, 0, 0]

        # sCog means single cog, gCog means group of cogs
        trapTargets = ["sCog", "sCog", "sCog", "sCog", "sCog", "sCog", "gCog"]
        trapExpMilestones = [0, 20, 100, 800, 2000, 6000, 10000]
        super().__init__(exp, trapExpMilestones, trapDamages, trapAccuracy, trapTargets, "Trap")
    

class Lure(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            # Damage is set to the amount of rounds lure lasts
            lureDamages = [[2,2],[2,2],[3,3],[3,3],[4,4],[4,4],[8,8]]
            lureAccuracy = [50, 50, 60, 60, 70, 70, 95]
        else:
            lureDamages = [[2,2],[2,2],[3,3],[3,3],[4,4],[4,4],[8,8]]
            lureAccuracy = [60, 60, 70, 70, 80, 80, 95]

        lureTargets = ["sCog", "gCog", "sCog", "gCog", "sCog", "gCog", "gCog"]
        lureExpMilestones = [0, 20, 100, 800, 2000, 6000, 10000]
        super().__init__(exp, lureExpMilestones, lureDamages, lureAccuracy, lureTargets, "Lure")
    

class Sound(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            soundDamages = [[3,4],[5,7],[9,11],[14,16],[19,21],[25,50],[90,90]]
        else:
            soundDamages = [[4,5],[6,8],[10,12],[15,17],[20,23],[27,55],[99,99]]

        soundAccuracy = [95,95,95,95,95,95,95]

        soundTargets = ["gCog", "gCog", "gCog", "gCog", "gCog", "gCog", "gCog"]
        soundExpMilestones = [0, 40, 200, 1000, 2500, 7500, 10000]
        super().__init__(exp, soundExpMilestones, soundDamages, soundAccuracy, soundTargets, "Sound")
    

class Throw(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            throwDamages = [[4,6],[8,10],[14,17],[24,27],[36,40],[48,100],[120,120]]
        else:
            throwDamages = [[5,7],[9,11],[15,18],[26,29],[39,44],[52,110],[132,132]]

        throwAccuracy = [75,75,75,75,75,75,75]

        throwTargets = ["sCog", "sCog", "sCog", "sCog", "sCog", "sCog", "gCog"]
        throwExpMilestones = [0, 10, 50, 400, 2000, 6000, 10000]
        super().__init__(exp, throwExpMilestones, throwDamages, throwAccuracy, throwTargets, "Throw")
    

class Squirt(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            squirtDamages = [[3,4],[6,8],[10,12],[18,21],[27,30],[36,80],[105,105]]
        else:
            squirtDamages = [[4,5],[7,9],[11,13],[19,23],[29,33],[39,88],[115,115]]

        squirtAccuracy = [95,95,95,95,95,95,95]

        squirtTargets = ["sCog", "sCog", "sCog", "sCog", "sCog", "sCog", "gCog"]
        squirtExpMilestones = [0, 10, 50, 400, 2000, 6000, 10000]
        super().__init__(exp, squirtExpMilestones, squirtDamages, squirtAccuracy, squirtTargets, "Squirt")
    

class Drop(Gags):
    def __init__(self, exp, organic):
        if (organic == False):
            dropDamages = [[10,10],[18,18],[30,30],[45,45],[60,70],[85,170],[180,180]]
        else:
            dropDamages = [[11,11],[19,19],[33,33],[49,49],[66,77],[93,187],[198,198]]

        dropAccuracy = [50,50,50,50,50,50,50]

        dropTargets = ["sCog", "sCog", "sCog", "sCog", "sCog", "sCog", "gCog"]
        dropExpMilestones = [0, 20, 100, 500, 2000, 6000, 10000]
        super().__init__(exp, dropExpMilestones, dropDamages, dropAccuracy, dropTargets, "Drop")