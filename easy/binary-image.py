#https://www.codingame.com/ide/puzzle/binary-image

h = int(input())
res = []
for i in range(h):
    row = map(int,input().split())
    out = ""
    white = True
    for nb in row:
        if white :
            out += "."*nb
            white = not white
        else:
            out += "O"*nb
            white = not white
    res.append(out)
 
if all([len(out) == len(res[0]) for out in res ]):
    for val in res:
        print(val)
else:
    print("INVALID")
