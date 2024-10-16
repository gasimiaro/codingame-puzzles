#https://www.codingame.com/ide/puzzle/embedded-chessboards


import math

n = int(input())  # Number of test cases

for _ in range(n):
    row, col, isWhite = map(int, input().split())
    good = 0  # Counter for valid chessboards

    # There must be at least 8 rows and 8 columns to form a chessboard
    if row < 8 or col < 8:
        print(0)
        continue  # Skip this test case if the grid is too small

    # Number of valid rows and columns where a chessboard can start
    valid_rows = row - 7
    valid_cols = col - 7

    for i in range(valid_rows):
        # Calculate how many columns can have a white bottom-right corner
        cols_count = valid_cols // 2 if valid_cols % 2 == 0 else math.ceil(valid_cols / 2)
        
        # If the row is even and isWhite is 1, the corner must be white, otherwise adjust for odd rows
        if (i % 2 == 0 and isWhite == 1) or (i % 2 != 0 and isWhite == 0):
            good += cols_count
        else:
            good += valid_cols - cols_count

    # Output the number of valid chessboards for this test case
    print(good)


