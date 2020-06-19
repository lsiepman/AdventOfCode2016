# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:06:29 2020.

@author: laura
"""

# IMPORTS
import hashlib
from collections import deque

# DATA
data = "njfxhljp"

# GOAL 1
"""You're trying to access a secure vault protected by a 4x4 grid of small
rooms connected by doors. You start in the top-left room (marked S),
and you can access the vault (marked V) once you reach the bottom-right room

The doors in your current room are either open or closed (and locked) based on
the hexadecimal MD5 hash of a passcode (your puzzle input) followed by a
sequence of uppercase characters representing the path you have taken so far
(U for up, D for down, L for left, and R for right).

Only the first four characters of the hash are used;
they represent, respectively, the doors up, down, left, and right
from your current position. Any b, c, d, e, or f means that the corresponding
door is open; any other character (any number or a) means that the
corresponding door is closed and locked

Given your vault's passcode, what is the shortest path
(the actual path, not just the length) to reach the vault?

#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |
####### V
"""


def find_hash(string):
    """Find the md5 hash of a string."""
    hashed = hashlib.md5(string.encode("utf8"))
    hashhex = hashed.hexdigest()

    return hashhex[:4]


def walk_maze(password):
    """Walk the maze in order to reach the vault."""
    # Create log for the path
    queue = deque()
    queue.append(('', 0, 0))

    while queue:
        path, x, y = queue.popleft()  # find current path and position

        # The vault is located at x = 3 and y = 3 in a 4x4 grid, with 0-index.
        if x == 3 and y == 3:
            yield path
            continue

        opn = ("b", "c", "d", "e", "f")  # letters that signify "open"

        hashhex = find_hash(password + path)  # find the current code

        # add the current move to the path to be hashed
        if hashhex[0] in opn and y > 0:
            queue.append((path + "U", x, y - 1))
        if hashhex[1] in opn and y < 3:
            queue.append((path + "D", x, y + 1))
        if hashhex[2] in opn and x > 0:
            queue.append((path + "L", x - 1, y))
        if hashhex[3] in opn and x < 3:
            queue.append((path + "R", x + 1, y))


print(f"The first answer is {next(walk_maze(data))}")

# GOAL 2
"""What is the length of the longest path that reaches the vault?"""

for item in walk_maze(data):
    pass
    answer2 = len(item)

print(f"The second anwer is {answer2}")
