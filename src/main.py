from Toon import Toon
from GagTrack import *
from Cog import Cog
from Battle import Battle


def main():
    toons = []
    cogs = []
    numToons = int(input("How many toons are in the battle?\n"))
    for i in range (1, numToons + 1):
        print("Please enter toon {} information".format(i))
        toonName = input("Toon Name?\n")
        toonLaff = input("Toon laff?\n")

        toonUpExp = int(input("Toon-Up Exp?\n"))
        trapExp = int(input("Trap Exp?\n"))
        lureExp = int(input("Lure Exp?\n"))
        soundExp = int(input("Sound Exp?\n"))
        throwExp = int(input("Throw Exp?\n"))
        squirtExp = int(input("Squirt Exp?\n"))
        dropExp = int(input("Drop Exp?\n"))

        organic = input("Which gag is organic?\n")

        toonUp = ToonUp(toonUpExp, False)
        trap = Trap(trapExp, False)
        lure = Lure(lureExp, False)
        sound = Sound(soundExp, False)
        throw = Throw(throwExp, False)
        squirt = Squirt(squirtExp, False)
        drop = Drop(dropExp, False)
        
        match organic:
            case "Toon-Up":
                toonUp = ToonUp(toonUpExp, True)
            case "Trap":
                trap = Trap(trapExp, True)
            case "Lure":
                lure = Lure(lureExp, True)
            case "Sound":
                sound = Sound(soundExp, True)
            case "Throw":
                throw = Throw(throwExp, True)
            case "Squirt":
                squirt = Squirt(squirtExp, True)
            case "Drop":
                drop = Drop(dropExp, True)
        toons.append(Toon(toonName, toonLaff, [toonUp, trap, lure, sound, throw, squirt, drop]))

    numCogs = int(input("How many Cogs are in the battle?\n"))
    for i in range (i, numCogs + 1):
        cogName = input("What is the Cog's name?\n")
        cogLevel = input("What is the Cog's level?\n")
        cogs.append(Cog(cogName, cogLevel))
    
    battle = Battle(toons, cogs)

if __name__ == "__main__":
    main()