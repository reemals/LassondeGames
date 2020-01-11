import request
import numpy as np
import sys
import mats

def main():
    data = request.createInstance()
    print(data)

       
if __name__ == '__main__':
    main()

map = mats.mat()
ini = request.getData()

print(ini)

#true is y

def pathCost(cost,current_x, current_y, x,y):
    while(x != current_x or  y != current_y ):
        if (y != current_y ):
            if map[current_x, current_y +1] != -100 :
                cost = cost + 1
                current_y =  current_y + 1
            else:
                cost = cost + 8
                current_y_ = current_y + 2

        elif x != current_x  :
            if map[current_x +1, current_y ] != -100 :
                cost = cost + 1
                current_x = current_x + 1
            else:
                cost = cost + 8
                current_x = current_x + 2

    return cost

def moveToMars():
    ini = request.getData()
    while (ini["location"]["x"] != ini["mapData"]["Mars"]["x"] or ini["location"]["y"] != ini["mapData"]["Mars"]["y"]):
        ini = request.getData()
        if (ini["location"]["y"] != ini["mapData"]["Mars"]["y"]):
                if map[ini["location"]["x"], ini["location"]["y"] + 1] != -100:
                    request.turn("N")
                    request.move(1)
                else:
                    mats.asteroid(map)
        elif ini["mapData"]["Mars"]["x"] != ini["location"]["x"]:
                if map[ini["location"]["x"]+1, ini["location"]["y"] ] != -100:
                    request.turn("E")
                    request.move(1)
                else:
                    request.turn("E")
                    mats.asteroid(map)
    request.finish()

def moveToStation1():
    ini = request.getData()
    while (ini["location"]["x"] != ini["mapData"]["Station1"]["x"] or ini["location"]["y"] != ini["mapData"]["Station1"]["y"]):
        ini = request.getData()
        if (ini["location"]["y"] != ini["mapData"]["Station1"]["y"]):
            if map[ini["location"]["x"], ini["location"]["y"] + 1] != -100:
                request.turn("N")
                request.move(1)
            else:
                mats.asteroid(map)
        elif ini["mapData"]["Station1"]["x"] != ini["location"]["x"]:
            if map[ini["location"]["x"] + 1, ini["location"]["y"]] != -100:
                request.turn("E")
                request.move(1)
            else:
                request.turn("E")
                mats.asteroid(map)

    request.refuel()

    ini = request.getData()
    while (ini["location"]["x"] != ini["mapData"]["Mars"]["x"] or ini["location"]["y"] != ini["mapData"]["Mars"]["y"]):
        ini = request.getData()
        if (ini["location"]["y"] != ini["mapData"]["Mars"]["y"]):
            if map[ini["location"]["x"], ini["location"]["y"] + 1] != -100:
                request.turn("N")
                request.move(1)
            else:
                mats.asteroid(map)
        elif ini["mapData"]["Mars"]["x"] != ini["location"]["x"]:
            if map[ini["location"]["x"] + 1, ini["location"]["y"]] != -100:
                request.turn("E")
                request.move(1)
            else:
                request.turn("E")
                mats.asteroid(map)
    request.finish()


def moveToStation2():
    ini = request.getData()
    while (ini["location"]["x"] != ini["mapData"]["Station2"]["x"] or ini["location"]["y"] != ini["mapData"]["Station2"]["y"]):
        ini = request.getData()
        if (ini["location"]["y"] != ini["mapData"]["Station2"]["y"]):
            if map[ini["location"]["x"], ini["location"]["y"] + 1] != -100:
                request.turn("N")
                request.move(1)
            else:
                mats.asteroid(map)
        elif ini["mapData"]["Station2"]["x"] != ini["location"]["x"]:
            if map[ini["location"]["x"] + 1, ini["location"]["y"]] != -100:
                request.turn("E")
                request.move(1)
            else:
                request.turn("E")
                mats.asteroid(map)

    request.refuel()

    ini = request.getData()
    while (ini["location"]["x"] != ini["mapData"]["Mars"]["x"] or ini["location"]["y"] != ini["mapData"]["Mars"]["y"]):
        ini = request.getData()
        if (ini["location"]["y"] != ini["mapData"]["Mars"]["y"]):
            if map[ini["location"]["x"], ini["location"]["y"] + 1] != -100:
                request.turn("N")
                request.move(1)
            else:
                mats.asteroid(map)
        elif ini["mapData"]["Mars"]["x"] != ini["location"]["x"]:
            if map[ini["location"]["x"] + 1, ini["location"]["y"]] != -100:
                request.turn("E")
                request.move(1)
            else:
                request.turn("E")
                mats.asteroid(map)
    request.finish()

pathChosen = 0

directPathToMars = pathCost(0, 0, 0, ini["mapData"]["Mars"]["x"], ini["mapData"]["Mars"]["y"])
print("Cost1: " + str(directPathToMars))
pathChosen = 1
pathToStation2 = 0
pathfromoStation2ToMars = 0
TotalStation2 = 0
if directPathToMars > 30 :
    pathToStation2 =  pathCost(0, 0, 0, ini["mapData"]["Station2"]["x"], ini["mapData"]["Station2"]["y"])
    pathfromoStation2ToMars = pathCost(0, ini["mapData"]["Station2"]["x"], ini["mapData"]["Station2"]["y"], ini["mapData"]["Mars"]["x"], ini["mapData"]["Mars"]["y"])
    TotalStation2 = pathfromoStation2ToMars + pathToStation2
    print("Cost2 pathToStation2: " + str(pathToStation2))
    print("Cost2 pathfromoStation2ToMars: " + str(pathfromoStation2ToMars))
    print("Cost2 TotalThroughStation2: " + str(TotalStation2))
    pathChosen = 2

pathToStation1 = 0
pathfromoStation1ToMars = 0
TotalStation1 = 0
if pathToStation2 > 30 or pathfromoStation2ToMars > 30:
    pathToStation1 =  pathCost(0, 0, 0, ini["mapData"]["Station1"]["x"], ini["mapData"]["Station1"]["y"])
    pathfromoStation1ToMars = pathCost(0, ini["mapData"]["Station1"]["x"], ini["mapData"]["Station1"]["y"], ini["mapData"]["Mars"]["x"], ini["mapData"]["Mars"]["y"])
    TotalStation1 = pathfromoStation1ToMars + pathToStation1
    print("Cost3 pathToStation1: " + str(pathToStation1))
    print("Cost3 pathfromoStation1ToMars: " + str(pathfromoStation1ToMars))
    print("Cost3 TotalThroughStation1: " + str(TotalStation1))
    pathChosen = 3

print("pathChosen: " + str(pathChosen))

if pathChosen == 1:
    moveToMars()
elif pathChosen == 3:
    moveToStation1()
else:
    moveToStation2()
