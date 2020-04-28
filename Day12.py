# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:18:32 2020.

@author: laura
"""

# IMPORTS

# DATA
data = []
with(open("Data - Day12.txt")) as f:
    for line in f:
        data.append(line.strip())

"""The assembunny code you've extracted operates on four registers
(a, b, c, and d) that start at 0 and can hold any integer.
However, it seems to make use of only a few instructions:

cpy x y copies x (either an integer or the value of a register) into register y.
inc x increases the value of register x by one.
dec x decreases the value of register x by one.
jnz x y jumps to an instruction y away
(positive means forward; negative means backward), but only if x is not zero.

The jnz instruction moves relative to itself:
    an offset of -1 would continue at the previous instruction,
    while an offset of 2 would skip over the next instruction."""

i = 0
registers = {"a": 0, "b": 0, "c": 0, "d": 0}

def get_answer(registers, i=0):
    while True:
        if i == 23:
            break

        instruction = data[i]

        if "cpy" in instruction:
            value = instruction.split()[1]
            reg = instruction.split()[2]
            if value in ["a", "b", "c", "d"]:
                registers[reg] = registers[value]
            else:
                registers[reg] = int(value)
            i += 1
        elif "inc" in instruction:
            reg = instruction.split()[1]
            registers[reg] += 1
            i += 1
        elif "dec" in instruction:
            reg = instruction.split()[1]
            registers[reg] -= 1
            i += 1
        elif "jnz" in instruction:
            reg = instruction.split()[1]
            offset = int(instruction.split()[2])
            if reg in ["a", "b", "c", "d"]:
                if registers[reg] != 0:
                    i += offset
                else:
                    i += 1
            else:
                if int(reg) != 0:
                    i += offset
                else:
                    i += 1
        else:
            print("Conflicting instructions")

    print(f"The value left in register a is {registers['a']}")

get_answer(registers)

# GOAL 2
"""As you head down the fire escape to the monorail,
you notice it didn't start;
register c needs to be initialized to the position of the ignition key.

If you instead initialize register c to be 1,
what value is now left in register a?"""

registers2 = {"a": 0, "b": 0, "c": 1, "d": 0}
get_answer(registers2)