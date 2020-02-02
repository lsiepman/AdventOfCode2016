# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:06:03 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import re
import operator
import numpy as np
#%% DATA
data = ["R5", "R4", "R2", "L3", "R1", "R1", "L4", "L5", "R3", "L1", "L1", "R4", "L2", "R1", "R4", "R4", "L2", "L2", "R4", "L4", "R1", "R3", "L3", "L1", "L2", "R1", "R5", "L5", "L1", "L1", "R3", "R5", "L1", "R4", "L5", "R5", "R1", "L185", "R4", "L1", "R51", "R3", "L2", "R78", "R1", "L4", "R188", "R1", "L5", "R5", "R2", "R3", "L5", "R3", "R4", "L1", "R2", "R2", "L4", "L4", "L5", "R5", "R4", "L4", "R2", "L5", "R2", "L1", "L4", "R4", "L4", "R2", "L3", "L4", "R2", "L3", "R3", "R2", "L2", "L3", "R4", "R3", "R1", "L4", "L2", "L5", "R4", "R4", "L1", "R1", "L5", "L1", "R3", "R1", "L2", "R1", "R1", "R3", "L4", "L1", "L3", "R2", "R4", "R2", "L2", "R1", "L5", "R3", "L3", "R3", "L1", "R4", "L3", "L3", "R4", "L2", "L1", "L3", "R2", "R3", "L2", "L1", "R4", "L3", "L5", "L2", "L4", "R1", "L4", "L4", "R3", "R5", "L4", "L1", "L1", "R4", "L2", "R5", "R1", "R1", "R2", "R1", "R5", "L1", "L3", "L5", "R2"]

data = pd.DataFrame(data, columns = ["all"])
#%% GOAL 1
"""You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?"""

#%% CALC 1
def FindTurn(string):
    return re.search(r"[A-Z]", string).group()

def FindBlocks(string):
    return re.search(r"[0-9]+", string).group()

def FindDirection(data):
    d = "N"
    direction = []
    for i in data["turn"]:
        
        if d == "N":
            if i == "R":
                d = "E"
            else: d = "W"
            
        elif d == "E":
            if i == "R":
                d = "S"
            else: d = "N"
        
        elif d == "S":
           if i == "R":
               d = "W"
           else: d = "E"   
       
        elif d == "W":
            if i == "R":
                d = "N"
            else: d = "S"
            
        direction.append(d)
        
    data["direction"] = direction
    
    return data

def Walk(data):
    location = (0,0)
    coordinates = []
    
    for i in range(len(data)):
        d = data["direction"][i]
        b = data["blocks"][i]
        if d == "N":
            move = (0, b)
        elif d == "S":
            move = (0, -b)
        elif d == "W":
            move = (-b, 0)
        elif d == "E":
            move = (b, 0)
            
        location = tuple(map(operator.add, location, move))
        coordinates.append(location)
        
    data["coordinates"] = coordinates
    
    return data

data["turn"] = data["all"].apply(FindTurn)
data["blocks"] = data["all"].apply(FindBlocks)
data["blocks"] = data["blocks"].astype(int)
data = FindDirection(data)
data = Walk(data)

print("Blocks:", np.abs(data["coordinates"][146][1]) + data["coordinates"][146][0])

#%% GOAL 2
"""Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?"""

#%% CALC 2
def WalkBlocks(data):
    location = (0,0)
    coordinates = []
    
    for i in range(len(data)):
        d = data["direction"][i]
        b = data["blocks"][i]
        
        for j in range(b):
            if d == "N":
                move = (0, 1)
            elif d == "S":
                move = (0, -1)
            elif d == "W":
                move = (-1, 0)
            elif d == "E":
                move = (1, 0)
            
            location = tuple(map(operator.add, location, move))
            coordinates.append(location)
    
    return coordinates

def FindDuplicates(coordinate_list):
    return set([x for x in coordinate_list if coordinate_list.count(x) > 1])
    
all_locations = WalkBlocks(data)
dups = list(FindDuplicates(all_locations))

print("Blocks", np.abs(dups[0][0]) + np.abs(dups[0][1]))

