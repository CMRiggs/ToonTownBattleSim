from math import floor, ceil

from GagTrack import *
from Cog import Cog, getCogDefense

class Battle:
    def __init__(self, toons, cogs):
        """Toons and Cogs are both arrays of up to 4 toons/cogs objects.
        Index 0 represents the far right position"""
        self.toons = toons
        self.cogs = cogs

def singleCogAccuracy(cog, gags, idxs, prevHits):
    """Gags is the gag track/exp of all gags being used. Idxs is an array
    saying which gag in the track is being used. gags and idxs should be
    the same length. prevHits is the amount of times the cog has been hit
    already in the turn"""
    # Lowest propAcc is selected among all gags
    propAcc = 100
    # Highest trackExp bonus is selected among all gags
    trackExp = 0

    # Go through every gag being used and find min propAcc and max trackExp
    for i,v in enumerate(idxs):
        propAcc = min(gags[i].accuracy[v], propAcc)
        # Search list from top to bottom keeping original indexes
        for j,b in reversed(list(enumerate(gags[i].expMilestones))):
            if (b <= gags[i].exp):
                trackExp = max(j*10,trackExp)
                break

    tgtDef = getCogDefense(cog.rank, cog.level)
    # No lure ratio bonus because singleCog
    bonus = prevHits * 20
    atkAcc = propAcc + trackExp + tgtDef + bonus

    # Max and min accuracy
    if atkAcc > 95:
        return 95
    if atkAcc < 5:
        return 5
    return atkAcc
    
def groupCogAccuracy(cogs, gags, idxs, prevHits):
    # Lowest propAcc is selected among all gags
    propAcc = 100
    # Highest trackExp bonus is selected among all gags
    trackExp = 0

    # Go through every gag being used and find min propAcc and max trackExp
    for i,v in enumerate(idxs):
        propAcc = min(gags[i].accuracy[v], propAcc)
        # Search list top from bottom keeping original indexes
        for j,b in reversed(list(enumerate(gags[i].expMilestones))):
            if (b <= gags[i].exp):
                trackExp = max(j*10,trackExp)
                break

    tgtDef = 0
    cogsLured = 0
    for _,v in enumerate(cogs):
        tgtDef = min(getCogDefense(v.rank, v.level), tgtDef)
        if v.lured == True:
            cogsLured += 1
    # No lure ratio bonus because singleCog
    bonus = prevHits * 20

    level7TS = False # Check for level 7 throw/squirt
    for i,v in enumerate(gags):
        if ((v.type == "Throw") or (v.type == "Squirt")) and (idxs[i] == 6):
            level7TS = True
            
    # Lure ratio applies to sound and level 7 throw/squirt
    if (gags[0].type == "Sound") or (level7TS):
        bonus += (cogsLured/len(cogs))*100

    atkAcc = propAcc + trackExp + tgtDef + bonus

    # Max and min accuracy
    if atkAcc > 95:
        return 95
    if atkAcc < 5:
        return 5
    return int(atkAcc)

def toonUpAccuracy(gag, idx):
    propAcc = gag.accuracy[idx]
    for i,v in reversed(list(enumerate(gag.expMilestones))):
            if (v <= gag.exp):
                trackExp = i*5
                break
    
    atkAcc = propAcc + trackExp
    if atkAcc > 95:
        return 95
    if atkAcc < 5:
        return 5
    return atkAcc

def lureDamage(damage):
    """Lured cogs take 1.5 damage from throw and squirt, this check
    needs to be made before this is called"""
    return ceil(damage * 1.5)

def comboDamage(dmgs):
    """Dmgs is an array of the damage numbers gotten from
    damageCalculation. Multiple of the same gag (2 throw)
    get a combo bonus."""
    return ceil(sum(dmgs) * 1.2)

def damageCalculation(gag, idx):
    """Calculates the damage of an individual gag on a cog
    Gag is the gag object the gag being used belongs to
    idx is the index of the gag (ex. cupcake = 0, wedding cake = 6)"""   
    # These gags don't deal damage
    if (gag.type == "Lure") or (gag.type == "Toon-Up"):
        return 0

    # At level 7 gags everything does max damage
    if (idx == 6) or (gag.exp == 10000):
        return gag.damages[idx][1]

    # If next gag has been unlocked gag does max damage
    if (gag.exp >= gag.expMilestones[idx + 1]):
        return gag.damages[idx][1]
    
    unlockExp = gag.expMilestones[idx]
    nextUnlockExp = gag.expMilestones[idx + 1]
    minDmg = gag.damages[idx][0]
    maxDmg = gag.damages[idx][1]
    pointsToNextStep = (nextUnlockExp - unlockExp + 1) / (maxDmg - minDmg + 1)

    damage = floor((gag.exp - unlockExp) / (pointsToNextStep) + minDmg)
    return damage
    
    # Could potentially be used in place of organic, but TTR patches
    # to things like trap could prevent that
    #bonus = int(damage * 0.1)
    #if (bonus < 1) and (damage > 0):
    #    bonus = 1
    #damage += bonus
    #return damage