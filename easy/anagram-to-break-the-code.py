#https://www.codingame.com/ide/puzzle/anagram-to-break-the-code

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = input().lower()
s = input()
res = []
for symbole in [":",".",",","!","?"]:
    s = s.replace(symbole," ") #replace all symbol with space
words = s.split() #create list
trouver = False
for i,word in enumerate(words):
    if len(word) == len(w):
        if sorted(word.lower()) == sorted(w) and word.lower() != w:
            first = str(i)[-1]
            res.append(first)

            second = len(words) - i - 1
            res.append(str(second)[-1])

            before_letter = "".join(words[:i])
            third = len(before_letter)
            res.append(str(third)[-1])

            after_letter = "".join(words[i+1:])
            fourth = len(after_letter)
            res.append(str(fourth)[-1])

            trouver = True
            break


print(".".join(res) if trouver else "IMPOSSIBLE")
