#https://www.codingame.com/ide/puzzle/sudoku-validator 


valable = True
sudoku = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))
    if sum(sudoku[i]) != 45 and len(set(sudoku[i])) != 9:
        valable = False 
        break
som = sum([sum(x) for x in sudoku])
#vertical
if valable:
    for x in range(9):
        if sum(sudoku[y][x] for y in range(9)) !=45 or len(set(sudoku[y][x] for y in range(9))) != 9:
            valable = False
            break

# 3 * 3
if valable:
    for x in range(3):
        for y in range(3):
            if sum(sudoku[x*3+i][y*3+j] for i in range(3) for j in range(3)) != 45 or  len(set(sudoku[x*3+i][y*3+j] for i in range(3) for j in range(3)) ) != 9:
                valable = False
                break            

print("true" if valable else "false")

