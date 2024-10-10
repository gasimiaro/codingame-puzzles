#https://www.codingame.com/ide/puzzle/queen-control
col = input()
color = "w" if col == "white" else "b"
chess_table =[]
q_place = [0,0]
nb_control = 0
for i in range(8):
    line = input()
    chess_table.append(list(line))
    q_find= line.find("Q")
    if q_find != -1:
        q_place = [q_find,i]
x =q_place[0]
y = q_place[1]
# print(q_place[0],q_place[1])
#horizontal right
if x + 1 < 8:
    for i in range(x+1,8):
        if chess_table[y][i] == "." :
            nb_control += 1
        elif chess_table[y][i] == color :
            break
        else:
            nb_control +=1
            break
#horizontal left
if x - 1 >= 0:
    for i in range(x-1,-1,-1):
        if chess_table[y][i] == "." :
            nb_control += 1
        elif chess_table[y][i] == color :
            break
        else:
            nb_control +=1
            break

#vertical up
if y - 1 >= 0:
    for i in range(y-1,-1,-1):
        if chess_table[i][x] == "." :
            nb_control += 1
        elif chess_table[i][x]== color :
            break
        else:
            nb_control +=1
            break

#vertical down
if y + 1 <8:
    for i in range(y+1,8):
        if chess_table[i][x]== "." :
            nb_control += 1
        elif chess_table[i][x] == color :
            break
        else:
            nb_control +=1
            break

#diagonal right down
if y + 1 <8 and x + 1 <8:
        y_prime = y +1
        x_prime = x + 1
        while y_prime <8 and x_prime<8:
            if chess_table[y_prime][x_prime]== "." :
                nb_control += 1
                y_prime += 1 
                x_prime += 1
            elif chess_table[y_prime][x_prime] == color :
                break
            else:
                nb_control +=1
                break

#diagonal right up
if y - 1 >= 0 and x + 1 <8:
        y_prime = y - 1
        x_prime = x + 1
        while y_prime >= 0 and x_prime<8:
            if chess_table[y_prime][x_prime]== "." :
                nb_control += 1
                y_prime -= 1 
                x_prime += 1
            elif chess_table[y_prime][x_prime] == color :
                break
            else:
                nb_control +=1
                break

#diagonal left up
if y - 1 >= 0 and x - 1 >= 0:
        y_prime = y - 1
        x_prime = x - 1
        while y_prime >= 0 and x_prime >= 0:
            if chess_table[y_prime][x_prime]== "." :
                nb_control += 1
                y_prime -= 1 
                x_prime -= 1
            elif chess_table[y_prime][x_prime] == color :
                break
            else:
                nb_control +=1
                break

#diagonal left down
if y + 1 <8 and x - 1 >= 0:
        y_prime = y + 1
        x_prime = x - 1
        while y_prime < 8 and x_prime >= 0:
            if chess_table[y_prime][x_prime]== "." :
                nb_control += 1
                y_prime += 1 
                x_prime -= 1
            elif chess_table[y_prime][x_prime] == color :
                break
            else:
                nb_control +=1
                break


print(nb_control)



