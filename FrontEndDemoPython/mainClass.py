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


directPathToMars = pathCost(0, 0, 0, ini["mapData"]["Mars"]["x"], ini["mapData"]["Mars"]["y"])
print("Cost1: " + str(directPathToMars))

# if directPathToMars > 30 :
pathToStation2 =  pathCost(0, 0, 0, ini["mapData"]["Station2"]["x"], ini["mapData"]["Station2"]["y"])
pathfromoStation2ToMars = pathCost(0, ini["mapData"]["Station2"]["x"], ini["mapData"]["Station2"]["y"], ini["mapData"]["Mars"]["x"], ini["mapData"]["Mars"]["y"])
TotalStation2 = pathfromoStation2ToMars + pathToStation2
print("Cost2: " + str(TotalStation2))

# if TotalStation2 > 30 :
pathToStation1 =  pathCost(0, 0, 0, ini["mapData"]["Station1"]["x"], ini["mapData"]["Station1"]["y"])
pathfromoStation1ToMars = pathCost(0, ini["mapData"]["Station1"]["x"], ini["mapData"]["Station1"]["y"], ini["mapData"]["Mars"]["x"], ini["mapData"]["Mars"]["y"])
TotalStation1 = pathfromoStation1ToMars + pathToStation1
print("Cost3: " + str(TotalStation1))
