#https://www.codingame.com/ide/puzzle/count-your-coins


value_to_reach = int(input())
n = int(input())
all_coins = {}
coins = []
step = 0
somme =0
for i in input().split():
    count = int(i)
    coins.append(count)
for i,val in enumerate(input().split()):
    value = int(val)
    all_coins[value] = coins[i]

sort_coins = dict(sorted(all_coins.items())) #sort the dict 
good = False
for key in sort_coins:
    while sort_coins[key] > 0 : #count first the low price
        somme += key
        sort_coins[key] -= 1
        step += 1

        if somme >= value_to_reach:
            good = True
            break
    if somme >= value_to_reach:
            good = True
            break

print(step if good else "-1")
