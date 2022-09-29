from Toon import *
from GagTrack import *
from Cog import *

class Battle:
    def __init__(self, toons, cogs):
        """Toons and Cogs are both arrays of up to 4 toons/cogs objects.
        Index 0 represents the far right position"""
        self.toons = toons
        self.cogs = cogs
    
    def addToon(self, toon, idx):
        if (self.toons[idx] == None):
            self.toons[idx] = toon
    
    def removeToon(self, toon, idx):
        if (self.toons[idx] != None):
            self.toons[idx] == None
    
    def addCog(self, cog, idx):
        if (self.cogs[idx] == None):
            self.cogs[idx] = cog
    
    def removeCog(self, cog, idx):
        if (self.cogs[idx] != None):
            self.cogs[idx] = cog
    
    def calculate(self):
        # Go through all toon actions then go through all cog actions
        pass

def initialize():
    # Initialize values to defaults
    # Start with one toon and one cog
    toons = [Toon(), None, None, None]
    cogs = [Cog("Flunky", 1), None, None, None]
    battle = Battle(toons, cogs)