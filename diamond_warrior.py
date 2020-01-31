
# Diamond-Warrior Python-Based Text Game v1.0.0
# By Minseo Kang @ pulsar8k

# Language Written by English
# README on Reddit!

import os
print("* Reading data file...")
dataPath = "C:\\diamond-warrior\\data\\inventory.txt"
directoryPath = "C:\\diamond-warrior\\data"
data = []
diamond = 0
gold = 0
silver = 0
stone = 0
pLevel = 1
llevel = 1

def makeDirectory():
    try:
        if not (os.path.isdir(directoryPath)):
            print("* Installing Resources...")
            os.makedirs(os.path.join(directoryPath))
    except:
        print("* Failed to create directory.")
        raise


def readData():
    try:
        makeDirectory()
        f = open(dataPath, "r")
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
        f.close()
        return True
    except FileNotFoundError:
        print("* Cannot read data file. Maybe First Time?")
        fc = open(dataPath, "wt")
        fc.write("0\n0\n0\n0\n1\n1")
        fc.close()
        return False


if not readData():
    readData()
else:
    pass

# print(data)
diamond: int = data[0]
gold: int = data[1]
silver: int = data[2]
stone: int = data[3]
pLevel: int = data[4]
llevel: int = data[5]
# print('{},{},{},{},{},{}'.format(diamond, gold, silver, stone, pLevel, llevel))

print("Welcome Back, Diamond Warrior!")


def saveData():
    print("* Saving Changes...")
    fs = open(dataPath, "wt")
    fs.write("{Diamond}\n{Gold}\n{Silver}\n{Stone}\n{pLevel}\n{lLevel}".format(Diamond=diamond, Gold=gold, Silver=silver, Stone=stone, pLevel=pLevel, lLevel=llevel))
    fs.close()
    print("* Saving Successful.")
    import sys
    sys.exit()

def shop():
    global gold
    global pLevel
    global llevel
    while True:
        menu = input('''
# Your Gold : {Gold}
- Your Pickaxe Level : Lv {PickaxeCount}
- Your Luck Level : Lv {LuckCount}
[p] : Upgrade Pickaxe - Costs {pUp} Gold
[l] : Upgrade Luck - Costs {lUp} Gold
[Enter] : Back to Home
Enter :'''.format(Gold=gold, PickaxeCount=pLevel, LuckCount=llevel, pUp=2 ** pLevel, lUp=3 ** llevel))
        if menu == "":
            break
        elif menu == "p":
            if gold >= (2 ** pLevel):
                gold = gold - (2 ** pLevel)
                pLevel = pLevel + 1
                print("* Purchase; Pickaxe Upgrade Successful!")
            else:
                print("* Not Enough Gold")
        elif menu == "l":
            if gold >= (3 ** llevel):
                gold = gold - (3 ** llevel)
                llevel = llevel + 1
                print("* Purchase; Luck Upgrade Successful!")
            else:
                print("* Not Enough Gold")
    summonMenu()

def mine():
    global diamond
    global gold
    global silver
    global stone
    global pLevel
    global llevel
    import random
    import time
    mineTime = random.randrange(1, 7)
    print("* Mining...")
    time.sleep(mineTime)
    rDiamond = random.randrange(1, 100)
    cDiamond = random.randrange(1, 7)
    if rDiamond >= (95 - llevel + 1):
        diamond += (cDiamond + (2 * pLevel) - 2)
        print("> Diamond! {} Diamonds!!".format(cDiamond))
    else:
        pass
    rGold = random.randrange(1, 100)
    cGold = random.randrange(1, 17)
    if rGold >= (70 - llevel + 1):
        gold += (cGold + (2 * pLevel) - 2)
        print("> Gold! {} Golds!!".format(cGold))
    else:
        pass
    rSilver = random.randrange(1, 100)
    cSilver = random.randrange(1, 28)
    if rSilver >= (50 - llevel + 1):
        silver += (cSilver + (2 * pLevel) - 2)
        print("> Silver! {} Silvers!!".format(cSilver))
    else:
        pass
    cStone = random.randrange(1, 54)
    stone += cStone
    print("> Stone! {} Stones!!".format(cStone))
    summonMenu()

def summonMenu():
    menu = input('''
# Diamond : {Diamond}, Gold : {Gold}, Silver : {Silver}, Stone : {Stone}
[Enter] : Mine Minerals
[s] : Enter Shop
[.] : Save Changes & Quit
Enter :'''.format(Diamond=diamond, Gold=gold, Silver=silver, Stone=stone))
    if menu == "":
        mine()
    elif menu == "s":
        shop()
    elif menu == ".":
        saveData()
    else:
        summonMenu()
    pass

summonMenu()