#https://www.codingame.com/ide/puzzle/treasure-hunt


h, w = map(int, input().split())

tab = []
start_x, start_y = 0, 0
for i in range(h):
    row = input()
    if 'X' in row:
        start_x, start_y = row.index('X'), i 
    tab.append(list(row)) 

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    current_gold = 0
    if tab[y][x].isdigit():  
        current_gold = int(tab[y][x])
    
    tab[y][x] = '#'
    
    max_gold = current_gold 
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < w and 0 <= ny < h and tab[ny][nx] != '#':  
            max_gold = max(max_gold, current_gold + dfs(nx, ny))  
    
    tab[y][x] = ' ' if current_gold == 0 else str(current_gold)
    
    return max_gold

result = dfs(start_x, start_y)

print(result)
