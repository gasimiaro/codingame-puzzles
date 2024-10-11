#https://www.codingame.com/ide/puzzle/ghost-legs

w, h = map(int, input().split())

top_labels = input().split('  ')
positions = list(range(len(top_labels)))

for i in range(1, h - 1):
    line = input().split('|')
    
    for j in range(len(line)):
        if line[j] == '--':
            for k in range(len(positions)):
                if positions[k] == j - 1:
                    positions[k] += 1
                elif positions[k] == j:
                    positions[k] -= 1

bottom_labels = input().split('  ')

for i in range(len(top_labels)):
    print(top_labels[i] + bottom_labels[positions[i]])
