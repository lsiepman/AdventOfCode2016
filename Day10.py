# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:55:14 2020.

@author: laura
"""

# IMPORTS
import pandas as pd
# DATA
data = []
with(open("Data - Day10.txt")) as f:
    for line in f:
        data.append(line.strip())

"""You come upon a factory in which many robots are zooming around handing
 small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when
 it has two microchips, and once it does, it gives each one to a different
 bot or puts it in a marked "output" bin. Sometimes, bots take microchips
 from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a
 single number; the bots must use some logic to decide what to do with
 each chip. You access the local control computer and download the bots'
 instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should
 be given to a specific bot; the rest of the instructions indicate what a
 given bot should do with its lower-value or higher-value chip.


Based on your instructions,
what is the number of the bot that is responsible for comparing value-61
microchips with value-17 microchips?"""

# ANSWER 1
def find_bot_instructions(data):
    bot_manual = {}
    for i in data:
        inst = i.split(" ")
        if inst[0] == "bot":
            content = {"low": f"{inst[5]} {inst[6]}",
                       "high": f"{inst[10]} {inst[11]}",
                       "values": []}
            dict_name = f"{inst[0]} {inst[1]}"

            bot_manual[dict_name] = content

    return bot_manual

def list_values(data):
    values = []
    for i in data:
        inst = i.split(" ")
        if inst[0] == "value":
            values.append(i)

    return values

def initial_chips(bot_manual, values):
    for i in values:
        inst = i.split(" ")
        bot_given = f"{inst[4]} {inst[5]}"
        val = int(inst[1])

        bot_manual[bot_given]["values"].append(val)

    return bot_manual

def compare_chips(bot_instructions):
    loop = True
    while loop:
        for i in bot_instructions:
            if len(bot_instructions[i]["values"]) == 2:
                low = min(bot_instructions[i]["values"])
                high = max(bot_instructions[i]["values"])

                if low == 17 and high == 61:
                    print("The answer is", i)
                    loop = False
                    break

                low_goes = bot_instructions[i]["low"]
                high_goes = bot_instructions[i]["high"]
                bot_instructions[i]["values"] = []

                bot_instructions[low_goes]["values"].append(low)
                bot_instructions[high_goes]["values"].append(high)



bot_instructions = find_bot_instructions(data)
val_instructions = list_values(data)
bot_instructions = initial_chips(bot_instructions, val_instructions)
compare_chips(bot_instructions)

# GOAL 2
"""What do you get if you multiply together the values of one chip
in each of outputs 0, 1, and 2?"""

# ANSWER 2
def find_outputs(bot_instructions):
    for i in range(21):
        bot_instructions[f"output {i}"] = {"values": []}

    loop = True
    while loop:
        for i in bot_instructions:
            if len(bot_instructions[i]["values"]) == 2:
                low = min(bot_instructions[i]["values"])
                high = max(bot_instructions[i]["values"])

                if (
                    len(bot_instructions["output 0"]["values"]) > 0 and
                    len(bot_instructions["output 1"]["values"]) > 0 and
                    len(bot_instructions["output 2"]["values"]) > 0
                    ):
                    answer = (bot_instructions["output 0"]["values"][0]
                    * bot_instructions["output 1"]["values"][0]
                    * bot_instructions["output 2"]["values"][0])

                    print("The answer is", answer)
                    loop = False
                    break

                low_goes = bot_instructions[i]["low"]
                high_goes = bot_instructions[i]["high"]
                bot_instructions[i]["values"] = []

                bot_instructions[low_goes]["values"].append(low)
                bot_instructions[high_goes]["values"].append(high)



bot_instructions = find_bot_instructions(data)
val_instructions = list_values(data)
bot_instructions = initial_chips(bot_instructions, val_instructions)
find_outputs(bot_instructions)