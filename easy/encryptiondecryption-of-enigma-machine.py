#https://www.codingame.com/ide/puzzle/encryptiondecryption-of-enigma-machine

operation = input()
pseudo_random_number = int(input())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotor = []
for i in range(3):
    rotor.append(input())
message = input()
pseudo = ""
res = ""
if operation == "ENCODE":
    for i in range(len(message)):
        new_index = (alphabet.index(message[i]) + pseudo_random_number + i) % len(alphabet)
        pseudo += alphabet[new_index]
    for r in rotor:
        new_pseudo = ""
        for c in pseudo:
            index_alphabet = alphabet.index(c)
            new_pseudo += r[index_alphabet]
        pseudo = new_pseudo
    print(pseudo)
else:        
    for i in range(2,-1,-1):
        new_pseudo = ""
        for c in message:
            index_in_rotor = rotor[i].index(c) 
            new_pseudo += alphabet[index_in_rotor]
        message = new_pseudo
    
    for i in range(len(message)):
        new_index = (alphabet.index(message[i]) - pseudo_random_number - i) % len(alphabet)
        pseudo += alphabet[new_index]
    print(pseudo)

