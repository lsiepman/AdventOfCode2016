# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:22:37 2020

@author: laura
"""

#%% IMPORTS
import pandas as pd
import re
from collections import Counter
import numpy as np
#%% DATA 
data = []
with(open("Data - Day04.txt", "r")) as file:
    for line in file:
        data.append(line)
data = pd.DataFrame(data)
#%% GOAL 1
"""Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization.

What is the sum of the sector IDs of the real rooms?"""

#%% ANSWER 1
def FindNum(string):
    return int(re.search("[0-9]+", string).group())
    
def FindChecksum(string):
    result = re.search("\[(\w+)\]", string).group(1)
    result = sorted(result)
    
    return "".join(result)


def FindLetters(string):
    return sorted(re.search("^[a-z-]+", string).group().replace("-", ""))  

def FindCommonLetters(list_of_letters):
    list_of_letters = Counter(list_of_letters).most_common(5)
    list_of_letters = dict(list_of_letters)
    list_of_letters = sorted(list_of_letters.keys())
    list_of_letters = "".join(list_of_letters)    
    return list_of_letters

data["num"] = data[0].apply(FindNum)
data["checksum"] = data[0].apply(FindChecksum)
data["letters"] = data[0].apply(FindLetters)
data["common_letters"] = data["letters"].apply(FindCommonLetters)
data["real"] = np.where(data["checksum"] == data["common_letters"], True, False)

answer = data.loc[data["real"] == True]
print("The sum of real room IDs is", sum(answer.num))

#%% GOAL 2
"""With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?"""

#%% SOLUTION 2
def Decrypt(string, shift):
    result = ""
    
    for i in string:
        if i == " ":
            result += " "
        elif i.isalpha():
            result += chr(((ord(i) - ord('a') + shift) % 26) + ord('a'))
                
    return result

def FindWords(string):
    return re.search("^[a-z-]+", string).group().replace("-", " ") 
    

data["Words"] = data[0].apply(FindWords)
decrypted = []
for i in range(len(data)):
    decrypted.append(Decrypt(data["Words"][i], data["num"][i]))
data["Decrypted"] = decrypted

for i in range(len(data["Decrypted"])):
    if data["Decrypted"][i].startswith("north"):
        x = i

print("The sector ID for the North Pole is", data["num"][810])
                     