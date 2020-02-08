# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:33:09 2020

@author: laura
"""

#%% IMPORTS
from hashlib import md5

#%% DATA
data = "cxdnnyjw"
#%% GOAL 1
"""You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time by finding the MD5 hash of some Door ID (your puzzle input) and an increasing integer index (starting with 0). A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash is the next character of the password.

Given the actual Door ID, what is the password?"""

#%% SOLUTION 1
password = []
for i in range(1, 1000000000):
    fullstr = data + str(i)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()
    
    if hashhex.startswith("00000"):
        password.append(hashhex[5])

    if len(password) == 8:
        break

print("The answer is", "".join(password))

#%% GOAL 2
"""As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism. Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also indicates the position within the password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character represents the position (0-7), and the seventh character is the character to put in that position.

A hash result of 000001f means that f is the second character in the password. Use only the first result for each position, and ignore invalid positions.

Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a cinematic "decrypting" animation."""

#%% SOLUTION 2
password2 = ["", "", "", "", "", "", "", ""]
replacements = 0
for i in range(1, 100000000):
    fullstr = data + str(i)
    hashed = md5(fullstr.encode())
    hashhex = hashed.hexdigest()
    
    if hashhex.startswith("00000"):
        position = hashhex[5]
        try:
            position = int(position)
            if password2[position] == "":
                password2[position] = hashhex[6]            
        except:
            pass
         
print("The real password is", "".join(password2))
  
    
