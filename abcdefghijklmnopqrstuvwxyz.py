#https://www.codingame.com/ide/puzzle/abcdefghijklmnopqrstuvwxyz

n = int(input())  # Number of lines in the grid
alphabet = "abcdefghijklmnopqrstuvwxyz"
all_input = []
for i in range(n):
    m = input()  # Read each line of the grid
    all_input.append(list(m))

# Create an output initialized with dashes ('-')
output = ["-" * len(all_input[0]) for _ in range(n)]

# Dictionary to store coordinates of found letters
coord = {}
alphabet_to_find = 0  # Index of the letter to search for in 'alphabet'

# Search for letters in the grid
for i in range(n):
    for j in range(len(all_input[0])):
        alphabet_to_find = 0  # Start with the first letter of the alphabet
        if all_input[i][j] == alphabet[alphabet_to_find]:
            x, y = i, j
            coord[alphabet[alphabet_to_find]] = [x, y]  # Store coordinates
            alphabet_to_find += 1

            # Traverse to find the next letters of the alphabet
            while alphabet_to_find < len(alphabet):
                next_found = False
                # Check neighbors in all directions (right, left, down, up)
                if y + 1 < len(all_input[0]) and all_input[x][y + 1] == alphabet[alphabet_to_find]:
                    y += 1  # Move to the right
                    next_found = True
                elif y - 1 >= 0 and all_input[x][y - 1] == alphabet[alphabet_to_find]:
                    y -= 1  # Move to the left
                    next_found = True
                elif x + 1 < n and all_input[x + 1][y] == alphabet[alphabet_to_find]:
                    x += 1  # Move downwards
                    next_found = True
                elif x - 1 >= 0 and all_input[x - 1][y] == alphabet[alphabet_to_find]:
                    x -= 1  # Move upwards
                    next_found = True

                # If the next letter is found, store its coordinates
                if next_found:
                    coord[alphabet[alphabet_to_find]] = [x, y]
                    alphabet_to_find += 1
                else:
                    break  # Stop if no next letter is found

            # Stop the outer loop if the entire alphabet has been found
            if alphabet_to_find == len(alphabet):
                break
    if alphabet_to_find == len(alphabet):
        break

# Place the found letters into the output grid
for letter, (x, y) in coord.items():
    output[x] = output[x][:y] + letter + output[x][y + 1:]

# Print the final output
for line in output:
    print(line)




#best way
# n = int(input())
# grid = [list(input())for _ in range(n)]

# def dfs(x,y,positions,chars):
#     if chars and chars[-1] == "z":
#         new_grid = [[chars[positions.index((x,y))] if (x,y) in positions else "-" for x in range(n)] for y in range(n)]

#         print("\n".join("".join(k) for k in new_grid))
#         quit()

#     if not chars or x >= 0 and x < len(grid) and y >= 0 and y < len(grid) and grid[y][x] == chr(ord(chars[-1])+1):
#         chars.append(grid[y][x])
#         positions.append((x,y))
        
#         dfs(x,y-1,positions,chars)
#         dfs(x,y+1,positions,chars)
#         dfs(x-1,y,positions,chars)
#         dfs(x+1,y,positions,chars)

# for y,yv in enumerate(grid):
#     for x,xv in enumerate(yv):
#         if xv == "a":
#             dfs(x,y,[],[])