#https://www.codingame.com/ide/puzzle/rooks-movements


position = input()
rook_position = [ord(position[0]) - ord("a"),int(position[1]) -1]
nb_pieces = int(input())
res = []
chess = [["."]*8 for _ in range(8)] #create chess table
for i in range(nb_pieces):
    inputs = input().split()
    colour = (inputs[0])
    one_piece = inputs[1]
    x = ord(one_piece[0]) - ord("a")
    y = int(one_piece[1]) - 1 
    chess[y][x] = colour

directions = [(-1,0),(0,-1),(1,0),(0,1)]


for dx,dy  in directions:
    x,y= rook_position[0],rook_position[1]
    while 0<= x + dx <8 and 0 <= y + dy < 8 :
            x += dx
            y += dy

            if chess[y][x] == ".":
                res.append(f"R{position}-{chr(ord('a') + x )}{y + 1}")

            elif  chess[y][x] == "0":  # the same color
                break    
            else :
                res.append(f"R{position}x{chr(ord('a') + x )}{y + 1}")
                break


res.sort()


for i in res:
    print(i)
