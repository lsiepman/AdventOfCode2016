# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:50:12 2020.

@author: laura
"""


# IMPORTS
import pandas as pd

# DATA
data = pd.DataFrame({"F1": {"Generators": ["Tm", "Sr", "Pu"], "Chips": ["Tm"], "Elevator": True},
                     "F2": {"Generators": [], "Chips": ["Pu", "Sr"], "Elevator": False},
                     "F3": {"Generators": ["Pm", "Ru"], "Chips": ["Pm", "Ru"], "Elevator": False},
                     "F4": {"Generators": [], "Chips": [], "Elevator": False }}).T
# GOAL 1
"""
In other words, if a chip is ever left in the same area as another RTG, and
it's not connected to its own RTG, the chip will be fried. Therefore, it is
assumed that you will follow procedure and keep chips connected to their
corresponding RTG when they're in the same room, and away from other RTGs
otherwise.

Within the radiation-shielded part of the facility (in which it's safe to have
these pre-assembly RTGs), there is an elevator that can move between the four
floors. Its capacity rating means it can carry at most yourself and two RTGs or
microchips in any combination. (They're rigged to some heavy diagnostic
equipment - the assembling machine will detach it for you.)
As a security measure, the elevator will only function if it contains at least
one RTG or microchip. The elevator always stops on each floor to recharge, and
this takes long enough that the items within it and the items on that floor can
irradiate each other. (You can prevent this if a Microchip and its Generator
end up on the same floor in this way, as they can be connected while the
elevator is recharging.)

When you enter the containment area, you and the elevator will start on the
first floor.

In your situation, what is the minimum number of steps required to
bring all of the objects to the fourth floor?"""

# ANSWER 1
"""Reasoning:
    if 2 items on F1: 1 movement to move all 1 floor
    if 4 items on F1: 5 movements to move all 1 floor
    if 6 items on F1: 9 movements needed
    if 8 itemd on f1: 13 movements needed
    if 10 items on f1: 17 movements needed

    so: for every 2 items extra, 4 extra movements are needed.

Also, if it is necessary to move 2 items down (for safety),
2 movements are added.
"""
# SO (num items per floor, to be moved:)
f1 = 4
f2 = 2 + f1
f3 = 4 + f2

def calc_answer_1(num_items, num_movements):
    if num_items == 2:
        num_movements += 1
    elif num_items == 4:
        num_movements += 5
    elif num_items == 6:
        num_movements += 9
    elif num_items == 8:
        num_movements += 13
    elif num_items == 10:
        num_movements += 17
    else:
        print("unexpected num items")

    return num_movements

x = calc_answer_1(f1, 0)
x = calc_answer_1(f2, x)
answer1 = calc_answer_1(f3, x)
print(f"The minimum number of movements is {answer1}")

# GOAL 2
"""Upon entering the isolated containment area, however,
you notice some extra parts on the first floor that weren't
listed on the record outside:

    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.

These work just like the other generators and microchips.
You'll have to get them up to assembly as well.

What is the minimum number of steps required to bring all of the objects,
including these four new ones, to the fourth floor?"""

# ANSWER 2
def calc_answer_2(num_items, num_movements):
    if num_items == 2:
        num_movements += 1
    elif num_items == 4:
        num_movements += 5
    elif num_items == 6:
        num_movements += 9
    elif num_items == 8:
        num_movements += 13
    elif num_items == 10:
        num_movements += 17
    elif num_items == 12:
        num_movements += 21
    elif num_items == 14:
        num_movements += 25
    else:
        print("unexpected num items")

    return num_movements

# new floor values
f1 = 4 + 4
f2 = 2 + f1
f3 = 4 + f2

x = calc_answer_1(f1, 0)
x = calc_answer_1(f2, x)
answer2 = calc_answer_2(f3, x)
print(f"The minimum number of movements is {answer2}")