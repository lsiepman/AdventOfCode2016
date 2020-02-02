# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:18:01 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
#%% DATA
data = []
with(open("Data - Day03.txt", "r")) as file:
    for line in file:
        data.append(line.split())

data = pd.DataFrame(data)
data[[0,1,2]] = data[[0,1,2]].astype(int)
#%% GOAL 1
"""Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?"""
#%% SOLUTION 1
def TriangleValid(data):
    valid = []
    for i in range(len(data)):
        side1 = data[0][i]
        side2 = data[1][i]
        side3 = data[2][i]
        
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            valid.append(True)
        else:
            valid.append(False)
        
    data["valid"] = valid
    
    return data
    
data = TriangleValid(data)
print("Answer:", sum(data["valid"]))
#%% GOAL 2
"""Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?"""
#%% SOLUTION 2
def FindGroups(data):
    side1 = []
    side2 = []
    side3 = []

    for column in data.columns[:3]:
        i = 0
        while i < len(data):
           side1.append(int(data[column][i]))
           side2.append(int(data[column][i+1]))
           side3.append(int(data[column][i+2]))
            
           i += 3
           
    new = pd.DataFrame(list(zip(side1, side2, side3)))
    return new

data2 = FindGroups(data)
data2 = TriangleValid(data2)
print("Answer2:", sum(data2["valid"]))
