# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:21:24 2020.

@author: laura
"""


# IMPORTS

# DATA
discs = {1: {"num_positions": 13, "cur_position": 1},
         2: {"num_positions": 19, "cur_position": 10},
         3: {"num_positions": 3, "cur_position": 2},
         4: {"num_positions": 7, "cur_position": 1},
         5: {"num_positions": 5, "cur_position": 3},
         6: {"num_positions": 17, "cur_position": 5}}

# GOAL 1
"""Part of the sculpture is even interactive!
When a button is pressed, a capsule is dropped and tries to fall through
slots in a set of rotating discs to finally go through a little hole at the
bottom and come out of the sculpture. If any of the slots aren't aligned with
the capsule as it passes, the capsule bounces off the disc and soars away.
You feel compelled to get one of those capsules.

The discs pause their motion each second and come in different sizes;
they seem to each have a fixed number of positions at which they stop.
You decide to call the position with the slot 0, and count up for each
position it reaches next.

Furthermore, the discs are spaced out so that after you push the button,
one second elapses before the first disc is reached, and one second elapses
as the capsule passes from one disc to the one below it. So,
if you push the button at time=100, then the capsule reaches the top disc at
time=101, the second disc at time=102, the third disc at time=103, and so on.

The button will only drop a capsule at an integer time
- no fractional seconds allowed.

What is the first time you can press the button to get a capsule?"""

# ANSWER 1:
rem = []
mods = []
for i in discs:
    rem.append(discs[i]["cur_position"])
    mods.append(discs[i]["num_positions"])


for t in range(100000000):
    if (rem[0] + (t + 1)) % mods[0] == 0:
        if (rem[1] + (t + 2)) % mods[1] == 0:
            if (rem[2] + (t + 3)) % mods[2] == 0:
                if (rem[3] + (t + 4)) % mods[3] == 0:
                    if (rem[4] + (t + 5)) % mods[4] == 0:
                        if (rem[5] + t + 6) % mods[5] == 0:
                            print(f"You have to wait {t} seconds.")
                            break

# GOAL 2
"""After getting the first capsule (it contained a star! what great fortune!),
 the machine detects your success and begins to rearrange itself.

When it's done, the discs are back in their original configuration as if it
were time=0 again, but a new disc with 11 positions and starting at
position 0 has appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the
configuration in your puzzle input, what is the first time you can press
the button to get another capsule?"""

# ANSWER 2
discs[7] = {"num_positions": 11, "cur_position": 0}

rem = []
mods = []
for i in discs:
    rem.append(discs[i]["cur_position"])
    mods.append(discs[i]["num_positions"])

for t in range(100000000):
    if (rem[0] + (t + 1)) % mods[0] == 0:
        if (rem[1] + (t + 2)) % mods[1] == 0:
            if (rem[2] + (t + 3)) % mods[2] == 0:
                if (rem[3] + (t + 4)) % mods[3] == 0:
                    if (rem[4] + (t + 5)) % mods[4] == 0:
                        if (rem[5] + t + 6) % mods[5] == 0:
                            if (rem[6] + t + 7) % mods[6] == 0:
                                print(f"You have to wait {t} seconds.")
                                break