# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:21:51 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
#%% DATA
data = []
with(open("Data - Day06.txt", "r")) as file:
    for line in file:
        data.append(line.strip())
        
data = pd.DataFrame(data)
#%% GOAL 1
"""Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?"""

#%% SOLUTION 1
data = data[0].str.split("", expand = True)
data = data.drop([0, 9], axis = 1)

message = []
for i in data.columns:
    message.append(data[i].mode().iloc[0])

print("".join(message))

#%% GOAL 2
"""Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?"""

#%% SOLUTION 2
message2 = []
for i in data.columns:
    message2.append(data[i].value_counts().index[-1])

print("".join(message2))