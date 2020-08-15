# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:49:14 2020.

@author: laura
"""

# IMPORTS
import pandas as pd
import re

# DATA
data = pd.read_csv("Data - Day22.txt", sep = r"\s+", skiprows = 1)

# GOAL 1
"""You gain access to a massive storage cluster arranged in a grid;
each storage node is only connected to the four nodes directly adjacent to it
(three if the node is on an edge, two if it's in a corner).

You can directly access data only on node /dev/grid/node-x0-y0,
but you can perform some limited actions on the other nodes:

    - You can get the disk usage of all nodes (via df).
    The result of doing this is in your puzzle input.
    - You can instruct a node to move (not copy) all of its data to an
    adjacent node (if the destination node has enough space to receive the
    data). The sending node is left empty after this operation.

Nodes are named by their position: the node named node-x10-y10 is adjacent
to nodes node-x9-y10, node-x11-y10, node-x10-y9, and node-x10-y11.

Before you begin, you need to understand the arrangement of data on these nodes.
Even though you can only move data between directly connected nodes,
you're going to need to rearrange a lot of the data to get access to the
data you need. Therefore, you need to work out how you might be able to
shift data around.

To do this, you'd like to count the number of viable pairs of nodes.
A viable pair is any two nodes (A,B), regardless of whether they are
directly connected, such that:

    - Node A is not empty (its Used is not zero).
    - Nodes A and B are not the same node.
    - The data on node A (its Used) would fit on node B (its Avail).

How many viable pairs of nodes are there?"""

# ANSWER 1
data["node_num"] = data.index

def find_vialable_pairs(data):
    viable_pairs = []

    # check all pairs
    for idx in range(len(data)):
        A = data.loc[idx]
        A_used = int(A.Used.replace("T", ""))

        if A_used > 0:
            for j in range(len(data)):
                B = data.loc[j]
                B_avail = int(B.Avail.replace("T", ""))

                if B_avail >= A_used:
                    viable_pairs.append((A.node_num, B.node_num))

    # remove all duplicates
    viable_pairs = [i for i in viable_pairs if i[0] != i[1]]

    return viable_pairs

pairs = find_vialable_pairs(data)
print(f"Answer 1 is {len(pairs)}")

# GOAL 2
"""Now that you have a better understanding of the grid, it's time to get to work.

Your goal is to gain access to the data which begins in the node
with y=0 and the highest x [32] (that is, the node in the top-right corner).

What is the fewest number of steps required to move your goal data to node-x0-y0?
"""

# create map
map_data = pd.DataFrame("", columns = range(0, 30), index = range(0,30))

for i in range(len(data)):
    node = data.loc[i]

    # find map coordinates
    x = int(re.search(r"x([0-9]+)", node.Filesystem).group(1))
    y = int(re.search(r"y([0-9]+)", node.Filesystem).group(1))

    # determine token
    used = int(node.Used.replace("T", ""))

    if used > 400:
        token = "#"
    elif used == 0:
        token = "_"
    else:
        token = "."

    if x == 0 and y == 0:
        token = "H" # for Home
    elif x == 32 and y == 0:
        token = "G" # for Goal
    else:
        token = token

    # add token to map
    map_data.loc[y, x] = token

map_data.to_csv("Day22_map.csv")
