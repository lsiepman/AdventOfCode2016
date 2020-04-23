# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:12:42 2020.

@author: laura
"""

# IMPORTS
import re

# GOAL 1
"""Wandering around a secure area, you come across a datalink port
 to a new part of the network. After briefly scanning it for interesting
 files, you find one file in particular that catches your attention.
 It's compressed with an experimental format, but fortunately,
 the documentation for the format is nearby.

The format compresses a sequence of characters. Whitespace is ignored.
To indicate that some sequence should be repeated, a marker is added to
the file, like (10x2). To decompress this marker, take the subsequent 10
 characters and repeat them 2 times. Then, continue reading the file after
 the repeated data. The marker itself is not included in the decompressed
 output.

If parentheses or other characters appear within the data referenced by a
marker, that's okay - treat it like normal data, not a marker, and then
resume looking for markers after the decompressed section."""

# DATA
data = ""
with(open("Data - Day09.txt")) as f:
    for line in f:
        data += line

# ANSWER 1
def find_first_answer(string, decompressed_file):
    string = string.strip()
    while len(string) > 0:
        try:
            marker = re.search(r"\(\d+x\d+\)", string).group()
            marker = marker.replace(")", "").replace("(", "")
            num_char = int(marker.split("x")[0])
            mult_var = int(marker.split("x")[1])
            preceding_text, text_after = re.compile(r"\(\d+x\d+\)").split(string, 1)

            selected_text = text_after[:num_char]
            decompressed_text = selected_text * mult_var

            decompressed_file += preceding_text
            decompressed_file += decompressed_text

            string = text_after[num_char:]

        except AttributeError:
            decompressed_file += string
            string = ""

    return decompressed_file

decompressed_file = find_first_answer(data, "")
print(f"The length of the decompressed file is {len(decompressed_file)}")

# GOAL 2
"""Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed
data are decompressed. This, the documentation explains, provides much
more substantial compression capabilities, allowing many-gigabyte files
to be stored in only a few kilobytes.

Unfortunately, the computer you brought probably doesn't have enough memory
 to actually decompress the file; you'll have to come up with another way
 to get its decompressed length."""


# ANSWER 2
def find_second_answer(string):
    string.strip()
    answer = 0
    i = 0
    while i < len(string):
        if string[i] == '(':
            mark = string.find(')', i)
            num_char, mult_val =\
                [int(x) for x in string[i + 1:mark].split('x')]

            answer += find_second_answer(string[mark + 1:mark + num_char + 1]) * mult_val
            i = mark + num_char
        else:
            answer += 1
        i += 1

    return answer

find_second_answer(data)


