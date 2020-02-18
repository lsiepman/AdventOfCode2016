# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:06:39 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import re
import regex as re2
#%% DATA
data = []
with(open("Data - Day07.txt", "r")) as file:
    for line in file:
        data.append(line.strip())

#%% GOAL 1
"""While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets."""

#%% SOLUTION 1
def SplitLines(line):
    lst = re.split(r'\[|\]', line)
    return lst[1::2], lst[::2]

def CheckABBA(string):
    return any(i != j for i, j in re2.findall(r'(.)(.)\2\1', string, overlapped=True))

num = 0
for i in data:
    inside, outside = SplitLines(i)
    if any(CheckABBA(j) for j in outside) and not any(CheckABBA(j) for j in inside):
        num += 1

print(num)

#%% GOAL 2
"""You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

How many IPs in your puzzle input support SSL?"""

#%% SOLUTION 2
def CheckABAandBAB(string):
    bab_aba = []
    for i,j in re2.findall(r'(.)(.)\1', string, overlapped=True):
        if i != j:
            bab_aba.append(j+i+j)
    return bab_aba


count = 0
for line in data:
    inside, outside = SplitLines(line)
    babs = []
    for k in inside:
        for bab in CheckABAandBAB(k):
            babs.append(bab)

    lst = []
    for bab in babs:
        for m in outside:
            if bab in m:
                lst.append(True)

    if any(lst):
        count +=1
print(count)
