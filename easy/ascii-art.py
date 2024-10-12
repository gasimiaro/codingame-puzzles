#https://www.codingame.com/ide/puzzle/ascii-art

l = int(input())
h = int(input())
t = input().upper()
res = ""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
for i in range(h):
    row = input()
    for letter in t:
        if letter not in alphabet:
            res += row[-l:] # If the letter is not in the alphabet, we print the last l characters of the row
        else:
            deb_letter = alphabet.index(letter)*l # We get the index of the letter in the alphabet and multiply it by l to get the starting index of the letter in the row
            res += row[deb_letter:deb_letter+l]

    res += "\n"   # Add a new line after each row   
    
print(res)

