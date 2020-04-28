# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:41:53 2020.

@author: laura
"""

# IMPORTS
import re
import numpy as np
from collections import deque

# DATA
fav_num = 1352

# GOAL 1
"""Every location in this area is addressed by a pair of non-negative integers
(x,y). Each such coordinate is either a wall or an open space.
You can't move diagonally. The cube maze starts at (0,0) and seems to extend
infinitely toward positive x and y; negative values are invalid, as they
represent a location outside the building. You are in a small waiting area
at (1,1).

While it seems chaotic, a nearby morale-boosting poster explains,
the layout is actually quite logical.
You can determine whether a given x,y coordinate will be a wall or an
open space using a simple system:

- Find x*x + 3*x + 2*x*y + y + y*y.
- Add the office designer's favorite number (your puzzle input).
- Find the binary representation of that sum;
count the number of bits that are 1.
    - If the number of bits that are 1 is even, it's an open space.
    - If the number of bits that are 1 is odd, it's a wall.

What is the fewest number of steps required for you to reach 31,39?
"""
# ANSWER 1

def determine_if_open(coordinates, fav_num=1352):
    x = coordinates[0]
    y = coordinates[1]

    calc_formula = x * x + 3 * x + 2 * x * y + y + y * y
    calc_formula += fav_num

    binary_represent = bin(calc_formula)
    num = re.search(r"(\d+)$", binary_represent).group()

    result = 0
    for i in list(num):
        result += int(i)

    if (result % 2) == 0:
        return True
    else:
        return False

def create_grid(x_max, y_max):
    grid = np.zeros((x_max, y_max), dtype=bool)
    for x in range(0, x_max):
        for y in range(0, y_max):
            grid[y,x] = determine_if_open((x,y))
    return grid

def walk_grid(grid, start_pos, goal):
    queue = deque([[start_pos]])
    seen = set([start_pos])
    height = width = len(grid)

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == goal[0] and y == goal[1]:
            print(f"The shortest path has {len(path) - 1} steps.")

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= x2 < width and 0 <= y2 < height
                    and grid[y2][x2] and (x2, y2) not in seen):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


grid = create_grid(50, 50)
walk_grid(grid, (1,1), (31,39))

# GOAL 2
"""How many locations (distinct x,y coordinates,
including your starting location) can you reach in at most 50 steps?"""

# ANSWER 2
def walk_50_steps(grid, start_pos):
    queue = deque([[start_pos]])
    seen = set([start_pos])
    height = width = len(grid)

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if len(path) == 51:
            print(f"After 50 steps, you can visit {len(seen)} unique location")
            break

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (0 <= x2 < width and 0 <= y2 < height
                    and grid[y2][x2] and (x2, y2) not in seen):
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

grid = create_grid(60, 60)
walk_50_steps(grid, (1,1))

