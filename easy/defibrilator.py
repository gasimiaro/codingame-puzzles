#https://www.codingame.com/ide/puzzle/defibrillators

import math

lon = input().replace(",",".")
lat = input().replace(",",".")
n = int(input())
all_defib = []
for i in range(n):
    defib = input().split(";")
    all_defib.append(defib)
min_d = float('inf')

nearest_defib = all_defib[0][1]
for defib in all_defib:
    lon_defib = defib[-2].replace(",",".")
    lat_defib = defib[-1].replace(",",".")
    x = (math.radians(float(lon_defib)) - math.radians(float(lon)))* math.cos((math.radians(float(lat)) + math.radians(float(lat_defib)))/2)
    y = math.radians(float(lat_defib)) - math.radians(float(lat))
    d = abs(math.sqrt(x**2 + y**2) * 6371)
    if min(min_d,d) == d:
        min_d = d
        nearest_defib = defib[1]


print(nearest_defib)
