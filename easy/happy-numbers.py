#https://www.codingame.com/ide/puzzle/happy-numbers

n = int(input())
for i in range(n):
    x = input()
    som = sum(int(digit)**2 for digit in x)
    seen_sums = set()  # To track sums and avoid infinite loops

    while som != 1 and som not in seen_sums:
        seen_sums.add(som)
        som = sum(int(digit)**2 for digit in str(som))

    print(f"{x} :)" if som == 1 else f"{x} :(")
