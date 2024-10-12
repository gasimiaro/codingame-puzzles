#https://www.codingame.com/ide/puzzle/the-river-i-


r_1 = int(input())
r_2 = int(input())
river1 = {r_1}
river2 = {r_2}
meet = False
equal = 0
while not meet:
    r_1 += sum([int(i) for i in str(r_1)])
    r_2 += sum([int(i) for i in str(r_2)])
    river1.add(r_1)
    river2.add(r_2)
    if r_1 in river2:
        meet = True
        equal = r_1
    elif r_2 in river1:
        meet = True
        equal = r_2
print(equal)
