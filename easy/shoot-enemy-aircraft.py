#https://www.codingame.com/ide/puzzle/shoot-enemy-aircraft

n = int(input())
carte = []
nb_aircraft = 0
for i in range(n-1):
    line = input()
    for index,c in enumerate(list(line)) :
        if c == "<":
            carte.append(["-1",index,i])
        elif c == ">":
            carte.append(["+1",index,i])
    
    nb_aircraft += line.count("<")
    nb_aircraft += line.count(">")

missile = [input().index("^"),n]
while nb_aircraft > 0:
    shootable = False
    for index,aircraft in enumerate(carte.copy()):
        if abs(aircraft[1] - missile[0]) == abs(aircraft[2] - missile[1]):
            nb_aircraft -=1
            print("SHOOT")
            shootable =True
            del carte[index]
        aircraft[1] += int(aircraft[0])
    if not shootable:
        print("WAIT")


