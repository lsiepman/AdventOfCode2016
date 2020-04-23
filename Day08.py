# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:15:16 2020

@author: laura
"""

# IMPORTS
import re
import numpy as np
import pandas as pd

# DATA
data = []
with(open("Data - Day08.txt")) as file:
    for line in file:
        data.append(line)

# GOAL 1
"""You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of requirements
telephone.

To get past the door, you first swipe a keycard (no problem; there was one on
 a nearby desk). Then, it displays a code on a little screen, and you type that
 code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes,
you've taken everything apart and figured out how it works.
Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions
for the screen; these instructions are your puzzle input.
The screen is 50 pixels wide and 6 pixels tall, all of which start off,
and is capable of three somewhat peculiar operations:

- rect AxB turns on all of the pixels in a rectangle at the top-left of
the screen which is A wide and B tall.
- rotate row y=A by B shifts all of the pixels in row A
(0 is the top row) right by B pixels.
Pixels that would fall off the right end appear at the left end of the row.
- rotate column x=A by B shifts all of the pixels in column A
(0 is the left column) down by B pixels.
Pixels that would fall off the bottom appear at the top of the column.
"""

# ANSWER 1
array = np.zeros((6, 50), dtype=bool)

for line in data:
    split_line = re.split(r"[ =]", line)

    if split_line[0] == "rect":
        width, height = map(int, split_line[1].split('x'))
        array[:height, :width] = True

    elif split_line[0] == "rotate":
        if split_line[1] == "row":
            rotate_loc = int(split_line[3])
            rotate_by = int(split_line[5])
            array[rotate_loc] = np.roll(array[rotate_loc], rotate_by)
        else:
            rotate_loc = int(split_line[3])
            rotate_by = int(split_line[5])
            array[:, rotate_loc] = np.roll(array[:, rotate_loc], rotate_by)

print(f"{np.sum(array)} pixels are lit.")

# GOAL 2
"""You notice that the screen is only capable of displaying capital letters;
in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?"""

# ANSWER 2
#use variable explorer in IDE
print("ZFHFSFOGPO")
