# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:30:12 2020.

@author: laura
"""


# IMPORTS
import numpy as np
from collections import deque
from itertools import permutations

# DATA
data = []
with(open("Data - Day24.txt")) as f:
    for line in f:
        data.append(line.strip())


# GOAL 1
"""You extract the duct layout for this area from some blueprints you acquired
and create a map with the relevant locations marked (your puzzle input).
0 is your current location, from which the cleaning robot embarks;
the other numbers are (in no particular order) the locations the robot
needs to visit at least once each. Walls are marked as #, and open passages
are marked as `.`. Numbers behave like open passages.
"""

# ANSWER 1
# create grid
grid = []
for i in data:
    line = []
    for symbol in i:
        if symbol == '#':
            line.append(-1)
        else:
            line.append(0)
    grid.append(line)

to_see = {}
for num, line in enumerate(data):
    for n, char in enumerate(line):
        if char not in ["#", "."]:
            to_see[int(char)] = (num, n)

num_locations = [to_see[x] for x in sorted(to_see.keys())]

# functions
def walk(grid, goal, loc, to):
    next = []
    for x,y in goal:
        grid[x][y] = loc

        for (ax, ay) in (x-1, y),(x+1, y),(x, y-1),(x, y+1):
            if (ax, ay) == to:
                return loc
            if grid[ax][ay] != 0:
                continue
            if (ax, ay) not in next:
                next.append((ax, ay))

    return walk(grid, next, loc+1, to)


def walk_grid(grid, from_, to):
    return walk([x[:] for x in grid], [from_], 1, to)


def calc_paths(to_see):
    paths = {}
    perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7]))
    perms = [i for i in perms if i[0] == 0]
    for i in perms:
        dist = 0
        dist += to_see[(i[0], i[1])]
        dist += to_see[(i[1], i[2])]
        dist += to_see[(i[2], i[3])]
        dist += to_see[(i[3], i[4])]
        dist += to_see[(i[4], i[5])]
        dist += to_see[(i[5], i[6])]
        dist += to_see[(i[6], i[7])]

        paths[i] = dist

    return paths

# prepare gridwalking
distance = {}
for i in range(len(num_locations) - 1):
  for j in range(i + 1, len(num_locations)):
    to_see[(i,j)] = to_see[(j,i)] = walk_grid(grid, num_locations[i], num_locations[j])

path_lengths = calc_paths(to_see)
print(f"The minimum path length is equal to {min(path_lengths.values())}")


# GOAL 2
"""Of course, if you leave the cleaning robot somewhere weird,
someone is bound to notice.
What is the fewest number of steps required to start at 0,
visit every non-0 number marked on the map at least once,
and then return to 0?"""

# ANSWER 2
def calc_paths_with_return(to_see):
    paths = {}
    perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 0]))
    perms = [i for i in perms if i[0] == 0 and i[8] == 0]
    for i in perms:
        dist = 0
        dist += to_see[(i[0], i[1])]
        dist += to_see[(i[1], i[2])]
        dist += to_see[(i[2], i[3])]
        dist += to_see[(i[3], i[4])]
        dist += to_see[(i[4], i[5])]
        dist += to_see[(i[5], i[6])]
        dist += to_see[(i[6], i[7])]
        dist += to_see[(i[7], i[8])]

        paths[i] = dist

    return paths

paths_2 = calc_paths_with_return(to_see)
print(f"The minimum path length with return: {min(paths_2.values())}")
