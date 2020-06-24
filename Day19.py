# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:08:57 2020.

@author: laura
"""

# IMPORTS
import math
from collections import deque

# DATA
data = 3004953

# GOAL 1
"""Each Elf brings a present. They all sit in a circle,
numbered starting with position 1. Then, starting with the first Elf,
they take turns stealing all the presents from the Elf to their left.
An Elf with no presents is removed from the circle and does not take turns.

With the number of Elves given in your puzzle input,
which Elf gets all the presents?"""

# ANSWER 1
# https://www.youtube.com/watch?v=uCsD3ZGzMgE Numberphile Josephus problem

# find closest power of 2
def find_closest_power_of_two(n):
    """Find closest power of two smaller than the target value"""
    return int(math.log(n, 2))


power_of_two = find_closest_power_of_two(data)

diff = data - 2 ** power_of_two

winner = 1  # default winner in the problem at powers of 2
for i in range(diff):
    winner += 2

print(f"Elf {winner} will get all presents.")


# GOAL 2
"""Realizing the folly of their present-exchange rules,
the Elves agree to instead steal presents from the Elf directly across
the circle. If two Elves are across the circle, the one on the left
(from the perspective of the stealer) is stolen from.
The other rules remain unchanged: Elves with no presents are removed
from the circle entirely, and the other elves move in slightly to keep
the circle evenly spaced.

With the number of Elves given in your puzzle input,
which Elf now gets all the presents?"""

# ANSWER 2
elves = list(range(1, data + 1))

# create two lists with elves, keep in mind the second is in reversed order
lst1 = deque(elves[:(data // 2)])
lst2 = deque(reversed(elves[(data // 2):]))

while lst1 and lst2:
    if len(lst1) > len(lst2):
        lst1.pop()
    else:
        lst2.pop()

    # switch stealing elf
    lst2.appendleft(lst1.popleft())
    lst1.append(lst2.pop())

if len(lst1) == 0:
    answer = lst2[0]
else:
    answer = lst1[0]

print(f"In the second round, elf {answer} gets all presents.")
