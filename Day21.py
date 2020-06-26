# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:40:56 2020.

@author: laura
"""

# IMPORTS
import re

# DATA
password = "abcdefgh"
data = []
with(open("Data - Day21.txt")) as file:
    for line in file:
        data.append(line.strip())

# GOAL 1
"""The scrambling function is a series of operations
(the exact list is provided in your puzzle input).
Starting with the password to be scrambled, apply each operation in
 succession to the string. The individual operations behave as follows:
        - swap position X with position Y means that the letters at
        indexes X and Y (counting from 0) should be swapped.
        - swap letter X with letter Y means that the letters X and Y should
        be swapped (regardless of where they appear in the string).
        - rotate left/right X steps means that the whole string should be
        rotated; for example, one right rotation would turn abcd into dabc.
        - rotate based on position of letter X means that the whole string
        should be rotated to the right based on the index of letter X
        (counting from 0) as determined before this instruction does any
        rotations. Once the index is determined, rotate the string to
        the right one time, plus a number of times equal to that index,
        plus one additional time if the index was at least 4.
        - reverse positions X through Y means that the span of letters at
        indexes X through Y (including the letters at X and Y) should be
        reversed in order.
        - move position X to position Y means that the letter which is at
        index X should be removed from the string, then inserted such that it
        ends up at index Y.

Now, you just need to generate a new scrambled password and you can access the
system. Given the list of scrambling operations in your puzzle input,
what is the result of scrambling abcdefgh?
"""

# ANSWER 1
def swap_position(instruction, word):
    num1 = re.search(r"^swap\sposition\s(\d)", instruction).group(1)
    num1 = int(num1)
    let1 = word[num1]

    num2 = re.search(r"(\d)$", instruction).group(1)
    num2 = int(num2)
    let2 = word[num2]

    word = word[:num1] + let2 + word[num1 + 1:]
    word = word[:num2] + let1 + word[num2 + 1:]

    return word

def swap_letter(instruction, word):
    let1 = re.search(r"^swap\sletter\s(\w)", instruction).group(1)
    num1 = word.index(let1)

    let2 = re.search(r"(\w)$", instruction).group(1)
    num2 = word.index(let2)

    word = word[:num1] + let2 + word[num1 + 1:]
    word = word[:num2] + let1 + word[num2 + 1:]

    return word

def rotate_sideways(instruction, word):
    num_shift = int(re.search(r"(\d)", instruction).group(1))

    if "left" in instruction:
        word = word[num_shift:] + word[:num_shift]
    elif "right" in instruction:
        word = word[-num_shift:] + word[:-num_shift]
    else:
        print("Unknown rotate")

    return word

def rotate_position(instruction, word):
    let_shift = re.search(r"(\w)$", instruction).group(1)
    num_shift = word.index(let_shift)

    if num_shift >= 4:
        num_shift += 2
    else:
        num_shift += 1
    new_word = word[-num_shift:] + word[:-num_shift]

    return new_word

def reverse(instruction, word):
    regex = re.search(r"(\d)\sthrough\s(\d)", instruction)
    num1 = int(regex.group(1))
    num2 = int(regex.group(2)) + 1

    new_order = word[num1:num2][::-1]
    word = word[:num1] + new_order + word[num2:]

    return word

def move(instruction, word):
    regex = re.search(r"(\d)\sto\sposition\s(\d)", instruction)
    num1 = int(regex.group(1))
    num2 = int(regex.group(2))

    let = word[num1]
    temp = word[:num1] + word[num1 + 1:]
    word = temp[:num2] + let + temp[num2:]

    return word

def find_answer_1(word, data):
    for i in data:
        if "swap position" in i:
            word = swap_position(i, word)
        elif "swap letter" in i:
            word = swap_letter(i, word)
        elif "rotate left" in i or "rotate right" in i:
            word = rotate_sideways(i, word)
        elif "rotate based on position" in i:
            word = rotate_position(i, word)
        elif "reverse" in i:
            word = reverse(i, word)
        elif "move" in i:
            word = move(i, word)
        else:
            print("Error, unexpected instruction")

    print(f"The scrambled password is: {word}")

find_answer_1(password, data)
