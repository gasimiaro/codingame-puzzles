#https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop

while True:
    remaining_turns = int(input())  
    path= ""
    if light_y > initial_ty:
        initial_ty += 1
        path += "S"
    elif light_y < initial_ty:
        initial_ty -= 1
        path += "N"

    if light_x < initial_tx:
        initial_tx -= 1
        path += "W"
    elif light_x > initial_tx:
        initial_tx += 1
        path += "E"
    
    print(path)