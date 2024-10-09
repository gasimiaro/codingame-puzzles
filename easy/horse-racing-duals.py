#https://www.codingame.com/ide/puzzle/horse-racing-duals

n = int(input())
horses = []
for i in range(n):
    pi = int(input())
    horses.append(pi)
horses.sort()
min_diff = horses[1]-horses[0]
for i in range(2,n):
    min_diff = min(min_diff,(horses[i]-horses[i-1]))
print(min_diff)
