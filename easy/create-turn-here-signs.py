#https://www.codingame.com/ide/puzzle/create-turn-here-signs

import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

direction,rep,h,w,big_space, small_space = input().split()
direction = ">" if direction == "right" else "<"
output = []
for i in range(int(h)):
    line = ""
    if direction == ">":
        if i < math.ceil(int(h)/2):
            line += " "*(i*int(small_space)) #add first indentation
        else:
            line += " "*(int(h)*int(small_space) - (i+1)*int(small_space))
    else:
        if i < math.ceil(int(h)/2):
            line += " "*((math.ceil(int(h)/2) -i-1)*int(small_space)) #add first indentation
        else:
            line += " "*((i+1)*int(small_space) - math.ceil(int(h)/2)*int(small_space) )
        
        
    for j in range(int(rep)):    
        line += direction * int(w)
        if j < int(rep) - 1:
            line += " " * int(big_space)
    output.append(line)



for line in output:
        print(line)
