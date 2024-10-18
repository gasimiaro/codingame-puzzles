#https://www.codingame.com/ide/puzzle/the-river-ii-

# Calculates the next river number (e.g., 7 -> 14, 14 -> 19, etc.).
def getNextRiverNumber(riverNumber):
    nextRiverNumber = riverNumber
    while riverNumber > 0:
        nextRiverNumber += riverNumber % 10  # Add the last digit of riverNumber.
        riverNumber //= 10  # Remove the last digit from riverNumber.
    return nextRiverNumber

# Read input.
r1 = int(input())

riversMeetR1 = False

# Find if any river meets r1.
for i in range(r1 - 1, 0, -1):  # Loop backwards from r1 - 1 to 1.
    if getNextRiverNumber(i) == r1:
        riversMeetR1 = True  # A river meets r1.
        break  # No need to check further, so break out of the loop.

# Output whether any river meets r1.
print("YES" if riversMeetR1 else "NO")
