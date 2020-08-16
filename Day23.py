# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:45:54 2020.

@author: laura
"""

# IMPORTS
import math

# DATA
data = []
with(open("Data - Day23.txt")) as f:
    for line in f:
        data.append(line.strip())

data2 = data.copy()

# GOAL 1
"""The safe has a digital screen and keypad for code entry.
A sticky note attached to the safe has a password hint on it: "eggs".
The painting is of a large rabbit coloring some eggs. You see 7.

Now, you just need to figure out what output the keypad would have sent to the
safe. You extract the assembunny code from the logic chip (your puzzle input).

The code looks like it uses almost the same architecture and instruction set that the monorail computer used! You should be able to use the same assembunny interpreter for this as you did there, but with one new instruction:

tgl x toggles the instruction x away (pointing at instructions
like jnz does: positive means forward; negative means backward):

- For one-argument instructions, inc becomes dec, and all other one-argument
 instructions become inc.
- For two-argument instructions, jnz becomes cpy, and all other
two-instructions become jnz.
- The arguments of a toggled instruction are not affected.
- If an attempt is made to toggle an instruction outside the program,
nothing happens.
- If toggling produces an invalid instruction (like cpy 1 2) and an
attempt is later made to execute that instruction, skip it instead.
- If tgl toggles itself (for example, if a is 0, tgl a would target itself
and become inc a), the resulting instruction is not executed until the next
time it is reached.

The rest of the electronics seem to place the keypad entry
(the number of eggs, 7) in register a, run the code,
and then send the value left in register a to the safe.

What value should be sent to the safe?
"""

# ANSWER 1
i = 0
registers = {"a": 7, "b": 0, "c": 0, "d": 0}

def get_answer(registers, max_i, data = data, i=0):
    while True:
        if i == max_i:
            break

        instruction = data[i]

        if "tgl" in instruction:
            reg = instruction.split()[1]
            offset = registers[reg]
            value = i + offset


            if value < 0 or value >= max_i:
                i += 1
            else:
                toggled = data[value]
                if "inc" in toggled:
                    toggled = toggled.replace("inc", "dec")
                    data[value] = toggled

                elif "dec" in toggled:
                    toggled = toggled.replace("dec", "inc")
                    data[value] = toggled

                elif "tgl" in toggled:
                    toggled = toggled.replace("tgl", "inc")
                    data[value] = toggled

                elif "cpy" in toggled:
                    toggled = toggled.replace("cpy", "jnz")
                    data[value] = toggled

                elif "jnz" in toggled:
                    toggled = toggled.replace("jnz", "cpy")
                    data[value] = toggled

                i += 1

        elif "cpy" in instruction:
            value = instruction.split()[1]
            reg = instruction.split()[2]

            if reg not in ["a", "b", "c", "d"]:
                pass
            elif value in ["a", "b", "c", "d"]:
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
            offset = instruction.split()[2]

            if offset in ["a", "b", "c", "d"]:
                offset = registers[offset]
            else:
                offset = int(offset)

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

example = ["cpy 2 a", "tgl a", "tgl a", "tgl a", "cpy 1 a", "dec a", "dec a"]
get_answer(registers, data = data, max_i = len(data))

# GOAL 2
"""The safe doesn't open, but it does make several angry noises to express its
frustration.

You're quite sure your logic is working correctly, so the only other thing is...
you check the painting again. As it turns out, colored eggs are still eggs.
Now you count 12.

As you run the program with this new input,
the prototype computer begins to overheat. You wonder
what's taking so long, and whether the lack of any instruction
more powerful than "add one" has anything to do with it. Don't
bunnies usually multiply?

Anyway, what value should actually be sent to the safe?"""

# ANSWER 2
answer1 = 12492
constant = answer1 - math.factorial(7)

answer2 = math.factorial(12) + constant

print(f"The second answer equals {answer2}")
