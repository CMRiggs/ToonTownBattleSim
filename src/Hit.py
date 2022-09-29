import math
from math import ceil
from math import floor

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