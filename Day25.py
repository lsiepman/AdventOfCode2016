# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:18:14 2020.

@author: laura
"""


# IMPORTS

# DATA
data = []
with(open("Data - Day25.txt")) as f:
    for line in f:
        data.append(line.strip())

# GOAL 1
"""This antenna code, being a signal generator, uses one extra instruction:
    - out x transmits x (either an integer or the value of a register)
    as the next value for the clock signal.
The code takes a value (via register a) that describes the signal to generate,
but you're not sure how it's used. You'll have to find the input to produce the
right signal through experimentation.

What is the lowest positive integer that can be used to initialize
register a and cause the code to output a clock signal of 0, 1, 0, 1...
repeating forever?
"""

# ANSWER 1
"""Manual Analysis

------------------------------------------------------------------------------
cpy a d
cpy 15 c
cpy 170 b <------
inc d <-----    |           loops simplify to d = a + (15 * 170) = a + 2550
dec b      |    |
jnz b -2 ---    |
dec c           |
jnz c -5 -------
------------------------------------------------------------------------------

cpy d a                      copy new value of d into a
jnz 0 0
------------------------------------------------------------------------------

cpy a b
cpy 0 a
cpy 2 c <----------------
jnz b 2 --- <--         |
jnz 1 6   |   |         |    loops simplify to c = 2 - (a % 2) and a = a / 2
dec b   <--   |         |
dec c         |         |
jnz c -4 ------         |
inc a                   |
jnz 1 -7 ----------------
------------------------------------------------------------------------------

cpy 2 b
jnz c 2 -- <--------
jnz 1 4  | ----    |
dec b <---    |    |       loops simplify to b = 2 - c
dec c         |    |
jnz 1 -4      | ----
jnz 0 0 <------
out b

------------------------------------------------------------------------------
jnz a -19                   This loop will run until a equals 0
jnz 1 -21                   This loop doesn't end

So in short:
- The code multiplies 15 * 170 = 2550. This is stored in d
- a = a / 2, to set up the a value for the next iteration (so in the first
round, a = d, then the second round a = a / 2). When a reaches 0, the initial
d values is again copied into a, creating a never ending loop.
- If a equals and even number, a % 2 = 0, so c = 2 and b = 0. Otherwise, b = 1


"""
def test_input(target):
    num  = 1
    while num < target:
        if num % 2 == 0:
            num = num * 2 + 1
        else:
            num = num * 2
    return num - target

print(f"The lowest possible integer that can initiate the loop is {test_input(2550)}")
