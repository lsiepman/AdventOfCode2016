# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:44:03 2020.

@author: laura
"""

# IMPORTS
import pandas as pd

# DATA
data = []
with(open("Data - Day20.txt")) as file:
    for line in file:
        data.append(line.strip())

data = pd.DataFrame(data)
data = data[0].str.split("-", expand=True)
data.columns = ["from", "to"]

data["from"] = pd.to_numeric(data["from"])
data["to"] = pd.to_numeric(data["to"])

# GOAL 1
"""You've retrieved the list of blocked IPs from the firewall,
but the list seems to be messy and poorly maintained,
and it's not clear which IPs are allowed.
Also, rather than being written in dot-decimal notation,
they are written as plain 32-bit integers, which can have any value
from 0 through 4294967295, inclusive.

The blacklist specifies ranges of IPs
(inclusive of both the start and end value) that are not allowed.

Given the list of blocked IPs you retrieved from the firewall
(your puzzle input), what is the lowest-valued IP that is not blocked?"""

# ANSWER 1
sorted_data = data.sort_values(by="from").reset_index(drop=True)

min_value = sorted_data["from"][0]
max_value = sorted_data["to"][0]

# find the largest value in "to", knowing the "from" lies within the current range
for i in sorted_data.index:
    if (
            sorted_data["from"][i] <= max_value + 1 and
            sorted_data["to"][i] > max_value
        ):
        max_value = sorted_data["to"][i]


print(f"The answer is {max_value + 1}.")

# GOAL 2
"""How many IPs are allowed by the blacklist?"""

# ANSWER 2
min_value = sorted_data["from"][0]
max_value = sorted_data["to"][0]

# find the largest value in "to", knowing the "from" lies within the current range
allowed = []
while max_value < 4294967295:
    for i in sorted_data.index:
        if (
                sorted_data["from"][i] <= max_value + 1 and
                sorted_data["to"][i] > max_value
            ):
            max_value = sorted_data["to"][i]

    max_value += 1
    allowed.append(max_value)

print(f"There are {len(allowed)-1} allowed values.")
