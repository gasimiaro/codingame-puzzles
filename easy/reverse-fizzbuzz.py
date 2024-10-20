#https://www.codingame.com/ide/puzzle/reverse-fizzbuzz

n = int(input())
autre = []
begin = 1
dictio = {
    "Fizz": [],
    "Buzz": [],
    "FizzBuzz": []
}

# Lecture des entrées et remplissage des listes
for i in range(n):
    line = input()
    if line in dictio:
        dictio[line].append(i)
    else :
        begin = int(line) - i
        autre.append(int(line))

f,b =1,1
# print(dictio["Fizz"][0])
if dictio["Fizz"] and len(dictio["Fizz"]) > 1:
    for i in range(2,dictio["Fizz"][-1]+ begin +1) :
        # print(i)
        if i not in autre and all((dictio["Fizz"][j] + begin ) % i == 0 for j in range(len(dictio["Fizz"]))  ):
            f = i
            break
elif not dictio["Fizz"]:
    for i in range(2,dictio["FizzBuzz"][-1]+ begin +1) :
        # print(i)
        if i not in autre and all((dictio["FizzBuzz"][j] + begin ) % i == 0 for j in range(len(dictio["FizzBuzz"]))  ):
            f = i
            break
else:
    f =  dictio["Fizz"][0]+ begin

if dictio["Buzz"] and len(dictio["Buzz"]) > 1:
    for i in range(2,dictio["Buzz"][-1]+ begin +1) :
        # print(i)
        if i not in autre and all((dictio["Buzz"][j] + begin ) % i == 0 for j in range(len(dictio["Buzz"]))  ):
            b = i
            break
elif not dictio["Buzz"]:
    for i in range(2,dictio["FizzBuzz"][-1]+ begin +1) :
        # print(i)
        if i not in autre and all((dictio["FizzBuzz"][j] + begin ) % i == 0 for j in range(len(dictio["FizzBuzz"]))  ):
            b = i
            break  
else:
    b =  dictio["Buzz"][0]+ begin
print(f, b)