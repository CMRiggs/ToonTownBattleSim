from GagTrack import *

class Toon:
    def __init__(self):
        """Gags is always an array of 7 GagTrack objects."""
        # Initialize toon name to "TOON"
        self.name = "TOON"

        # Initialize laff to minimum values
        self.laff = 15
        self.maxLaff = 15

        # Initialize gags to minimum exp
        self.gags = [ToonUp(0, False), Trap(0, False), Lure(0, False),
                    Sound(0, False), Throw(0, False), Squirt(0, False),
                    Drop(0, False)]

        # No organic by default
        self.organic = None

        # No action by default (the gag the toon will use in the calculator)
        action = None
    
    # Set the toons action to the given action
    def setAction(self, action):
        self.action = action

    # Set the exp of all GagTracks to 10000
    def maxGags(self):
        for _,v in self.gags():
            v.exp = 10000
    
    # Set the exp of all GagTracks to 0
    def minGags(self):
        for _,v in self.gags():
            v.exp = 0
    
    # Set a GagTrack to organic
    def setOrganic(self, gagTrack):
        pass
    