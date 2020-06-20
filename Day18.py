# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:12:33 2020.

@author: laura
"""

# GOAL 1
"""The tiles are arranged into rows that are all the same width;
you take note of the safe tiles (.) and traps (^) in the first row
(your puzzle input). The type of tile (trapped or safe) in each row is based on
the types of the tiles in the same position, and to either side of that
position, in the previous row. (If either side is off either end of the row,
 it counts as "safe" because there isn't a trap embedded in the wall.)

 Let's call these three tiles from the previous row the left, center,
 and right tiles, respectively. Then, a new tile is a trap only in one of
 the following situations:

- Its left and center tiles are traps, but its right tile is not.
- Its center and right tiles are traps, but its left tile is not.
- Only its left tile is a trap.
- Only its right tile is a trap.

In any other situation, the new tile is safe.

Starting with the map in your puzzle input,
in a total of 40 rows (including the starting row),
how many safe tiles are there?"""

# DATA
data = """.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"""

data = list(data)


# ANSWER 1
total = []
total.append(data)


def find_new_row(prev_row):
    """Determines the values in the next row."""
    new_row = []
    for i, j in enumerate(prev_row):
        if i == 0:
            left = "."
        else:
            left = prev_row[i - 1]

        center = j

        if i == 99:
            right = "."
        else:
            right = prev_row[i + 1]

        if right == "." and center == "." and left == "^":
            val = "^"
        elif right == "^" and center == "." and left == ".":
            val = "^"
        elif right == "^" and center == "^" and left == ".":
           val = "^"
        elif right == "." and center == "^" and left == "^":
            val = "^"
        else:
            val = "."

        new_row.append(val)

    return new_row

for i in range(39):
    data = find_new_row(data)
    total.append(data)

flat_list = [item for sublist in total for item in sublist]
print(f"The room contains {flat_list.count('.')} safe tiles")

# GOAL 2
"""How many safe tiles are there in a total of 400000 rows?"""

# ANSWER 2:
data = """.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"""
data = list(data)
total = []
total.append(data)

for i in range(400000-1):
    data = find_new_row(data)
    total.append(data)

flat_list = [item for sublist in total for item in sublist]
print(f"The larger room contains {flat_list.count('.')} safe tiles")
