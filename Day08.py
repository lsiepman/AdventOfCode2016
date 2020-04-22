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
data = pd.DataFrame(data)
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
def find_action(string):
    """Discovers which action should be taken."""
    if "rect" in string:
        action = "rect"
    elif "rotate row" in string:
        action = "rotate row"
    elif "rotate column" in string:
        action = "rotate column"
    else:
        action = "unknown"
    return action


def find_rect_cordinates(string, return_val):
    """For all rect actions, discover the exact rectangle to be switched on."""
    if "rect" in string:
        coordinate1 = int(re.search(r"(\d)x", string).group(1))
        coordinate2 = int(re.search(r"x(\d)", string).group(1))
    else:
        coordinate1 = np.nan
        coordinate2 = np.nan

    if return_val == 1:
        return coordinate1
    elif return_val == 2:
        return coordinate2
    else:
        print("No values are returned")


def find_rotate_loc(string):
    """Find the rotate locations."""
    if "rotate" in string:
        rotate_loc = int(re.search(r"[xy]=(\d)", string).group(1))
    else:
        rotate_loc = np.nan

    return rotate_loc


def find_rotate_by(string):
    """Find how much to rotate."""
    if "rotate" in string:
        rotate_by = int(re.search(r"by\s(\d)", string).group(1))
    else:
        rotate_by = np.nan

    return rotate_by


def switch_pixels_on(array, data, row_idx):
    """Switch pixels on."""
    width = int(data["Rect_cor1"].iloc[row_idx])
    height = int(data["Rect_cor2"].iloc[row_idx])

    array[0:height, 0:width] = 1

    return array

def rotate_pixels(array, data, row_idx, column=True):
    """Rotate pixels."""
    rot_loc = int(data["Rotate_location"].iloc[row_idx])
    rot_by = int(data["Rotate_by"].iloc[row_idx])

    if column:
        array[:, rot_loc] = np.roll(array[:, rot_loc], rot_by, axis=0)
    else:
        array[rot_loc, :] = np.roll(array[rot_loc, :], rot_by, axis=1)

    return array

def perform_action(data, array):
    pass

data["Action"] = data[0].apply(find_action)
data["Rect_cor1"] = data[0].apply(find_rect_cordinates, return_val=1)
data["Rect_cor2"] = data[0].apply(find_rect_cordinates, return_val=2)
data["Rotate_location"] = data[0].apply(find_rotate_loc)
data["Rotate_by"] = data[0].apply(find_rotate_by)

array = np.zeros((6, 50))
array = perform_action(data, array)
print(f"{np.sum(array)} pixels are lit.")
