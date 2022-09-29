from Cog import getCogDefense

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