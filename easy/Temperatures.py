#https://www.codingame.com/ide/puzzle/temperatures

n = int(input()) 
if n == 0:
    print("0")
else:
    all_temp =list(map(int,input().split()))
    nearest = min(all_temp,key=abs)
    print(abs(nearest) if abs(nearest) in all_temp else nearest)

