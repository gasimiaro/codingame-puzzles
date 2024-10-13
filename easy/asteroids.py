#https://www.codingame.com/ide/puzzle/asteroids

import math

# Parsing inputs
w, h, t1, t2, t3 = [int(i) for i in input().split()]
first, second = [], []

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    first.append(first_picture_row)
    second.append(second_picture_row)

third = [['.'] * w for _ in range(h)]

final_positions = {}

for y in range(h):
    for x in range(w):
        if first[y][x] != '.':
            asteroid = first[y][x]  

            for y2 in range(h):
                for x2 in range(w):
                    if second[y2][x2] == asteroid:
                        dx = x2 - x
                        dy = y2 - y

                        move_x = math.floor((dx * (t3 - t2)) / (t2 - t1))
                        move_y = math.floor((dy * (t3 - t2)) / (t2 - t1))

                        new_x = x2 + move_x
                        new_y = y2 + move_y

                        if 0 <= new_x < w and 0 <= new_y < h:
                            if (new_y, new_x) not in final_positions or asteroid < final_positions[(new_y, new_x)]:
                                final_positions[(new_y, new_x)] = asteroid

for (y, x), asteroid in final_positions.items():
    third[y][x] = asteroid

for row in third:
    print("".join(row))
