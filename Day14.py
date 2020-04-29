# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:46:19 2020.

@author: laura
"""

# IMPORTS
import re
from hashlib import md5

# DATA
data = "zpqevtbw"
# data = "abc"
# GOAL 1
"""To generate keys, you first get a stream of random data by taking the MD5
of a pre-arranged salt (your puzzle input) and an increasing integer index
(starting with 0, and represented in decimal); the resulting MD5 hash should
be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for
your one-time pad. A hash is a key only if:

- It contains three of the same character in a row, like 777.
Only consider the first such triplet in a hash.
- One of the next 1000 hashes in the stream contains that same
character five times in a row, like 77777.

Given the actual salt in your puzzle input,
what index produces your 64th one-time pad key?
"""

valid_key_idx = []
triplets = []
for i in range(0, 20000):
    fullstr = data + str(i)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()

    trip = re.search(r"(.)\1{2}", hashhex)
    if trip:
        char = trip.group(1)
        triplets.append((i, char))

for tup in triplets:
    num = tup[0]
    char = tup[1]
    regexp = r"" + char + r"{5}"

    for i in range(num + 1, num + 1000):
        fullstr = data + str(i)
        hashed = md5(fullstr.encode())
        hashhex = hashed.hexdigest()

        quin = re.search(regexp, hashhex)
        if quin:
            valid_key_idx.append(num)
            break

print(f"The {valid_key_idx[62]}th index produces the 64th key.")

# GOAL 2
"""To implement key stretching, whenever you generate a hash,
before you use it, you first find the MD5 hash of that hash,
then the MD5 hash of that hash, and so on, a total of 2016 additional hashings.
Always use lowercase hexadecimal representations of hashes.

Given the actual salt in your puzzle input and using 2016 extra
MD5 calls of key stretching, what index now produces
your 64th one-time pad key?"""

triplets = []
quintuplets = []
for i in range(0, 25000):
    fullstr = data + str(i)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()

    for x in range(2016):
        hashed = md5(hashhex.encode())
        hashhex = hashed.hexdigest()

    trip = re.search(r"(.)\1{2}", hashhex)
    if trip:
        char = trip.group(1)
        triplets.append((i, char))

    quin = re.search(r"(.)\1{4}", hashhex)
    if quin:
        char2 = quin.group(1)
        quintuplets.append((i, char2))

valid_key_idx = []
for trip in triplets:
    t_num = trip[0]
    t_char = trip[1]

    for quin in quintuplets:
        q_num = quin[0]
        q_char = quin[1]

        if q_num in range(t_num + 1, t_num + 1000) and t_char == q_char:
            valid_key_idx.append(t_num)
            break
        elif q_num > t_num + 1000:
            break

print(f"The {valid_key_idx[63]}rd index produces the 64th key.")
