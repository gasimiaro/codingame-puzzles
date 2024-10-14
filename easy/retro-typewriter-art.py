#https://www.codingame.com/ide/puzzle/retro-typewriter-art

t = input().split()
special_car ={
    'sp': " ",
    'bS' : "\\",
    'sQ' : "'",
}
res = ""
for car in t:
    if car == "nl":
        res += "\n"
    else:
        number,rep = "",""
        for i in car:
            if i.isdigit():
                number += i
            else:
                rep += i
        if rep in special_car:
            rep = special_car[rep]
        if number == car:
            rep = car[-1]
            number = car[:-1]
        if number:
            res += rep * int(number)        

print(res)
