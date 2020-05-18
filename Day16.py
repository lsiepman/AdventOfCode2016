# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:55:04 2020.

@author: laura
"""

# IMPORTS

# DATA
data = "10001110011110000"

# GOAL 1
"""Start with an appropriate initial state (your puzzle input).
Then, so long as you don't have enough data yet to fill the disk,
repeat the following steps:

- Call the data you have at this point "a".
- Make a copy of "a"; call this copy "b".
- Reverse the order of the characters in "b".
- In "b", replace all instances of 0 with 1 and all 1s with 0.
- The resulting data is "a", then a single 0, then "b".

Repeat these steps until you have enough data to fill the desired disk.

The first disk you have to fill has length 272. Using the initial state in
your puzzle input, what is the correct checksum?
"""

# ANSWER 1
def reverse_string(string):
    return string[::-1]

def swap_string(string):
    new_string = ["0"]
    for i in string:
        if i == "0":
            new_string.append("1")
        else:
            new_string.append("0")

    return "".join(new_string)

def combine_strings(old, new):
    return old + new

def execute_functions(string):
    rev_string = reverse_string(string)
    swapped_string = swap_string(rev_string)

    return combine_strings(string, swapped_string)

def find_checksum(string):
    pairs = [string[i:i + 2] for i in range(0, len(string), 2)]

    checksum = []
    for i in pairs:
        if i == "10" or i == "01":
            checksum.append("0")
        else:
            checksum.append("1")

    checksum = "".join(checksum)

    if len(checksum) % 2 == 0:
        checksum = find_checksum(checksum)

    return checksum


while len(data) < 272:
    data = execute_functions(data)

data = data[:272]
checksum = find_checksum(data)

print(f"The first answer is {checksum}")

# GOAL 2
"""The second disk you have to fill has length 35651584.
Again using the initial state in your puzzle input,
what is the correct checksum for this disk?"""

# ANSWER 2
data = "10001110011110000"

while len(data) < 35651584:
    data = execute_functions(data)

data = data[:35651584]
checksum = find_checksum(data)

print(f"The second answer is {checksum}")