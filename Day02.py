# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:31:22 2020

@author: laura
"""

#%% IMPORTS
import operator
#%% DATA
data = []
with(open("Data - Day02.txt", "r")) as file:
    for line in file:
        data.append(line)
#%% GOAL 1
"""You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?
"""

#%% SOLUTION 1
instructions = []
for i in range(len(data)):
    instructions.append(list(data[i]))
    
def FindLoc(instructions):
    location = [0,0]
    locations = []
    for i in instructions:
        for j in i:
            if j == "U":
                move = [0, 1]
            elif j == "R":
                move = [1, 0]
            elif j == "L": 
                move = [-1, 0]
            elif j == "D":
                move = [0, -1]
            
            location = list(map(operator.add, location, move))
            
            if location[0] == 2:
                location[0] = 1
            elif location[0] == -2:
                location[0] = -1
            
            if location[1] == 2:
                location[1] = 1
            elif location[1] == -2:
                location[1] = -1
                
        locations.append(location)
    return locations

def ConvertLoc(locs):
    numbers = []
    for i in locs:
        if i == [-1, 1]:
            n = 1
        elif i == [0, 1]:
            n = 2
        elif i == [1, 1]:
            n = 3
        elif i == [-1, 0]:
            n = 4
        elif i == [0, 0]:
            n = 5
        elif i == [1, 0]:
            n = 6
        elif i == [-1, -1]:
            n = 7
        elif i == [0, -1]:
            n = 8
        elif i == [1, -1]:
            n = 9
        numbers.append(str(n))
    print("code:", "".join(numbers))
    
ConvertLoc(FindLoc(instructions))

#%% GOAL 2
"""You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D
    
So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?
"""

#%% SOLUTION 2
def FindLoc2(instructions, location = [-2, 0]):
        
    locations = []
    for i in instructions:  
        for j in i:
            if j == "U" and location not in [[-2,0], [-1,1], [0,2], [1,1], [2,0]]:
                move = [0, 1]
            elif j == "R" and location not in [[0,2], [1,1], [2,0], [1,-1], [0,-2]]:
                move = [1, 0]
            elif j == "L" and location not in [[0,2], [-1,1], [-2,0], [-1,-1], [0, -2]]: 
                move = [-1, 0]
            elif j == "D" and location not in [[-2,0], [-1,-1], [0,-2], [1,-1], [2,0]]:
                move = [0, -1]
            else:
                move = [0,0]

            location = list(map(operator.add, location, move))                    
                
        locations.append(location)

    return locations

def ConvertLoc2(locs):
    numbers = []
    for i in locs:
        if i == [0, 2]:
            n = 1
        elif i == [-1, 1]:
            n = 2
        elif i == [0, 1]:
            n = 3
        elif i == [1, 1]:
            n = 4
        elif i == [-2, 0]:
            n = 5
        elif i == [-1, 0]:
            n = 6
        elif i == [0, 0]:
            n = 7
        elif i == [1, 0]:
            n = 8
        elif i == [2, 0]:
            n = 9
        elif i == [-1, -1]:
            n = "A"
        elif i == [0, -1]:
            n = "B"
        elif i == [1, -1]:
            n = "C"
        elif i == [0, -2]:
            n = "D"
        else:
            n = "unknown"
        numbers.append(str(n))
    print("code2:", "".join(numbers))
    
ConvertLoc2(FindLoc2(instructions))

